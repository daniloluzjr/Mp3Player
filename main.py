import os
import pygame

# Função para carregar músicas em uma pasta específica
def carregar_musica(pasta):
    lista_musicas = os.listdir(pasta)
    lista_musicas = [os.path.join(pasta, musica) for musica in lista_musicas if musica.endswith('.mp3')]
    return lista_musicas

# Função principal para reproduzir música
def reproduzir_musica(musicas, indice):
    pygame.mixer.init()
    pygame.mixer.music.load(musicas[indice])
    pygame.mixer.music.play()

# Pasta onde estão as músicas (altere para o seu diretório)
pasta_musicas = 'D:\Backup Files\MUSICAS - CLIPES\MP3 - GERAL\80s'

# Carregar músicas
lista_de_musicas = carregar_musica(pasta_musicas)
indice_musica_atual = 0

# Reproduzir a primeira música da lista
reproduzir_musica(lista_de_musicas, indice_musica_atual)

# Loop para manter o programa em execução e lidar com comandos
rodando = True
while rodando:
    comando = input("Digite 'play', 'pause', 'next' ou 'previous': ")

    if comando == 'play':
        if not pygame.mixer.music.get_busy():
            reproduzir_musica(lista_de_musicas, indice_musica_atual)
    elif comando == 'pause':
        pygame.mixer.music.pause()
    elif comando == 'stop':
        pygame.mixer.music.stop()
        break  # Sai do loop e encerra o programa
    elif comando == 'next':
        indice_musica_atual = (indice_musica_atual + 1) % len(lista_de_musicas)
        pygame.mixer.music.stop()
        reproduzir_musica(lista_de_musicas, indice_musica_atual)
    elif comando == 'previous':
        indice_musica_atual = (indice_musica_atual - 1) % len(lista_de_musicas)
        pygame.mixer.music.stop()
        reproduzir_musica(lista_de_musicas, indice_musica_atual)
    else:
        print("Comando inválido")

# Parar a reprodução e encerrar o mixer quando sair do loop
pygame.mixer.music.stop()
pygame.mixer.quit()
