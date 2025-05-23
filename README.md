# Simplified LLM Question Answering API

A streamlined FastAPI backend for interacting with LLM models via OpenAI-compatible APIs.

## Features

- Simple configuration
- Structured logging
- Simple and full chat endpoints
- Type validation with Pydantic
- Interactive API documentation

## Project Structure

```
├── app.py             # FastAPI application and routes
├── config.py          # Configuration settings and message templates
├── schemas.py         # Pydantic models for API
├── utils.py           # Utility functions and logger setup
└── requirements.txt   # Project dependencies
```

## Setup

### 方式一：使用 pip

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

Or with uvicorn directly:

```
uvicorn app:app --host 0.0.0.0 --port 8989 --reload
```

### 方式二：使用 uv（推荐）

1. 安装 uv（一个快速的 Python 包管理器）：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 克隆仓库：

```bash
git clone https://github.com/cyuQ1n/AISeed.git
cd AISeed
```

3. 创建并激活虚拟环境：

```bash
uv venv --python 3.12
source .venv/bin/activate  # Unix/macOS 系统
# Windows 系统使用：
# .venv\Scripts\activate
```

4. 安装依赖：

```bash
uv pip install -r requirements.txt
```

## Configuration

You can configure the server by editing the `config.py` file or by setting environment variables:
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8989)
- `API_BASE`: OpenAI API base URL
- `API_KEY`: OpenAI API key
- `DEFAULT_MODEL`: Default model to use

## API Documentation

Interactive documentation available at:
- **Swagger UI**: `http://localhost:8989/docs`
- **ReDoc**: `http://localhost:8989/redoc`

## API Endpoints

### Health Check
- `GET /`: Simple health check endpoint

### Chat Completion
- `POST /chat`: Full chat completion with custom messages
- `POST /simple`: Simplified chat endpoint with just a message parameter

## API Usage Examples

### Simple Chat

```python
import requests

response = requests.post(
    "http://localhost:8989/simple",
    params={
        "message": "What is the capital of France?",
        "model_name": "Qwen/Qwen2.5-7B-Instruct"
    }
)
print(response.json())
```

### Full Chat API

```python
import requests

response = requests.post(
    "http://localhost:8989/chat",
    json={
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
        "model_name": "Qwen/Qwen2.5-7B-Instruct",
        "temperature": 0.7
    }
)
print(response.json())
```

## License

MIT License 