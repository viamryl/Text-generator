from gtts import gTTS
import os

text = "halo, selamat pagi dunia"
bahasa = "id"

file = gTTS(text = text, lang=bahasa)

file.save("hallo.mp3")

