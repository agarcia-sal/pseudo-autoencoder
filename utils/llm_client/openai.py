import logging
import os
import time
# from typing import Optional
from typing import List, Dict, Optional
from .base import BaseClient

try:
    from openai import OpenAI
except ImportError:
    OpenAI = 'openai'


logger = logging.getLogger(__name__)

class OpenAIClient(BaseClient):

    ClientClass = OpenAI

    def __init__(
        self,
        model: str,
        temperature: float = 1.0,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> None:
        super().__init__(model, temperature)
        api_key = os.getenv('OPENAI_API_KEY')
        if isinstance(self.ClientClass, str):
            logger.fatal(f"Package `{self.ClientClass}` is required")
            exit(-1)
        
        self.client = self.ClientClass(api_key=api_key, base_url=base_url)
        
    
    def _chat_completion_api(self, messages: list[dict], temperature: float, n: int = 1):
        response = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=temperature, n=n, stream=False,
        )
        return response.choices
        # payload = {
        #     "model": self.model,
        #     "messages": messages,
        #     "temperature": temperature,
        #     "n": n
        # }
        
        # response = self.client.session.post(
        #     f"{self.base_url}/chat/completions",
        #     json=payload,
        #     timeout=30  # Add timeout to prevent hanging
        # )
        # response.raise_for_status()  # Raise exception for bad status codes
        
        # return response.json()["choices"]
    
    def multi_chat_completion_batch(self, messages_list: List[List[Dict]], n: int = 1, temperature: Optional[float] = None):
        """
        Use OpenAI's batch endpoint - most efficient for many requests!
        """
        import openai
        
        # Prepare requests for batch API
        assert isinstance(messages_list, list), "messages_list should be a list."
        if not isinstance(messages_list[0], list):
            messages_list = [messages_list]
        
        if len(messages_list) > 1:
            assert n == 1, "Currently, only n=1 is supported for multi-chat completion."

        # Create batch - this sends all requests at once
        batch = self.client.batches.create(
            input_file={"requests": messages_list},
            endpoint="/v1/chat/completions",
        )
        
        # Wait for completion and process results
        while batch.status != "completed":
            time.sleep(5)  # Check every 5 seconds
            batch = self.client.batches.retrieve(batch.id)
        
        contents = []
        for result in batch.results:
            if result.status == "succeeded":
                response = result.body
                contents.extend([choice['message']['content'] for choice in response['choices']])
            else:
                contents.append(f"Error: {result.error}")
        
        return contents
    

