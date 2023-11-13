"""
This is a sample API code to send a text to the server and recieve speech
for the given text.

Supported languages: 

Assamese, Bengali, Bodo, Gujarati, Hindi, Kannada, Malayalam, Manipuri
Marathi, Odia, Punjabi, Rajasthani, Tamil, Telugu, Urdu

"""
import requests
import json
import base64

# endpoint
url = "http://localhost:5000/tts"

lang = 'hindi'
gender = 'female'
text = "सुप्रभात, आप कैसे हैं?" # hindi
# text = "സുപ്രഭാതം, സുഖമാ?" # malayalam
# text = "সুপ্ৰভাত, তুমি কেনে?" # manipuri
# text = "सुप्रभात, तुम्ही कसे आहात?" # marathi
# text = "ಶುಭೋದಯ, ನೀವು ಹೇಗಿದ್ದೀರಿ?" # kannada
# text = "बसु म्विथ्बो, बरि दिबाबो?" # bodo male yet to be added <---
# text = "Good morning, how are you?" # english
# text = "সুপ্ৰভাত, আপুনি কেমন আছে?" # assamese
# text = "காலை வணக்கம், நீங்கள் எப்படி இருக்கின்றீர்கள்?" # tamil
# text = "ସୁପ୍ରଭାତ, ଆପଣ କେମିତି ଅଛନ୍ତି?"
# text = "सुप्रभात, आप कैसे छो?" # rajasthani
# text = "శుభోదయం, మీరు ఎలా ఉన్నారు?" # telugu
# text = "সুপ্রভাত, আপনি কেমন আছেন?" # bengali
# text = "સુપ્રભાત, તમે કેમ છો?" # gujarati

payload = json.dumps(
    {
    "input": text,
    "gender": gender,
    "lang": lang,
    "alpha": 1 # to control speed
    })

headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload).json()

# save the received encoded audio
audio = response['audio']
file_name = "tts.wav"
wav_file = open(file_name,'wb')
decode_string = base64.b64decode(audio)
wav_file.write(decode_string)
wav_file.close()