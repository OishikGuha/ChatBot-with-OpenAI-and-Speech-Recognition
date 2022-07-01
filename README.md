# Chatbot made with OpenAI and Google's Speech Recognition
This is a little voice chatbot I made using OpenAI's davinci and Google's speech recognition package.

## Dependencies
```
openai
Flask
SpeechRecognition
PyAudio (Can be installed from the repo)
```

## How to run
1. Go to [OpenAI's quickstart guide](https://beta.openai.com/docs/quickstart)
2. Scroll down until you find your secret key, click copy. (You may have to login first)

![image](https://user-images.githubusercontent.com/57310936/176870800-3b1bac98-52f0-42d3-9110-a7d31a4c366a.png)

3. Clone this repo.
4. Execute `pip install -r requirements.txt`
5. Go to main.py line 8 and replace "Enter your key here." with your secret key.
6. Execute main.py (`python main.py`) and go to http://127.0.0.1:5000 .
7. Finally, click "Start Recording", talk with the AI and enjoy!
