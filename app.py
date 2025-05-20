from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import (
    APP_NAME, APP_VERSION, APP_DESCRIPTION,
    DEFAULT_MODEL,HOST, PORT, DOCS_URL, REDOC_URL, OPENAPI_URL
)
from prompts import create_chat_messages, DEFAULT_SYSTEM_PROMPT
from schemas import ChatRequest, ChatResponse, HealthResponse, Message
from utils import get_chat_completion, logger

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
    openapi_url=OPENAPI_URL
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=HealthResponse)
async def health_check():
    """API health check endpoint"""
    return HealthResponse(version=APP_VERSION)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat completion endpoint
    
    Send a request to get a response from the LLM
    """
    try:
        # Get parameters with defaults
        modelName = request.modelName or DEFAULT_MODEL
        temperature = request.temperature or 0.7
        
        # Convert request messages to format expected by OpenAI
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Get completion from the model
        response = get_chat_completion(
            messages=messages,
            model_name=modelName,
            temperature=temperature
        )
        
        # Return the response
        return ChatResponse(
            response=response,
            modelUsed=modelName
        )
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.post("/simple", response_model=ChatResponse)
async def simple_chat_endpoint(
    message: str,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    modelName: str = DEFAULT_MODEL,
    temperature: float = 0.7
):
    """
    Simple chat endpoint that only requires a message
    """
    try:
        # Create messages using the helper function
        messages = create_chat_messages(
            user_message=message,
            system_prompt=system_prompt
        )
        
        # Convert to dict format expected by OpenAI
        messages_dict = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
        
        # Get completion
        response = get_chat_completion(
            messages=messages_dict,
            model_name=modelName,
            temperature=temperature
        )
        
        # Return the response
        return ChatResponse(
            response=response,
            modelUsed=modelName
        )
        
    except Exception as e:
        logger.error(f"Error in simple chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server at http://{HOST}:{PORT}")
    logger.info(f"API documentation available at http://{HOST}:{PORT}{DOCS_URL}")
    logger.info(f"API documentation available at http://localhost:{PORT}{DOCS_URL}")
    uvicorn.run("app:app", host=HOST, port=PORT, reload=False) 