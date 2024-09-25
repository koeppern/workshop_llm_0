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


## Parameters
msg = [
    "I'm Johannes.",
    "What is my name?",
]

## Application
tools = Tools()

tools.init_tools()

# variant 1 - no appending of messages
res = tools.chat_completion(
	messages=[
		{"role": "user", "content": msg[0]}
	]
)

print(res)

res = tools.chat_completion(
	messages=[
		{"role": "user", "content": msg[1]}
	]
)

print(res)

## Variant 2 - appending of messages
messages =[{"role": "user", "content": msg[0]}]

res = tools.chat_completion(
	messages=messages
)

print(res)

messages.append({"role": "assistant", "content": res})

messages.append({"role": "user", "content": msg[1]})

res = tools.chat_completion(
	messages=messages
)

print(res)
