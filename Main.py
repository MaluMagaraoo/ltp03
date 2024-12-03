import random
import time  # Adicione esta linha para importar a biblioteca time
from pergunta import Pergunta
from gerenciador import GerenciadorPerguntas

def obter_classificacao(pontos):
    if pontos == 5:
        return "🌟 Classificação: Esmeralda"
    elif pontos == 4:
        return "🏆 Classificação: Platina"
    elif pontos == 3:
        return "🥇 Classificação: Ouro"
    elif pontos == 2:
        return "🥈 Classificação: Prata"
    elif pontos == 1:
        return "🥉 Classificação: Bronze"
    else:
        return "🥉 Classificação: Ferro"


def main():
    gerenciador = GerenciadorPerguntas()

    while True:
        print("🎮 Bem-vindo ao Quiz de League of Legends")
        print("1 - Jogar")
        print("2 - Recordes")
        print("3 - Adicionar pergunta")
        print("4 - Créditos")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Início do quiz (função de jogar)
            print("\nVamos jogar!\n")
            perguntas_aleatorias = gerenciador.obter_perguntas_aleatorias(5)
            pontos = 0
            tempo_inicial = time.time()

            for pergunta in perguntas_aleatorias:
                print(f"\n{pergunta.enunciado}")
                for i, opcao in enumerate(pergunta.opcoes):
                    print(f"{chr(97 + i)}) {opcao}")
                resposta = input("Digite a letra da resposta: ")

                if resposta.lower() == pergunta.resposta_correta:
                    print("Resposta correta! ✅")
                    pontos += 1
                else:
                    print(f"Resposta incorreta! ❌ A resposta correta era: {pergunta.resposta_correta}")

            tempo_final = time.time()
            tempo_total = tempo_final - tempo_inicial
            print(f"\nVocê fez {pontos} pontos em {tempo_total:.2f} segundos.")


            nome = input("Digite seu nome para salvar o recorde: ")
            classificacao = obter_classificacao(pontos)
            print(f"Classificação: {classificacao}")

            gerenciador.adicionar_recorde(nome, pontos, tempo_total)

        elif opcao == "2":

            print("\n=== RECORDES ===")
            for recorde in gerenciador.recordes:
                print(f"{recorde['nome']}: {recorde['pontos']} pontos, {recorde['tempo']:.2f} segundos")

        elif opcao == "3":

            enunciado = input("Digite o enunciado da pergunta: ")
            opcoes = [
                input("Digite a opção a): "),
                input("Digite a opção b): "),
                input("Digite a opção c): "),
                input("Digite a opção d): ")
            ]
            resposta_correta = input("Digite a letra da resposta correta: ")

            # Passando os parâmetros corretamente
            gerenciador.adicionar_pergunta(enunciado, opcoes, resposta_correta)

        elif opcao == "4":

            print("\n=== CRÉDITOS ===")
            print("Desenvolvido pelas alunas: ")
            print("Fernanda Hiramoto - 22409565\nMaria Luiza - 22408637\nNicolle Kalinne - 22400710")
            print("Obrigada por jogar!❤️")
            print("\n=====================================")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
