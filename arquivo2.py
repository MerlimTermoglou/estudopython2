import os

os.system("clear")

arq = open("./arquivos/dados.csv","a")
nome = input("digite seu nome:\n")
email = input("digite seu email:\n")

arq.write(nome+" - "+email+"\n")

arq.close