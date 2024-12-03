import time
import json

class Quiz:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.pontuacao = 0
        self.recordes = self.carregar_recordes()  # Carregar os recordes ao iniciar

    def carregar_recordes(self):
        try:
            with open("recordes.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_recordes(self):
        with open("recordes.json", "w") as f:
            json.dump(self.recordes, f, indent=4)

    def jogar(self):
        nome = input("Digite seu nome: ")
        print("\n🎮 Bem-vindo ao Quiz de League of Legends\n")

        # Começar a contagem do tempo
        inicio_tempo = time.time()

        for idx, pergunta in enumerate(self.perguntas, start=1):
            print(f"Pergunta {idx}: {pergunta.enunciado}")
            print("a)", pergunta.opcoes[0])
            print("b)", pergunta.opcoes[1])
            print("c)", pergunta.opcoes[2])
            print("d)", pergunta.opcoes[3])

            resposta = input("Escolha uma alternativa (a, b, c ou d): ").lower()
            if resposta == pergunta.resposta_correta:
                print("✔️ Resposta correta!\n")
                self.pontuacao += 1
            else:
                print(f"❌ Resposta incorreta. A resposta correta era: {pergunta.resposta_correta}\n")

        # Calcular o tempo total de jogo
        tempo_total = time.time() - inicio_tempo
        self.exibir_resultado(nome, tempo_total)

        # Adicionar o recorde
        self.adicionar_recorde(nome, self.pontuacao, tempo_total)

    def exibir_resultado(self, nome, tempo_total):
        print("\n=== RESULTADO ===")
        print(f"Jogador: {nome}")
        print(f"Você acertou {self.pontuacao}/{len(self.perguntas)} perguntas.")
        if self.pontuacao == 0:
            print("🥉 Classificação: Ferro")
        elif self.pontuacao == 1:
            print("🥉 Classificação: Bronze")
        elif self.pontuacao == 2:
            print("🥈 Classificação: Prata")
        elif self.pontuacao == 3:
            print("🥇 Classificação: Ouro")
        elif self.pontuacao == 4:
            print("🏆 Classificação: Platina")
        elif self.pontuacao == 5:
            print("🌟 Classificação: Esmeralda")
        print(f"Tempo: {tempo_total:.2f} segundos\n")
        print("Obrigado por jogar!")

    def adicionar_recorde(self, nome, pontuacao, tempo):
        self.recordes.append({"nome": nome, "pontuacao": pontuacao, "tempo": tempo})
        self.salvar_recordes()  # Salvar os recordes sempre que adicionar um novo

    def exibir_recordes(self):
        print("\n=== RECORDES ===")
        if not self.recordes:
            print("Ainda não há recordes.")
        else:
            # Ordenar os recordes pela pontuação e tempo
            self.recordes.sort(key=lambda x: (-x["pontuacao"], x["tempo"]))
            for idx, recorde in enumerate(self.recordes, start=1):
                print(f"{idx}. {recorde['nome']} - {recorde['pontuacao']} pontos - {recorde['tempo']:.2f} segundos")
