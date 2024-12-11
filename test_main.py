from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestLevel1:

    def test_stdout(self):
        response = client.post("/execute", json={"code": "print('Hello World!')"})

        assert response.status_code == 200
        assert "stdout" in response.json()
        assert response.json()["stdout"] == "Hello World!\n"

    def test_stderr(self):
        response = client.post("/execute", json={"code": "1/0"})

        assert response.status_code == 200
        assert "stderr" in response.json()
        assert response.json()["stderr"] == (
            "Traceback (most recent call last):\n"
            '  File "<string>", line 1, in <module>\n'
            "ZeroDivisionError: division by zero\n"
        )


class TestLevel2:

    def test_timeout_limit(self):
        response = client.post("/execute", json={"code": "while True: pass"})

        assert response.status_code == 200
        assert "error" in response.json()
        assert response.json()["error"] == "execution timeout"

    def test_memory_limit(self):
        response = client.post("/execute", json={"code": "a = 'a'*10**8"})

        assert response.status_code == 200
        assert "error" in response.json()
        assert response.json()["error"] == "execution timeout"


class TestLevel3:

    def setup_class(self):
        response = client.post("/execute", json={"code": "x = 5"})
        self.id = response.json()["id"]

    def test_new_session(self):
        response = client.post("/execute", json={"code": "x = 5"})

        assert response.status_code == 200
        assert "id" in response.json()

    def test_existing_session(self):
        response = client.post("/execute", json={"id": self.id, "code": "print(x)"})

        assert response.status_code == 200
        assert response.json() == {"id": self.id, "stdout": "5\n"}


class TestLevel4:

    def test_filesystem_access(self):
        response = client.post(
            "/execute", json={"code": "import os; os.remove('file.txt')"}
        )

        assert response.status_code == 200

        assert response.json() == {
            "id": "8ccfcbba-5a94-49a3-aecc-edb0b8273e31",
            "stderr": "Traceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\nPermissionError: [Errno 13] Permission denied: 'file.txt'\n",
        }
