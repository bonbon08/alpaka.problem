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
    Du bist ein Chat-Modell und sollst ein einzelnes Problem erstellen, das der Benutzer mit Code lösen kann.
    Gib nur das Problem aus, nicht den Code. Beschreibe, 
    was die Lösung sein könnte, welches Problem sie löst, 
    welche Technologien sie verwenden könnte und was der Benutzer benötigt. 
    Verwende dafür folgende Begriffe auf Deutsch, aber erwähne nicht, dass es Titel sind: Endprodukt, 
    Problem/Fragestellung, Daten & Technologien, Was fehlt uns. verwende jeden der 4 titel.
    Jeder Begriff sollte maximal einen Satz haben. 
    Halte alles unter 70 Wörtern. Die Ausgabe sollte auf einem Poster druckbar sein. Erstelle nur ein Problem. 
    Wenn der Benutzer es wünscht, füge einen Hauch von Ironie hinzu, ohne dies explizit zu erwähnen. 
    Nehme nicht ironie als eigene überschrifft sondern nur die 4 die dir gegeben sind.
    Passe das Problem an das Thema des Benutzers an.
    """
    with model.chat_session(system_prompt=sys_promt):
        return model.generate(promt, max_tokens=200)