
import random

def escolher_palavras():
    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]
    return random.choice(palavras)
        #palavras = [linha.strip() for linha in arquivo]

def mostrar_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    return estagios[min(tentativas, len(estagios)-1)]
def jogar_forca():
    palavra = escolher_palavras()
    letras_descobertas = ['_' if letra.isalpha() else letra for letra in palavra]
    letras_erradas = []
    tentativas = 6
    
    print("Sejam bem-vindos ao Jogo da Forca!!!")
    print(f'Você tem {tentativas} tentativas para adivinhar a palavra. \n Boa sorte!')
    
    while tentativas > 0 and '_' in letras_descobertas:
        print (mostrar_forca(len(letras_erradas)))
        print("Palavra:", ' '.join(letras_descobertas))
        print("Letras erradas:", ' '.join(letras_erradas))
        print(f'Tentativas restantes: {tentativas}')
        tentativa = input ('Digite uma letra: ').upper()

        if not tentativa.isalpha() or len (tentativa) != 1:
            print("Digite apenas uma Letra!")
            continue
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("Você já tentou essa Letra!!")
            continue
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_descobertas[i] = tentativa
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1

    if '_' not in letras_descobertas:
        print(f'Parabens! Você acertou a palavra: {palavra}')

    else: 
        print(mostrar_forca(len(letras_erradas)))
        print (f'Você perdeu! A palavra era:  {palavra}')

if __name__=="__main__":
     while True:
        jogar_forca()
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

   



