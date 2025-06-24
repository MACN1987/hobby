
import tkinter as tk
from tkinter import messagebox
import random
import winsound

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.jogador = "X"
        self.ia = "O"
        self.vitorias_jogador = 0
        self.vitorias_ia = 0
        self.empates = 0
        self.vitorias_jogador1 = 0
        self.vitorias_jogador2 = 0
        self.empates_2jog = 0
        self.dificuldade = "1"
        self.modo_vs_ia = True

        self.tela_inicial()

    def tela_inicial(self):
        self.frame_inicio = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_inicio.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame_inicio, text="JOGO DA VELHA", font=("Comic Sans MS", 24, "bold"), fg="blue", bg="#f0f0f0").pack(pady=20)

        tk.Button(self.frame_inicio, text="1 Jogador (vs IA)", font=("Arial", 14), command=self.selecionar_dificuldade).pack(pady=10)
        tk.Button(self.frame_inicio, text="2 Jogadores", font=("Arial", 14), command=self.iniciar_jogo_vs_jogador).pack(pady=10)

    def selecionar_dificuldade(self):
        self.frame_inicio.destroy()
        self.frame_dificuldade = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_dificuldade.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.frame_dificuldade, text="Escolha a dificuldade da IA", font=("Comic Sans MS", 16, "bold"), bg="#f0f0f0").pack(pady=15)
        tk.Button(self.frame_dificuldade, text="Fácil", font=("Arial", 9, "bold"), width=15, height=2, command=lambda: self.iniciar_jogo("1")).pack(pady=5)
        tk.Button(self.frame_dificuldade, text="Médio", font=("Arial", 9, "bold"), width=15, height=2, command=lambda: self.iniciar_jogo("2")).pack(pady=5)
        tk.Button(self.frame_dificuldade, text="Difícil", font=("Arial", 9, "bold"), width=15, height=2, command=lambda: self.iniciar_jogo("3")).pack(pady=5)

    def iniciar_jogo_vs_jogador(self):
        self.modo_vs_ia = False
        self.iniciar_jogo(None)

    def iniciar_jogo(self, dificuldade):
        if dificuldade:
            self.dificuldade = dificuldade
        if hasattr(self, 'frame_inicio'):
            self.frame_inicio.destroy()
        if hasattr(self, 'frame_dificuldade'):
            self.frame_dificuldade.destroy()

        self.tabuleiro = [" " for _ in range(9)]
        self.botoes = []

        self.frame_placar = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_placar.pack(pady=10)

        self.placar_label = tk.Label(self.frame_placar, text=self.obter_placar(), font=("Arial", 12), bg="#f0f0f0")
        self.placar_label.pack()

        self.frame_tabuleiro = tk.Frame(self.root)
        self.frame_tabuleiro.pack()

        for i in range(9):
            btn = tk.Button(self.frame_tabuleiro, text="", width=5, height=2, font=("Arial", 24), bg="lightyellow",
                            command=lambda i=i: self.clique(i))
            btn.grid(row=i // 3, column=i % 3)
            self.botoes.append(btn)

        if self.modo_vs_ia:
            self.jogador_atual = random.choice([self.jogador, self.ia])
            if self.jogador_atual == self.ia:
                self.root.after(500, self.jogada_ia)
        else:
            self.jogador_atual = random.choice(["X", "O"])

    def obter_placar(self):
        if self.modo_vs_ia:
            return f"Você: {self.vitorias_jogador}  |  IA: {self.vitorias_ia}  |  Empates: {self.empates}"
        else:
            return f"Jogador X: {self.vitorias_jogador1}  |  Jogador O: {self.vitorias_jogador2}  |  Empates: {self.empates_2jog}"

    def clique(self, i):
        if self.tabuleiro[i] == " ":
            self.tocar_som()
            self.botoes[i]["text"] = self.jogador_atual
            self.botoes[i]["bg"] = "lightblue" if self.jogador_atual == "X" else "salmon"
            self.tabuleiro[i] = self.jogador_atual
            if self.verificar_fim_de_jogo(self.jogador_atual):
                return
            if self.modo_vs_ia:
                self.jogador_atual = self.ia
                self.root.after(500, self.jogada_ia)
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def jogada_ia(self):
        pos = self.definir_jogada_ia()
        self.tocar_som()
        self.botoes[pos]["text"] = self.ia
        self.botoes[pos]["bg"] = "salmon"
        self.tabuleiro[pos] = self.ia
        if self.verificar_fim_de_jogo(self.ia):
            return
        self.jogador_atual = self.jogador

    def definir_jogada_ia(self):
        if self.dificuldade == "3":
            for i in range(9):
                if self.tabuleiro[i] == " ":
                    self.tabuleiro[i] = self.ia
                    if self.verificar_vencedor(self.ia):
                        self.tabuleiro[i] = " "
                        return i
                    self.tabuleiro[i] = " "
            for i in range(9):
                if self.tabuleiro[i] == " ":
                    self.tabuleiro[i] = self.jogador
                    if self.verificar_vencedor(self.jogador):
                        self.tabuleiro[i] = " "
                        return i
                    self.tabuleiro[i] = " "
            if self.tabuleiro[4] == " ": return 4
            for i in [0, 2, 6, 8]:
                if self.tabuleiro[i] == " ": return i
            for i in [1, 3, 5, 7]:
                if self.tabuleiro[i] == " ": return i
        elif self.dificuldade == "2":
            for i in range(9):
                if self.tabuleiro[i] == " ":
                    self.tabuleiro[i] = self.ia
                    if self.verificar_vencedor(self.ia):
                        self.tabuleiro[i] = " "
                        return i
                    self.tabuleiro[i] = " "
            for i in range(9):
                if self.tabuleiro[i] == " ":
                    self.tabuleiro[i] = self.jogador
                    if self.verificar_vencedor(self.jogador):
                        self.tabuleiro[i] = " "
                        return i
                    self.tabuleiro[i] = " "
        return random.choice([i for i, v in enumerate(self.tabuleiro) if v == " "])

    def verificar_fim_de_jogo(self, jogador):
        if self.verificar_vencedor(jogador):
            if self.modo_vs_ia:
                if jogador == self.jogador:
                    self.vitorias_jogador += 1
                    self.fim_jogo("Você venceu!")
                else:
                    self.vitorias_ia += 1
                    self.fim_jogo("A IA venceu!")
            else:
                if jogador == "X":
                    self.vitorias_jogador1 += 1
                else:
                    self.vitorias_jogador2 += 1
                self.fim_jogo(f"Jogador {jogador} venceu!")
            return True
        if self.verificar_empate():
            if self.modo_vs_ia:
                self.empates += 1
            else:
                self.empates_2jog += 1
            self.fim_jogo("Empate!")
            return True
        return False

    def verificar_vencedor(self, jogador):
        v = self.tabuleiro
        return any([
            v[0] == v[1] == v[2] == jogador,
            v[3] == v[4] == v[5] == jogador,
            v[6] == v[7] == v[8] == jogador,
            v[0] == v[3] == v[6] == jogador,
            v[1] == v[4] == v[7] == jogador,
            v[2] == v[5] == v[8] == jogador,
            v[0] == v[4] == v[8] == jogador,
            v[2] == v[4] == v[6] == jogador,
        ])

    def verificar_empate(self):
        return " " not in self.tabuleiro

    def fim_jogo(self, mensagem):
        messagebox.showinfo("Fim de Jogo", mensagem)
        self.placar_label.config(text=self.obter_placar())
        self.reiniciar()

    def reiniciar(self):
        for btn in self.botoes:
            btn.destroy()
        self.frame_tabuleiro.destroy()
        self.frame_placar.destroy()
        self.iniciar_jogo(self.dificuldade if self.modo_vs_ia else None)

    def tocar_som(self):
        try:
            winsound.MessageBeep()
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()