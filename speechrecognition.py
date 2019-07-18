import speech_recognition as sr
import webbrowser

r=sr.Recognizer() # this command initialises the recogniser

# If you want to use audio input from microphones, PyAudio is also necessary. If not installed, the
# library speech_recognition will still work, but Microphone will not be defined

with sr.Microphone() as source: #using with keyword session will be closed automaticallly

    print("Speak!")
    audio=r.listen(source) #the recogniser will now listen to the source and save it to audio

    try:

        #for testing purposes, we're just using the default API key to use another API key, use
        #`r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`

        text=r.recognize_google(audio)   #using this command you can also convert an pre recorded audio to text
        print("You said : {}".format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text
        webbrowser.open(search_url)
        #open the url in your default browser

    except:

        print("Can't recognize")
