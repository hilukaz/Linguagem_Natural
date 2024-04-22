print("testando")

import speech_recognition as sr

import os


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False

        if "Excel" in frase:
            os.system("start Excel.exe")
            return False

        if "Word" in frase:
            os.system("start WINWORD.exe")
            return False

        if "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False
        
        elif "fechar" in frase:
            os.system("exit")
            return True
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

while True:
    if ouvir_microfone():
        break