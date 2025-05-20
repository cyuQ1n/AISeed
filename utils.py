import time
import datetime
from loguru import logger
from openai import OpenAI
from typing import List, Dict

from config import (
    DEFAULT_MODEL, 
    API_BASE, 
    API_KEY, 
    MAX_RETRIES,
    RETRY_DELAY,
    DEFAULT_TEMPERATURE
)

# Configure logger
logger.add(
    "app.log",
    rotation="10 MB",
    retention="1 week",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# Initialize API client
client = OpenAI(base_url=API_BASE, api_key=API_KEY)

def get_chat_completion(
    messages: List[Dict[str, str]], 
    model_name: str = DEFAULT_MODEL, 
    temperature: float = DEFAULT_TEMPERATURE, 
    max_retries: int = MAX_RETRIES, 
    retry_delay: int = RETRY_DELAY
) -> str:
    """
    Get a response from the LLM
    
    Args:
        messages: List of message objects
        model_name: Name of the model to use
        temperature: Temperature parameter for response generation
        max_retries: Maximum number of retries
        retry_delay: Delay between retries in seconds
        
    Returns:
        Generated response text
    """
    # Log the user's query
    user_message = ""
    for msg in messages:
        if msg.get("role") == "user":
            user_message = msg.get("content", "")
    
    logger.info(f"User query: {user_message}")
    
    # Attempt to get completion with retries
    retries = 0
    while retries < max_retries:
        try:
            start_time = time.time()
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=temperature,
            )
            output = completion.choices[0].message.content
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_tokens = completion.usage.total_tokens
            
            logger.info(
                f"Call time: {datetime.datetime.now()}, "
                f"Model: {model_name}, Tokens: {total_tokens}, "
                f"Duration: {elapsed_time:.2f}s"
            )
            
            # Log a preview of the response
            max_log_length = 100
            log_response = output[:max_log_length] + ("..." if len(output) > max_log_length else "")
            logger.info(f"Model response: {log_response}")
            
            return output
            
        except Exception as e:
            retries += 1
            logger.error(f"Error calling get_chat_completion (attempt {retries}/{max_retries}): {str(e)}")
            if retries < max_retries:
                time.sleep(retry_delay)
            else:
                logger.error("Maximum retries reached, returning error message")
                return f"Error: Model call failed. Reason: {str(e)}" 