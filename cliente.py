from langserve import RemoteRunnable

chain_remote = RemoteRunnable("https://localhost:8000/conversa")
response = chain_remote.invoke({"question": "what are you?"})
print(response)