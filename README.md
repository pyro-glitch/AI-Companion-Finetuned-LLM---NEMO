# AI-Companion-Finetuned-LLM-NEMO

---

### This is an AI based friendly companion assistant. The main intention of creating this is have a friendly companion with which the user can share their thoughts and get a lively and friendly response from the AI.

### The AI is enable with performing some basic tasks on the trigger of a wake word 'Nemo'. The number and types of tasks can be added as per need. As for the current time being the AI has the ability to following the following tasks:

#### - Searching the web for a query
#### - Open any app on the device
#### - Provide time of any location
#### - Play music (This feature has not been implemented completely)

---

## Tech Stack:
| Feature | Tech Stack used|
| :-----: | :---: |
| FrontEnd           | HTML, CSS, JS                                       |
| Backend            | Python, Ell framework( Connect Python to Js)        |  
| LLM Used           | Dialoge GPT by Microsoft                            |
| Store in the cloud | Hugging Face                                        | 
| Text To Speech     | pyttsx3 library                                     |
| Speech to Text     | speech_recognition library                          |
| Open Apps          | AppOpener library                                   |
| Time Functions     | geopy, timezonefinder library, API (www.timeapi.io) |

---

### Hugging Face link to original model
[microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium)

### Hugging Face link to finetuned model 
[pyro-glitch/NEMO-DialoGPT-medium-model](https://huggingface.co/pyro-glitch/NEMO-DialoGPT-medium-model)
