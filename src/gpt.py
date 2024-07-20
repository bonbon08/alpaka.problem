from gpt4all import GPT4All


model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf") 

def get_ai_return(trolllevel, theme):
    seriousnesses = [
        "sehr ernst",
        "ernst",
        "nahezu ernst",
        "teilweise ernst",
        "ein bisschen ernst",
        "eher weniger ernst",
        "nicht ernst",
        "ein wenig ironisch",
        "teilweise ironisch",
        "ironisch",
        "sehr ironisch"
    ]
    promt = "Mein Thema ist: " + theme + " und es soll ernsthafftigkeit " + seriousnesses[trolllevel] +" haben, bitte halte die formulierung der worte und wort wahl auf dem nivou eines durchnittlichen 12-18 jährigen"
    sys_promt="""
    You are a chat model that should gennerate problems for the user to solve with code, you should not output any code but only a problem,
    you should output what the solution could be, what problem it solves, what technolgies the solution might use and what the the user might
    need to make this solution please make for each of each of these a Title and after that print the information the Titles should be (german):
    Endprodunkt, Problem/Fragestellung, Daten&technologien and was fehlt uns create a maximum of 1 sentence for each title?
    . Your output should be directly printable on a poster.
    Only create one single problem and not more because we only want on problem so just create one and not two make only one or two senteces for each title
    your answer should be in german and you should make it a little bit trolly if the user wants to 
    and the problem should be themed after the wish of the user.
    """
    with model.chat_session(system_prompt=sys_promt):
        return model.generate(promt, max_tokens=256)