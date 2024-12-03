import random


class Pergunta:
    def __init__(self, enunciado, opcoes, resposta_correta):
        self.enunciado = enunciado
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta

    def exibir_pergunta(self):
        print(self.enunciado)
        for i, opcao in enumerate(self.opcoes, start=1):
            print(f"{chr(96 + i)}) {opcao}")

    def verificar_resposta(self, resposta):
        return resposta.lower() == self.resposta_correta.lower()