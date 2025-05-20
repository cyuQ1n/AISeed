from typing import Dict, List, Any, Optional

# System prompts
DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question is not clear or factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

def create_chat_messages(user_message, system_prompt=DEFAULT_SYSTEM_PROMPT, chat_history=None):
    """Create a properly formatted list of messages for the chat completion API"""
    messages = [{"role": "system", "content": system_prompt}]
    
    if chat_history:
        messages.extend(chat_history)
    
    messages.append({"role": "user", "content": user_message})
    
    return messages 