# Python Code Execution Server

A secure, containerized Python code execution server built with FastAPI that provides a sandboxed environment for running Python code snippets. This project demonstrates modern Python web development practices, security considerations, and containerization.

## 🚀 Features

- **Secure Code Execution**: Sandboxed environment with memory and execution time limits
- **Session Management**: Maintains code execution context across requests
- **RESTful API**: Clean and intuitive API endpoints
- **Comprehensive Testing**: Extensive test suite covering various execution scenarios
- **Docker Support**: Containerized deployment for consistent environments
- **API Documentation**: Interactive API documentation with Swagger UI and ReDoc

## 🔒 Security Features

- Memory usage limits (100MB per execution)
- Execution timeout (2 seconds)
- Restricted filesystem access
- Containerized execution environment
- Non-root user execution

## 🛠️ Technology Stack

- FastAPI - Modern, fast web framework for building APIs
- Python 3.9+ - Core programming language
- Docker - Containerization
- Pytest - Testing framework
- Uvicorn - ASGI server

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

### Local Development Setup

1. Create and activate virtual environment:

```bash
python -m venv venv

# For Linux/Mac
source venv/bin/activate

# For Windows
.\venv\Scripts\activate.bat
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Running Tests

```bash
pytest
```

## 🐳 Docker Deployment

1. Build the Docker image:

```bash
docker build -t pyserver .
```

2. Run the container:

```bash
docker run -p 8000:8000 pyserver
```

## 📝 API Usage

### Execute Python Code

```bash
POST /execute
Content-Type: application/json

{
    "code": "print('Hello, World!')"
}
```

### Maintain Execution Context

```bash
POST /execute
Content-Type: application/json

{
    "id": "session-id",
    "code": "print(x)"  # Access variables from previous executions
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
