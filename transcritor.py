# Código escrito por Luiza Pozzobon

from pydub import AudioSegment
import sys
import glob
import math
import os

from speech_to_text import Transcrever

inputFilenames = []
duration = 30

for argument in sys.argv:
	# Override the filename
	if (argument[-4:].lower() == '.wav'):
		filenames = glob.glob(argument)

		for filename in filenames:
			inputFilenames.append(filename)
		continue

	if (argument[:11] == '--duration='):
		argument = int(argument[11:])

		if (argument > 0):
			duration = argument
			continue
		else:
			print('A duração é em segundos e números inteiros.')
			exit()

if (len(inputFilenames) == 0):
	print("""\
Usage:
python transcritor.py arquivo.wav arquivo2.wav arquivo3.wav ... --duration=30""")
	exit()

# Cycle through files
for inputFilename in inputFilenames:
	outputFilenamePrefix = inputFilename[:-4]
	outputFilenameNumber = 0
	try:
		inputFile = AudioSegment.from_wav(outputFilenamePrefix+".wav")
	except:
		print(inputFilename, "doesn't look like a valid .wav file.  Skipping.")
		continue

	audioDur = inputFile.duration_seconds
	audioPieces = audioDur/duration
	piecesDuration = audioPieces*30
	roundPieces = math.ceil(audioPieces)
	diffDuration = audioDur - piecesDuration

	pieceDuration = duration*1000 # em milisegundos -> 30*1000= 30 segundos

	t1 = 0
	t2 = pieceDuration

	if not os.path.exists(outputFilenamePrefix):
		os.mkdir(outputFilenamePrefix)
		print("Arquivos salvos no diretório: ", outputFilenamePrefix)
	else:
		print("Arquivos salvos no diretório: ", outputFilenamePrefix)

	for i in range(1, roundPieces):
		newAudio = inputFile[t1:t2]
		outputFilenameNumber = outputFilenameNumber + 1
		outputFilename = str(outputFilenameNumber)
		outputFilename = outputFilename.zfill(2) # Pad to 2 digits
		outputFilename = outputFilenamePrefix + "/" + outputFilenamePrefix + '-' + outputFilename + '.wav'

		print("Escrevendo em ", outputFilename)
		newAudio.export(outputFilename, format="wav")
		
		t1 = t2
		if i != (roundPieces-1):
			t2 = (i+1)*pieceDuration
		else:
			t2 = ((i+1)*pieceDuration) + diffDuration

	print("------ Fim da separação de áudios -------")

	filename = inputFilename.replace('.wav','')
	filename = outputFilenamePrefix + "/" + filename
	print("------ Começando as transcrições de ", outputFilenamePrefix, "------")
	t = Transcrever(nome_audio=filename, n_audios=roundPieces) 
	t.transcrever() # não alterar essa linha
	print("------ Fim das transcrições de ", outputFilenamePrefix, "------")