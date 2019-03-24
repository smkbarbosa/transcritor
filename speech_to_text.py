
# -------- NÃO ALTERAR NADA ABAIXO (ATÉ PROXIMO COMENTARIO)

import speech_recognition as sr
from os import path

r = sr.Recognizer()
class Transcrever:
  
	def __init__(self, nome_audio, n_audios):
		self.nome_audio = nome_audio
		self.n_audios = n_audios

	def salvar_txt(self, text, text2):
		text_file = open(self.nome_audio + ".txt", "w")
		text_file.write(text)
		text_file.close()

		text_file = open(self.nome_audio + "2.txt", "w")
		text_file.write(text2)
		text_file.close()
    
	def transcrever(self):
		text = ""
		text2 = ""

	    #try:
		for i in range(1, self.n_audios):

			if i < 10:
				AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), self.nome_audio + "-0"+ str(i) + ".wav") # de 01 a 09
			else:
				AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), self.nome_audio + "-" + str(i) + ".wav") # de 10 em diante

			with sr.AudioFile(AUDIO_FILE) as source:
				try:
					audio = r.record(source)  # read the entire audio file
				except:
					self.salvar_txt(text, text2)


			# recognize speech using Google Speech Recognition
			try:
				t = r.recognize_google(audio, language = "pt-br")
				
				text = text + " " + t  # para texto corrido
				text2 = text2 + "\r\n" + t # para enter entre arquivos
				
				print('Foi o audio ', i)
				self.salvar_txt(text, text2)
			  
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service (provavelmente arquivo muito grande); {0}".format(e))
	    #except:
	    #  pass
    
 #--------------------- NÃO ALTERAR ACIMA
    
 # -------------------- ALTERAR ABAIXO  

if __name__ == "__main__":

	t = Transcrever(nome_audio="Helenise", n_audios=145) 
         # preencher com o nome do arquivo original e a quantia de arquivos cortados
         # Arquivo ***DEVE*** estar na mesma pasta deste código e ***DEVE*** ser formato wav
         # Ex: Arquivo Helenise.wav, separado em 145 partes com o outro algoritmo (split.py)
         #     t = Transcrever(nome_audio="Helenise", n_audios=145)
   # -----------------------------------------------------------------------

	t.transcrever() # não alterar essa linha