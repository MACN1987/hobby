# jogo_velha.py
from datetime import datetime
import os
import random

def criar_tabuleiro():
    return [' ' for _ in range(9)]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabuleiro(tabuleiro):
    print()
    print(f' {tabuleiro[0]}   | {tabuleiro[1]}   | {tabuleiro[2]} ')
    print('-----+-----+-----')
    print(f' {tabuleiro[3]}   | {tabuleiro[4]}   | {tabuleiro[5]} ')
    print('-----+-----+-----')
    print(f' {tabuleiro[6]}   | {tabuleiro[7]}   | {tabuleiro[8]} ')
    print()

def jogada_valida(tabuleiro, posicao):
    return tabuleiro[posicao] == ' '

def fazer_jogada(tabuleiro, posicao, jogador):
    if jogada_valida(tabuleiro, posicao):
        tabuleiro[posicao] = jogador
        return True
    return False

def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vitoria = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]
    for linha in combinacoes_vitoria:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def jogada_ia(tabuleiro):
    posicoes_disponiveis = [i for i in range(9) if tabuleiro[i] == ' ']
    return random.choice(posicoes_disponiveis)

if __name__ == '__main__':
    while True:
        limpar_tela()
        print("Bem-vindo ao Jogo da Velha!")
        print("Escolha o modo de jogo:")
        print("1- Jogar contra outra pessoa\n2- Jogar contra a IA\n3- Sair")

        modo = input("Digite 1, 2 ou 3: ")
        while modo not in ['1', '2', '3']:
            modo = input("Opção inválida. Digite 1, 2, ou 3: ")

        if modo == '3':
            hora = datetime.now().hour
            if 5 <= hora < 12:
                saudacao = "Bom Dia!"
            elif 12 <= hora < 18:
                saudacao = "Boa Tarde!"
            elif 18 <= hora < 24:
                saudacao = "Boa Noite!"
            else:
                saudacao = "Boa Madrugada!"
            print(f"{saudacao} Obrigado por Jogar! Até a próxima amigo(a)!")
            break

        if modo == "1":
            tabuleiro = criar_tabuleiro()
            jogador_atual = 'X'
            while True:
                exibir_tabuleiro(tabuleiro)
                try:
                    pos = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
                    if pos < 0 or pos > 8:
                        print("Posição inválida. Escolha um número entre 1 e 9.")
                        continue
                    if not fazer_jogada(tabuleiro, pos, jogador_atual):
                        print("Posição ocupada. Tente novamente.")
                        continue

                    if verificar_vencedor(tabuleiro, jogador_atual):
                        exibir_tabuleiro(tabuleiro)
                        print(f"Parabéns, Jogador {jogador_atual}, você foi o vencedor!")
                        input("Pressione Enter para voltar ao menu...")
                        break
                    if verificar_empate(tabuleiro):
                        exibir_tabuleiro(tabuleiro)
                        print("Houve um empate!")
                        input("Pressione Enter para voltar ao menu...")
                        break

                    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

                except ValueError:
                    print("Por favor, digite um número válido entre 1 e 9.")

        elif modo == "2":
            tabuleiro = criar_tabuleiro()
            jogador_usuario = 'X'
            jogador_ia = 'O'
            jogador_atual = jogador_usuario

            while True:
                exibir_tabuleiro(tabuleiro)

                if jogador_atual == jogador_usuario:
                    try:
                        pos = int(input(f"Sua vez, jogador {jogador_usuario} (1-9): ")) - 1
                        if pos < 0 or pos > 8:
                            print("Posição inválida. Escolha de 1 a 9.")
                            continue
                        if not fazer_jogada(tabuleiro, pos, jogador_usuario):
                            print("Posição ocupada. Tente novamente.")
                            continue
                    except ValueError:
                        print("Entrada inválida. Digite um número entre 1 e 9.")
                        
                else:
                    print("Vez da IA...")
                    pos = jogada_ia(tabuleiro)
                    fazer_jogada(tabuleiro, pos, jogador_ia)

                # Verificar vitória ou empate
                if verificar_vencedor(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    if jogador_atual == jogador_usuario:
                        print("Parabéns! Você venceu a IA!")
                    else:
                        print("A IA venceu. Tente novamente!")
                    input("Pressione Enter para voltar ao menu...")
                    break

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    input("Pressione Enter para voltar ao menu...")
                    break

                
                if jogador_atual == jogador_usuario:
                   jogador_atual = jogador_ia
                else:
                    jogador_atual = jogador_usuario

 
                
                
                




        


        