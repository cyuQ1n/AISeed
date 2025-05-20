from pydantic import BaseModel, Field
from typing import List, Optional

class Message(BaseModel):
    role: str = Field(..., description="Role of the message sender (system, user, assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    messages: List[Message] = Field(..., description="List of conversation messages")
    modelName: Optional[str] = Field(None, description="Name of the model to use")
    temperature: Optional[float] = Field(0.7, description="Temperature for response generation")

class ChatResponse(BaseModel):
    response: str = Field(..., description="Generated response from the model")
    modelUsed: str = Field(..., description="Name of the model that was used")

class HealthResponse(BaseModel):
    status: str = Field("ok", description="API health status")
    version: str = Field(..., description="API version") 