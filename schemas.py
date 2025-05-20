from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Optional, Any

class Message(BaseModel):
    role: str = Field(..., description="Role of the message sender (system, user, assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    messages: List[Message] = Field(..., description="List of conversation messages")
    model_name: Optional[str] = Field(None, description="Name of the model to use")
    temperature: Optional[float] = Field(0.7, description="Temperature for response generation")
    api_endpoint: Optional[str] = Field("default", description="API endpoint to use")

class ChatResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    
    response: str = Field(..., description="Generated response from the model")
    model_used: str = Field(..., description="Name of the model that was used")
    api_endpoint: str = Field(..., description="API endpoint that was used")

class HealthResponse(BaseModel):
    status: str = Field("ok", description="API health status")
    version: str = Field(..., description="API version") 