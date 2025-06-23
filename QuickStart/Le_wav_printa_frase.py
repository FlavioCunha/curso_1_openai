from pydub import AudioSegment
import speech_recognition as sr

# Converta para PCM WAV
audio = AudioSegment.from_file("dog.wav")
audio.export("dog_pcm.wav", format="wav", codec="pcm_s16le")

# Agora reconheça o áudio convertido
def wav_to_text(filepath):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio, language="pt-BR")

texto = wav_to_text("dog_pcm.wav")
palavras = texto.split()
print(' '.join(palavras[:15]))

# Esse erro ocorre porque o pydub precisa do programa ffmpeg instalado no seu sistema para manipular arquivos de áudio,
# e ele não foi encontrado.