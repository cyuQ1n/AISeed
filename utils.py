import time
import datetime
from loguru import logger
from openai import OpenAI
from typing import List, Dict, Any, Optional
import urllib.parse

from config import (
    DEFAULT_MODEL, 
    DEFAULT_API_BASE, 
    DEFAULT_API_KEY, 
    API_CONFIGS,
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

# Initialize API client dictionary
clients = {
    "default": OpenAI(base_url=DEFAULT_API_BASE, api_key=DEFAULT_API_KEY)
}

# Initialize all configured API clients
for api_name, config in API_CONFIGS.items():
    clients[api_name] = OpenAI(base_url=config["API_BASE"], api_key=config["API_KEY"])

def get_chat_completion(
    messages: List[Dict[str, str]], 
    model_name: str = DEFAULT_MODEL, 
    temperature: float = DEFAULT_TEMPERATURE, 
    max_retries: int = MAX_RETRIES, 
    retry_delay: int = RETRY_DELAY, 
    api_endpoint: str = "default"
) -> str:
    """
    Get a response from the LLM
    
    Args:
        messages: List of message objects
        model_name: Name of the model to use
        temperature: Temperature parameter for response generation
        max_retries: Maximum number of retries
        retry_delay: Delay between retries in seconds
        api_endpoint: Name of the API endpoint configuration to use
        
    Returns:
        Generated response text
    """
    # Get the appropriate API client
    if api_endpoint in clients:
        client = clients[api_endpoint]
    else:
        logger.warning(f"API endpoint '{api_endpoint}' not found, using default")
        client = clients["default"]
        
    # If using a specific API endpoint configuration, use its model name unless explicitly specified
    if api_endpoint in API_CONFIGS and model_name == DEFAULT_MODEL:
        model_name = API_CONFIGS[api_endpoint]["BASE_MODEL"]
    
    # 记录用户的最后一条消息（一般是当前查询）
    user_message = ""
    for msg in messages:
        if msg.get("role") == "user":
            user_message = msg.get("content", "")
    
    logger.info(f"用户查询: {user_message}")
    
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
                f"调用时间: {datetime.datetime.now()}, API端点: {api_endpoint}, "
                f"模型: {model_name}, Token数: {total_tokens}, 耗时: {elapsed_time:.2f}秒"
            )
            
            # 记录模型回复（限制长度避免日志过长）
            max_log_length = 100
            log_response = output[:max_log_length] + ("..." if len(output) > max_log_length else "")
            logger.info(f"模型回复: {log_response}")
            
            return output
            
        except Exception as e:
            retries += 1
            logger.error(f"get_chat_completion 调用出错 (第{retries}/{max_retries}次尝试): {str(e)}")
            if retries < max_retries:
                time.sleep(retry_delay)
            else:
                logger.error("达到最大重试次数，返回错误信息")
                return f"错误: 模型调用失败，原因: {str(e)}" 