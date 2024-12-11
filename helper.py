from pydantic import BaseModel
import subprocess
import resource

class Request(BaseModel):
    id: str = None
    code: str


def set_memory_limit():
    memory_limit = 100 * 1024 * 1024  # 100 MB
    resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))


def handle_response(process: subprocess.CompletedProcess) -> dict[str, str]:
    if process.returncode == 0:
        return {"stdout": process.stdout}
    elif "MemoryError" in process.stderr:
        return {"error": "execution timeout"}
    else:
        return {"stderr": process.stderr}


def run_python_code(code: str) -> dict[str, str]:
    try:
        process = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=2,
            preexec_fn=set_memory_limit,
        )
        return handle_response(process)

    except subprocess.TimeoutExpired:
        return {"error": "execution timeout"}

    except Exception as e:
        return {"error": f"execution failed: {str(e)}"}
