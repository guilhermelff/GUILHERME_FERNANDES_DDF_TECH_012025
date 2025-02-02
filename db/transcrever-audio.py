import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcriber_mp3_para_txt(arquivo_mp3, arquivo_txt):
    """
    Transcreve um arquivo MP3 em um arquivo TXT.

    Args:
        arquivo_mp3: O caminho para o arquivo MP3.
        arquivo_txt: O caminho para o arquivo TXT de saída.
    """

    # Carrega o arquivo MP3
    sound = AudioSegment.from_mp3(arquivo_mp3)

    # Divide o áudio em partes menores para melhorar a precisão da transcrição
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40)

    # Cria um reconhecedor de fala
    r = sr.Recognizer()

    # Abre o arquivo TXT para escrita
    with open(arquivo_txt, "w") as f:
        # Itera sobre as partes do áudio
        for i, chunk in enumerate(chunks):
            # Exporta a parte do áudio para um arquivo WAV temporário
            chunk_file = f"chunk{i}.wav"
            chunk.export(chunk_file, format="wav")

            # Reconhece a fala na parte do áudio
            with sr.AudioFile(chunk_file) as source:
                audio_data = r.record(source)

            # Transcreve a fala
            try:
                text = r.recognize_google(audio_data, language="en-US")
                f.write(text + " ")
            except sr.UnknownValueError:
                print(f"Não foi possível entender a fala na parte {i}")
            except sr.RequestError as e:
                print(f"Erro na requisição ao serviço de reconhecimento de fala: {e}")

            # Remove o arquivo WAV temporário
            import os
            os.remove(chunk_file)


arquivo_mp3 = r"C:\Users\Guilherme\Documents\GUILHERME_FERNANDES_DDF_TECH_012025\products.mp3"  # Substitua pelo caminho do seu arquivo MP3
arquivo_txt = r"C:\Users\Guilherme\Documents\GUILHERME_FERNANDES_DDF_TECH_012025\transcricao.txt"  # Substitua pelo caminho do arquivo TXT de saída

transcriber_mp3_para_txt(arquivo_mp3, arquivo_txt)