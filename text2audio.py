from google.cloud import texttospeech

def synthesize_text(text, output_file):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="id-ID", # Indonesian language code
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE # or MALE, depending on your preference
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_file}"')

# Usage example
synthesize_text("Selamat pagi. Apa kabar?", "output.mp3")
