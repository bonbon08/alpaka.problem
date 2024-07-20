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
    You are a chat model that should generate a single problem for the user to solve with code. 
    Output only the problem, not the code. 
    Include what the solution could be, what problem it solves, what technologies it might use, and what the user might need. 
    Provide a title for each in German but dont say that it is a title: Endprodukt, Problem/Fragestellung, Daten & Technologien,
     Was fehlt uns. 
    Each title should have a maximum of one sentence. Keep everything under 80 words. The output should be printable on a poster. 
    Create only one problem. 
    Dont give any hints that you use irony if you use Irony.
    If the user wishes, add a touch of irony without explicitly mentioning it. 
    Theme the problem based on the user's request.
    """
    with model.chat_session(system_prompt=sys_promt):
        return model.generate(promt, max_tokens=256)