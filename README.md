# LLM Question Answering API

A simple, reusable FastAPI backend for interacting with LLM models via OpenAI-compatible APIs.

## Features

- Multiple API endpoint configurations
- Retry mechanism for API calls
- Structured logging
- Simple and advanced chat endpoints
- Type validation with Pydantic
- Interactive API documentation

## Project Structure

```
├── app.py              # FastAPI application and routes
├── config.py           # Configuration settings
├── prompts.py          # System prompts and message templates
├── schemas.py          # Pydantic models for API
├── utils.py            # Utility functions and logger setup
├── requirements.txt    # Project dependencies
└── .env.example        # Example environment variables
```

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your API keys
3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

Or with uvicorn directly:

```
uvicorn app:app --host 0.0.0.0 --port 8989 --reload
```

## Configuration

You can configure the server settings by editing the `config.py` file or by setting environment variables:
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8989)

## API Documentation

The API includes interactive documentation:
- **Swagger UI**: `http://localhost:8989/docs`
- **ReDoc**: `http://localhost:8989/redoc`

## API Endpoints

### Health Check
- `GET /`: Simple health check endpoint

### Chat Completion
- `POST /chat`: Full chat completion with custom messages
- `POST /simple_chat`: Simplified chat endpoint with just a message parameter

## API Usage Examples

### Simple Chat

```python
import requests

response = requests.post(
    "http://localhost:8989/simple_chat",
    params={
        "message": "What is the capital of France?",
        "api_endpoint": "default"
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
        "temperature": 0.7,
        "api_endpoint": "default"
    }
)
print(response.json())
```

## Configuration

Edit the `config.py` file to add or modify API endpoint configurations. You can define multiple API endpoints with different models and base URLs.

## License

MIT License 