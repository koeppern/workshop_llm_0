"""
03_chat_flow.py
2024-09-24, Johannes Köppern

Build up a conversation by attaching the answers from the assistant and 
additional questions to the messages list.

User messages:
1. I'm Johannes.
2. What is my name?

- In first step, messages list it NOT extended and assistant won't be able to 
    answer.
- In second step, messages list is extended and assistant will be able to answer.
"""
from tools.tools import Tools


## Application
tools = Tools()

tools.init_tools()



