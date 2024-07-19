import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v0.6", torch_dtype=torch.bfloat16, device_map="auto")


theme = input("Theme==> ")
troll = input("Trolllevel[0-10]==> ")

messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who wants the help the user with the task of finding a problem to solve with the code with the theme the user choose and the troll level please answer in german",
    },
    {"role": "user", "content": "Please create a problem in german to solve with code with the theme " + theme + " and the troll level " + troll + "/10"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])