import time
from pynput.keyboard import Controller, Key


TEMPO_ENTRE_NUMEROS = 0.5  
ESPERA_INICIAL = 3          


numeros = [
    "ZERO !", "UM !", "DOIS !", "TRÊS !", "QUATRO !", "CINCO !", "SEIS !", "SETE !", "OITO !", "NOVE !", "DEZ !",
    "ONZE !", "DOZE !", "TREZE !", "QUATORZE !", "QUINZE !", "DEZESSEIS !", "DEZESSETE !", "DEZOITO !", "DEZENOVE !", "VINTE !",
    "VINTE E UM !", "VINTE E DOIS !", "VINTE E TRÊS !", "VINTE E QUATRO !", "VINTE E CINCO !", "VINTE E SEIS !", "VINTE E SETE !", "VINTE E OITO !", "VINTE E NOVE !", "TRINTA !",
    "TRINTA E UM !", "TRINTA E DOIS !", "TRINTA E TRÊS !", "TRINTA E QUATRO !", "TRINTA E CINCO !", "TRINTA E SEIS !", "TRINTA E SETE !", "TRINTA E OITO !", "TRINTA E NOVE !", "QUARENTA !",
    "QUARENTA E UM !", "QUARENTA E DOIS !", "QUARENTA E TRÊS !", "QUARENTA E QUATRO !", "QUARENTA E CINCO !", "QUARENTA E SEIS !", "QUARENTA E SETE !", "QUARENTA E OITO !", "QUARENTA E NOVE !", "CINQUENTA !",
    "CINQUENTA E UM !", "CINQUENTA E DOIS !", "CINQUENTA E TRÊS !", "CINQUENTA E QUATRO !", "CINQUENTA E CINCO !", "CINQUENTA E SEIS !", "CINQUENTA E SETE !", "CINQUENTA E OITO !", "CINQUENTA E NOVE !", "SESSENTA !",
    "SESSENTA E UM !", "SESSENTA E DOIS !", "SESSENTA E TRÊS !", "SESSENTA E QUATRO !", "SESSENTA E CINCO !", "SESSENTA E SEIS !", "SESSENTA E SETE !", "SESSENTA E OITO !", "SESSENTA E NOVE !", "SETENTA !",
    "SETENTA E UM !", "SETENTA E DOIS !", "SETENTA E TRÊS !", "SETENTA E QUATRO !", "SETENTA E CINCO !", "SETENTA E SEIS !", "SETENTA E SETE !", "SETENTA E OITO !", "SETENTA E NOVE !", "OITENTA !",
    "OITENTA E UM !", "OITENTA E DOIS !", "OITENTA E TRÊS !", "OITENTA E QUATRO !", "OITENTA E CINCO !", "OITENTA E SEIS !", "OITENTA E SETE !", "OITENTA E OITO !", "OITENTA E NOVE !", "NOVENTA !",
    "NOVENTA E UM !", "NOVENTA E DOIS !", "NOVENTA E TRÊS !", "NOVENTA E QUATRO !", "NOVENTA E CINCO !", "NOVENTA E SEIS !", "NOVENTA E SETE !", "NOVENTA E OITO !", "NOVENTA E NOVE !", "CEM !",
    "CENTO E UM !", "CENTO E DOIS !", "CENTO E TRÊS !", "CENTO E QUATRO !", "CENTO E CINCO !", "CENTO E SEIS !", "CENTO E SETE !", "CENTO E OITO !", "CENTO E NOVE !", "CENTO E DEZ !",
    "CENTO E ONZE !", "CENTO E DOZE !", "CENTO E TREZE !", "CENTO E QUATORZE !", "CENTO E QUINZE !", "CENTO E DEZESSEIS !", "CENTO E DEZESSETE !", "CENTO E DEZOITO !", "CENTO E DEZENOVE !", "CENTO E VINTE !",
    "CENTO E VINTE E UM !", "CENTO E VINTE E DOIS !", "CENTO E VINTE E TRÊS !", "CENTO E VINTE E QUATRO !", "CENTO E VINTE E CINCO !", "CENTO E VINTE E SEIS !", "CENTO E VINTE E SETE !", "CENTO E VINTE E OITO !", "CENTO E VINTE E NOVE !", "CENTO E TRINTA !",
    "CENTO E TRINTA E UM !", "CENTO E TRINTA E DOIS !", "CENTO E TRINTA E TRÊS !", "CENTO E TRINTA E QUATRO !", "CENTO E TRINTA E CINCO !", "CENTO E TRINTA E SEIS !", "CENTO E TRINTA E SETE !", "CENTO E TRINTA E OITO !", "CENTO E TRINTA E NOVE !", "CENTO E QUARENTA !",
    "CENTO E QUARENTA E UM !", "CENTO E QUARENTA E DOIS !", "CENTO E QUARENTA E TRÊS !", "CENTO E QUARENTA E QUATRO !", "CENTO E QUARENTA E CINCO !", "CENTO E QUARENTA E SEIS !", "CENTO E QUARENTA E SETE !", "CENTO E QUARENTA E OITO !", "CENTO E QUARENTA E NOVE !", "CENTO E CINQUENTA !",
    "CENTO E CINQUENTA E UM !", "CENTO E CINQUENTA E DOIS !", "CENTO E CINQUENTA E TRÊS !", "CENTO E CINQUENTA E QUATRO !", "CENTO E CINQUENTA E CINCO !", "CENTO E CINQUENTA E SEIS !", "CENTO E CINQUENTA E SETE !", "CENTO E CINQUENTA E OITO !", "CENTO E CINQUENTA E NOVE !", "CENTO E SESSENTA !",
    "CENTO E SESSENTA E UM !", "CENTO E SESSENTA E DOIS !", "CENTO E SESSENTA E TRÊS !", "CENTO E SESSENTA E QUATRO !", "CENTO E SESSENTA E CINCO !", "CENTO E SESSENTA E SEIS !", "CENTO E SESSENTA E SETE !", "CENTO E SESSENTA E OITO !", "CENTO E SESSENTA E NOVE !", "CENTO E SETENTA !",
    "CENTO E SETENTA E UM !", "CENTO E SETENTA E DOIS !", "CENTO E SETENTA E TRÊS !", "CENTO E SETENTA E QUATRO !", "CENTO E SETENTA E CINCO !", "CENTO E SETENTA E SEIS !", "CENTO E SETENTA E SETE !", "CENTO E SETENTA E OITO !", "CENTO E SETENTA E NOVE !", "CENTO E OITENTA !",
    "CENTO E OITENTA E UM !", "CENTO E OITENTA E DOIS !", "CENTO E OITENTA E TRÊS !", "CENTO E OITENTA E QUATRO !", "CENTO E OITENTA E CINCO !", "CENTO E OITENTA E SEIS !", "CENTO E OITENTA E SETE !", "CENTO E OITENTA E OITO !", "CENTO E OITENTA E NOVE !", "CENTO E NOVENTA !",
    "CENTO E NOVENTA E UM !", "CENTO E NOVENTA E DOIS !", "CENTO E NOVENTA E TRÊS !", "CENTO E NOVENTA E QUATRO !", "CENTO E NOVENTA E CINCO !", "CENTO E NOVENTA E SEIS !", "CENTO E NOVENTA E SETE !", "CENTO E NOVENTA E OITO !", "CENTO E NOVENTA E NOVE !", "DUZENTOS !",
    "DUZENTOS E UM !", "DUZENTOS E DOIS !", "DUZENTOS E TRÊS !", "DUZENTOS E QUATRO !", "DUZENTOS E CINCO !", "DUZENTOS E SEIS !", "DUZENTOS E SETE !", "DUZENTOS E OITO !", "DUZENTOS E NOVE !", "DUZENTOS E DEZ !",
    "QUATROCENTOS E NOVENTA E NOVE !", "QUINHENTOS !"
]

keyboard = Controller()

def abrir_chat():
    """Abre o chat do Roblox"""
    keyboard.press(';')
    time.sleep(0.1)
    keyboard.release(';')
    time.sleep(0.5)

def enviar_mensagem(texto):
    """Digita e envia a mensagem"""
    keyboard.type(texto)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

print("===== AUTOMAÇÃO ROBLOX - NÚMEROS (0-500) =====")

while True:
    try:
        numero_final = int(input("Até qual número enviar? (0 a 500): "))
        if 0 <= numero_final <= 500:
            break
        print("Digite um número entre 0 e 500!")
    except:
        print("Número inválido!")

print(f"\nEnviando de ZERO ! até {numeros[numero_final]}")
print(f"Começando em {ESPERA_INICIAL} segundos... (foco no Roblox)")
time.sleep(ESPERA_INICIAL)

try:
    for i in range(numero_final + 1):
        print(f"Enviando: {numeros[i]}")
        abrir_chat()
        enviar_mensagem(numeros[i])
        if i < numero_final:
            time.sleep(TEMPO_ENTRE_NUMEROS)
    print("✅ Concluído!")
except KeyboardInterrupt:
    print("❌ Interrompido pelo usuário!")