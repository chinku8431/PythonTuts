#Example to convert text to speech
from gtts import gTTS
gTTS(text="Hello this is Naveen",lang="en").save("one.mp3")
print(print("mp3 file is ready"))
