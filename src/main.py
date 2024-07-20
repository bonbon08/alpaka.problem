from gpt4all import GPT4All

trolllevel = 5
theme = "Klima"

seriousnesses = [
    "sehr ernst",
    "ernst",
    "nahezu ernst",
    "teilweise ernst",
    "ein bisschen ernst",
    "eher weniger ernst",
    "nicht ernst",
    "ein wenig trollend",
    "teilweise trollend",
    "trollend",
    "sehr trollend"
]

model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf", model_path=".cache/") 

promt = "Mein Thema ist: " + theme + " und es soll ernsthafftigkeit " + seriousnesses[trolllevel] +" haben, bitte halte die formulierung der worte und wort wahl auf dem nivou eines durchnittlichen 12-18 jährigen"
sys_promt="""
You are a chat model that should gennerate problems for the user to solve with code, you should not output any code but only a problem,
 you should output what the solution could be, what problem it solves, what technolgies the solution might use and what the the user might
need to make this solution please make for each of each of these a Title and after that print the information the Titles should be (german):
Endprodunkt, Problem/Fragestellung, Daten&technologien and was fehlt uns?
. Your output should be directly printable on a poster.

your answer should be in german and you should make it a little bit trolly if the user wants to 
(you will get a number from 0 to 10 about how trolly it should be but just intigrate this factor into your answer but into the hole answerd not only in one specific 
part of your answer and dont talk about it)
and the problem should be themed after the wish of the user.
"""
with model.chat_session(system_prompt=sys_promt):
    print(model.generate(promt, max_tokens=512))