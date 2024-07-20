from gpt4all import GPT4All
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf", model_path=".cache/") 
with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=128))