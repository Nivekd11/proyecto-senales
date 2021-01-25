from senalDiscreta import SenalDiscreta
import numpy as np
from IPython.display import Audio
from scipy.io.wavfile import read, write
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

#Constantes and Variables:
formato=pyaudio.paInt16
canal = 1
frecuenciaDeMuestreo = 44100
tamanioVentana = 1024
tiempoGrabado = 3
nombreAudio = ''
audio = pyaudio.PyAudio()
flujo = audio.open(format=formato,channels=canal,rate=frecuenciaDeMuestreo,input=True,frames_per_buffer=tamanioVentana)
#-----------------------------------------------------------------------------------------------------------------------

def setNomebreAudio(nombre): #Establesemos el nombre del archivo de audio
    nombreAudio=nombre
    nombreAudio=nombreAudio+'.wav'

def getNomebreAudio(): #Obtenemos el Archivo de Audio
    return nombreAudio

def setTiempoDeGrabado(tiempo):
    tiempoGrabado=tiempo

def getTiempoDeGrabado():
    return tiempoGrabado

def grabarAudio():
    #Aqui Grabamos el WAV de n segundos y 
    #guardamos con el nombre de que querramos en el folder de "src"

    print('...Grabando')
    senial=[]
    for i in range(int((frecuenciaDeMuestreo/tamanioVentana)*tiempoGrabado+1)):
        data = flujo.read(tamanioVentana)
        senialDato = np.fromstring(data,dtype=np.int16)
        senial.extend(senialDato)

    print('..fin..')

    wavefile = wave.open("entrada.wav",'wb')
    wavefile.setnchannels(canal)
    wavefile.setsampwidth(audio.get_sample_size(formato))
    wavefile.setframerate(frecuenciaDeMuestreo)
    wavefile.writeframes(b''.join(senial))
    wavefile.close()
     
def obtenerSenalDiscretaDesdeAudio():
    Fr, data = read("src/entrada.wav") #Leemos archivo obteniendo frecuencia y arreglo con canales
    return SenalDiscreta(data[:,0], 0, False) #Se toma como data solo el primer canal

def obtenerAudioDesdeSenalDiscreta(senal):
    write("src/salida.wav", frecuenciaDeMuestreo, np.array(senal.obtener_datos()))

