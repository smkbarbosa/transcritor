# transcritor

Código para transcrever automaticamente clipes de áudio grandes em pt-br.
--------------
---- Instruções para primeira execução ----

1. Instalar Python
	1.1 Marcar a caixa da primeira tela do instalador de "Adicionar ao PATH" (ou algo assim)

2. Abrir o prompt do PowerShell ou cmd

	2.1 pip install -r requirements.txt
	
	2.2 sudo apt install ffmpeg

-------------

---- Instruções de uso ----

1. Abrir prompt do PowerShell ou cmd na pasta dos arquivos speech_to_text e transcritor

	(Shift + botão direito na pasta em que estão os arquivos de áudio e os códigos)

2. Converter audio mp3 para wav

```
ffmpeg -i <audio>.mp3 -acodec pcm_s16le -ac 1 -ar 16000 audio.wav
```

3. Digitar:

	```python transcritor.py nome_do_arquivo.wav nome_do_arquivo2.wav```


	- OBSERVAÇÕES:
	
	3.1 Pode botar quantos arquivos quiser para transcrever, mas sugiro não botar muitos se não demora muito tempo.
	
	3.2 O tempo de duração padrão para cada arquivo gerado é de 30 segundos, 
	se quiser alterar, executar o comando com o parâmetro "--duration=xx segundos".
	No exemplo abaixo, os áudios serão particionados em 40 segundos cada.

		```python transcritor.py nome_do_arquivo.wav --duration=40```

4. Aguardar. Os áudios serão particionados e transcritos automaticamente. 
Esses arquivos se encontrarão na pasta de nome igual ao arquivo de áudio principal.
