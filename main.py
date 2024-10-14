import time
import pygame
from pygame.locals import *
from images import *
import os
# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Carregar sons (verifique os caminhos e formatos)
morte = pygame.mixer.Sound("midia/morte.mp3")  # Altere para .wav
moeda = pygame.mixer.Sound("midia/coin.mp3")  # Altere para .wav
comemoracao = pygame.mixer.Sound("midia/winner.mp3")  # Altere para .wav
os.system("cls")
def main():
    print("Digite uma das opções:")
    print("1 [morte] 2 [moeda] 3 [comemoracao]")
   
    op = input()
    
    match op:
        case "1":
            morte.play()
        case "2":
            moeda.play()
        case "3":
            comemoracao.play()
            winner()
    
    # Aguarde um tempo para permitir que o som seja reproduzido
    time.sleep(2)  # Aguarda 2 segundos

main()

# Finalizando o Pygame
#pygame.quit()