from datetime import datetime
import os
import random

from colorama import init, Fore, Style
init(autoreset=True)

def criar_tabuleiro():
    return [' ' for _ in range(9)]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabuleiro(tabuleiro):
    print()
    for i in range(0, 9, 3):
        linha = []
        for j in range(i, i+3):
            valor = tabuleiro[j]
            if valor == 'X':
                cor = Fore.BLUE + 'X' + Style.RESET_ALL
            elif valor == 'O':
                cor = Fore.RED + 'O' + Style.RESET_ALL
            else:
                numero = str(j+1)
                if (j+1) % 2 == 0:
                    cor = Fore.GREEN + numero + Style.RESET_ALL
                else:
                    cor = Fore.YELLOW + numero + Style.RESET_ALL
            linha.append(cor)
        print(" " + " | ".join(linha))
        if i < 6:
            print("---+---+---")
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
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for linha in combinacoes_vitoria:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def jogada_ia(tabuleiro, jogador_ia='O', jogador_usuario='X', nivel='1'):
    if nivel == '1':
        posicoes_disponiveis = [i for i in range(9) if tabuleiro[i] == ' ']
        return random.choice(posicoes_disponiveis)

    def pode_vencer(jogador):
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = jogador
                if verificar_vencedor(tabuleiro, jogador):
                    tabuleiro[i] = ' '
                    return i
                tabuleiro[i] = ' '
        return None

    pos = pode_vencer(jogador_ia)
    if pos is not None:
        return pos

    pos = pode_vencer(jogador_usuario)
    if pos is not None:
        return pos

    if nivel == '3':
        if tabuleiro[4] == ' ':
            return 4
        cantos = [i for i in [0, 2, 6, 8] if tabuleiro[i] == ' ']
        if cantos:
            return random.choice(cantos)

    posicoes_disponiveis = [i for i in range(9) if tabuleiro[i] == ' ']
    return random.choice(posicoes_disponiveis)

if __name__ == '__main__':
    vitorias_jogador = 0
    vitorias_ia = 0
    empates = 0
    while True:
        limpar_tela()
        print(f"{Fore.BLUE}Placar:{Style.RESET_ALL} Jogador: {vitorias_jogador}  |  IA: {vitorias_ia}  |  Empates: {empates}")
        print()

        print("Bem-vindo ao Jogo da Velha!")
        print("Escolha o modo de jogo:")
        print("1 - Jogar contra outra pessoa")
        print("2 - Jogar contra a IA")
        print("3 - Sair")

        modo = input("Digite 1, 2 ou 3: ")
        while modo not in ['1', '2', '3']:
            modo = input("Opção inválida. Digite 1, 2 ou 3: ")

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
                        print(Fore.GREEN + f"Parabéns, Jogador {jogador_atual}, você foi o vencedor!" + Style.RESET_ALL)
                        input("Pressione Enter para voltar ao menu...")
                        break
                    if verificar_empate(tabuleiro):
                        exibir_tabuleiro(tabuleiro)
                        print(Fore.CYAN + "Houve um empate!" + Style.RESET_ALL)
                        input("Pressione Enter para voltar ao menu...")
                        break

                    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

                except ValueError:
                    print("Por favor, digite um número válido entre 1 e 9.")

        elif modo == "2":
            print("Escolha a dificuldade da IA:")
            print("1 - Fácil (aleatória)")
            print("2 - Média (bloqueia jogador)")
            print("3 - Difícil (inteligente)")
            nivel = input("Digite 1, 2 ou 3: ")
            while nivel not in ['1', '2', '3']:
                nivel = input("Opção inválida. Digite 1, 2 ou 3: ")

            tabuleiro = criar_tabuleiro()
            jogador_usuario = 'X'
            jogador_ia = 'O'
            jogador_atual = random.choice([jogador_usuario, jogador_ia])
            if jogador_atual == jogador_usuario:
                print(Fore.YELLOW + "Você começa jogando!" + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "A IA começa jogando!" + Style.RESET_ALL)
            #jogador_atual = jogador_usuario

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
                    pos = jogada_ia(tabuleiro, jogador_ia, jogador_usuario, nivel)
                    fazer_jogada(tabuleiro, pos, jogador_ia)

                if verificar_vencedor(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    if jogador_atual == jogador_usuario:
                        print(Fore.GREEN + "Parabéns! Você venceu a IA!" + Style.RESET_ALL)
                        vitorias_jogador += 1
                    else:
                        print(Fore.RED + "A IA venceu. Tente novamente!" + Style.RESET_ALL)
                        vitorias_ia += 1
                    input("Pressione Enter para voltar ao menu...")
                    break

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print(Fore.CYAN + "Empate!" + Style.RESET_ALL)
                    empates += 1 
                    input("Pressione Enter para voltar ao menu...")
                    break

                jogador_atual = jogador_ia if jogador_atual == jogador_usuario else jogador_usuario
