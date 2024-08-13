import pyttsx3
import eel
import random
from UseModel import UseModels
from ExecuteCommands import CommandHandler
import speech_recognition as sr

# Speech to text
print("Setting up Speech to text")
listener = sr.Recognizer()

# Text to speech
print("Setting up text to speech")
speaker = pyttsx3.init()
speaker.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
speaker.setProperty('rate', speaker.getProperty('rate')-75)

# init UseModel class
print("Setting up Model")
model_name = "saved_model/NEMO_AI_Compainon_v0.5"
UseModel=UseModels()
UseModel.getModelFromSaved("saved_model/DialogGPT-medium-model")
UseModel.getTokenizerFromSaved("saved_model/DialogGPT-medium-tokenizer")
UseModel.setMemory(5)

# UI
print("Setting up UI")
eel.init('UI')

# Command Handler
CH = CommandHandler

@eel.expose
def getVoiceInput():
    try:
        with sr.Microphone() as source:
            audio = listener.listen(source)
            text = listener.recognize_google(audio)
    except:
        text = "#error"
    return text

def selectTask(command):
    command = command[5:]
    command = command.lower()
    command = command.split()
    print(command)

    if (command[:3] == ["play", "the", "song"]):
        if (len(command) > 1):
            songName = " ".join([str(elem) for i, elem in enumerate(command[3:])])
        else:
            songName = command[3:]

        return CH.playMusic(CH, name=songName)

    elif (command[:4] == ["what", "is", "the", "time"]):
        if (command[4] == "now"):
            return CH.getTime(CH, str="now")
        elif (command[4] == "in"):
            return CH.getTime(CH, str=command[5])

    elif (command[0] == "open"):
        return CH.openApp(CH, name=command[1])

    elif (command[0] == "search"):
        command.pop(0)
        if(len(command)>1):
            query = " ".join([str(elem) for i, elem in enumerate(command)])
        else:
            query=command[0]
        CH.search(CH, query)
        return "Searching the web for "+query

    else:
        return "I think that's a invalid command"

commandMode=0
@eel.expose
def chat(user_input):
    print("ME:  ", user_input)

    commandMode=0
    if (user_input.startswith("Nemo ") or user_input.startswith("nemo ")):
        commandMode=1
        try:
            response = selectTask(user_input)
        except:
            response="Sorry, I didn't get it could you repeat it again?"

    if(commandMode==0):
        response = UseModel.inference(user_input)

        print("BOT: ", response)

    # speak response
    speaker.say(response)
    speaker.runAndWait()

    return response


# start the app
eel.start('index.html', mode='chrome' ,size=(420, 680))

# selectTask("Nemo search youtube")
# selectTask("Nemo open word")
# selectTask("Nemo what is the time in berlin")
# selectTask("Nemo play the song shape of you")

