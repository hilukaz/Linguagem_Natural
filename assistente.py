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
        frase = microfone.recognize_google(audio,language='jp')

        # if "navegador" in frase:
        #     os.system("start Chrome.exe")
        #     return False

        if "fechar" in frase:
            os.system("exit")
            return True
        
        elif "não entendi" in frase:
            ### REQUISIÇÃO COM SCRIPT 'me explique o que foi dito por você na frase anterior' ###
            return True

        elif "o que é" in frase:
            ### REQUISIÇÃO COM SCRIPT 'o que é {palavra}' ###
            return True
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)

        ### NESSE MOMENTO TERIA ALGUMA REQUISIÇÃO COM UM SCRIPT JÁ PRONTO NO CHATGPT PARA DAR CONTINUIDADE A CONVERSAÇÃO COM A LINGUA QUE ESTÁ PRATICANDO###
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

while True:
    if ouvir_microfone():
        break