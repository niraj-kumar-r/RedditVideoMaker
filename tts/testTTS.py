from gtts import gTTS

myText = "Which profession attracts the worst kinds of people?"

language = 'en'

output = gTTS(text=myText, lang=language, slow=False, tld='us')

output.save("output.mp3")

