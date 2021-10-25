import time, os
from notifypy import Notify
from playsound import playsound
import threading

tasks_time = 25
pomodoro = ""
break_time = 5
count = 0
pausar = False

def timer(tempo):
    warn(tempo)
    tempo = tempo * 60
    while(tempo>0):
        time.sleep(1)
        tempo = tempo - 1
        printTerminal(tempo)
   

def warn(tempo):
    mensagem = ""
    titulo = ""
    notification = Notify()

    if(tempo==15 or tempo==5):
        titulo = "PAUSA"
        mensagem = "Pausa de "+str(tempo)+" minutos"
    else:
        titulo = "MÃOS À MASSA"
        mensagem = "Estudo de "+str(tempo)+" minutos "

    notification.title = titulo
    notification.message = mensagem
    notification.send()
    playsound('ring.mp3')
    
def printTerminal(tempo):
    
    minutos = int(tempo/60)
    segundos = int(tempo - (minutos*60))
    # os.system('clear')   
    if segundos>=10:
        if minutos<10:
            print("0"+str(minutos)+":"+str(segundos), end="\r")
        else:
            print(str(minutos)+":"+str(segundos), end="\r")
    else:
        if minutos<10:
            print("0"+str(minutos)+":0"+str(segundos), end="\r")
        else:
            print(str(minutos)+":0"+str(segundos), end="\r")

def isPausa():

    pomodoro = input()
    if pomodoro == "p":
        pausar = True
    else:
        pausar = False

while(True):

    threading.Thread(target=isPausa).start()

    while(pausar != True):
        
        timer(tasks_time)
        
        count += 1

        if count%3==0:
            break_time = 15
        else:
            break_time = 5

        os.system('clear')
        print("Estatísticas")
        estatsHora = str(int((count*25)/60))
        if(int(estatsHora)>0):
            estatsMinuto = str(int(count*25)-(int(estatsHora)*60))
        else:
            estatsMinuto = str(int(count*25))
        print("Tempo de estudo = "+estatsHora+":"+estatsMinuto)
        timer(break_time)

os.system('clear')