from gpt4all import GPT4All

trolllevel = "2"
theme = "Klima"

model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf", model_path=".cache/") 

promt = "Mein Thema ist: " + theme + " und es soll ein trollevel " + trolllevel +"/10 haben"

with model.chat_session(system_prompt="You are a chat model taht should gennerate problems for the user to solve with code, you should not output any code but only a problem, you should output what the solution could be, what problem it solves, what technolgies the solution might use and what the the user might need to make this solution. Your output should be directly printable on a poster. your answer should be in german and you should make it a little bit trolly if the user wants to (you will get a number from 0 to 10 about how trolly it should be) and the problem should be themed after the wish of the user"):
    print(model.generate(promt, max_tokens=1024))