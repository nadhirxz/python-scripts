import pyttsx3 

man = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
woman = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
converter = pyttsx3.init()

converter.setProperty("voice", woman)
converter.setProperty("rate", 150) 
converter.setProperty("volume", 1) 
converter.say(input("Yout text : "))

converter.runAndWait()