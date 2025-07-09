#Imports
import time

# Variaveis
nome = "Programador Python"
idade = "18"
peso = "41"

print("A seguir mostraremos as seguintes informações sobre você, encontrada nas nossas variáveis DEFINIDAS:")

print("Carregando dados...")
for i in range(101):
    print(f"\rCarregando: {i}%", end="", flush=True)
    time.sleep(0.01)
    
print()
time.sleep(0.3)
print("Entrando na váriavel NOME")
time.sleep(0.2)
print("Pegando dados..")
time.sleep(0.2)
print("Enviando payload..")
time.sleep(0.2)
print("Seu nome:", nome)
time.sleep(2)
print("Entrando na váriavel IDADE")
time.sleep(0.2)
print("Pegando dados..")
time.sleep(0.2)
print("Enviando payload..")
time.sleep(2.0)
print("Sua idade:", idade)
time.sleep(1)
print("Entrando na váriavel PESO")
time.sleep(0.2)
print("Pegando dados..")
time.sleep(0.2)
print("Enviando payload..")
time.sleep(2.0)
print("Seu peso:", peso)

