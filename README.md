---
Model Type: Text to Speech
Supported Languages: Assamese, Bengali, Bodo, Gujarati, Hindi, Kannada, Malayalam, Manipuri, Marathi, Odia, Punjabi, Rajasthani, Tamil, Telugu, Urdu
---
***Demo: [IITM-TTS Demo](https://iitm-tts.onrender.com) | This may take approximately 30 seconds to load the first time and will go idle after 15 minutes of inactivity.***

# Fastspeech2_HS_Flask_API

This repository contains the Flask API implementation of the Text to Speech Model developed by the Speech Lab at IIT Madras. 
For a comprehensive understanding of the models and inference details, please consult the original repository 
[Fastspeech2_HS](https://github.com/smtiitm/Fastspeech2_HS).

### Table of Contents
- [Setup](#setup)
- [Installation](#installation)
- [Run Flask server](#run-flask-server)
- [API](#api)
- [Citation for the original repo](#citation-for-the-original-repo)

### Setup
Some of the large files in this repo are uploaded using git lfs. Install latest git LFS by following the given commands:

Some of the large files in this repository have been uploaded using Git-LFS. 
To ensure seamless handling of these files, please install Git-LFS by executing the provided commands:

```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.python.sh | bash
sudo apt-get install git-lfs
git lfs install
```

The entire repository, including the models, has been uploaded to Hugging Face 
"[Fastspeech2_HS_Flask_API](https://huggingface.co/k-m-irfan/Fastspeech2_HS_Flask_API)" due to size restrictions on GitHub for Git LFS. 
To clone the repository from Hugging Face, please use the following command:

```bash
git clone https://huggingface.co/k-m-irfan/Fastspeech2_HS_Flask_API
```

Alternatively, you can download the models from the original repository [Fastspeech2_HS](https://github.com/smtiitm/Fastspeech2_HS) 
and organize the folder structure as specified below. Skip this step if already cloned the repository from Hugging Face.

```bash
models
├── hindi
│   ├── female
│   └── male
├── tamil
│   ├── female
│   └── male
.
.
.
└── marathi
    ├── female
    └── male
```

### Installation:

Create a virtual environment and activate it:
```bash
python3 -m venv tts-hs-hifigan
source tts-hs-hifigan/bin/activate
```

Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### Run Flask server:
Ensure the server application is running correctly before proceeding. Use the following commands and check for any errors:
```bash
python3 flask_app.py
# OR
gunicorn -w 2 -b 0.0.0.0:5000 flask_app:app --timeout 600
```

If the application is running without any issues, proceed to start the server using the following command:
```bash
bash start.sh
```

### API
```python
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
```

### Citation for the original repo
If you use this Fastspeech2 Model in your research or work, please consider citing:

“
COPYRIGHT
2023, Speech Technology Consortium,
Bhashini, MeiTY and by Hema A Murthy & S Umesh,
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
and
ELECTRICAL ENGINEERING,
IIT MADRAS. ALL RIGHTS RESERVED "


Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
