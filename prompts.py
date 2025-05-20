from typing import Dict, List, Any, Optional

# System prompts for different use cases
DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question is not clear or factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

CODING_SYSTEM_PROMPT = """You are a skilled programming assistant. Provide clear, efficient and well-commented code examples. Explain your approach when helpful but focus mainly on providing working solutions. When appropriate, mention potential edge cases or optimizations."""

QA_SYSTEM_PROMPT = """You are a question answering assistant. Your goal is to provide accurate, comprehensive answers to user questions. Base your answers on facts and reliable information. If you're unsure, acknowledge the limitations in your knowledge rather than speculating."""

# Template functions for common message structures
def create_chat_messages(
    user_message: str, 
    system_prompt: str = DEFAULT_SYSTEM_PROMPT, 
    chat_history: Optional[List[Dict[str, str]]] = None
) -> List[Dict[str, str]]:
    """
    Create a properly formatted list of messages for the chat completion API
    
    Args:
        user_message: The user's current message
        system_prompt: The system prompt to use
        chat_history: Optional list of previous messages
        
    Returns:
        Formatted list of messages
    """
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add chat history if provided
    if chat_history:
        messages.extend(chat_history)
    
    # Add the current user message
    messages.append({"role": "user", "content": user_message})
    
    return messages 