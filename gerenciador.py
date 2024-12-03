import random
import json
from pergunta import Pergunta

class GerenciadorPerguntas:
    def __init__(self):
        self.perguntas = []
        self.recordes = []
        self.carregar_perguntas()

    def carregar_perguntas(self):
        """Carregar as perguntas de um arquivo JSON, caso exista."""
        try:
            with open("perguntas.json", "r") as f:
                perguntas_salvas = json.load(f)
                self.perguntas = [Pergunta(**p) for p in perguntas_salvas]
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou estiver vazio, carrega perguntas iniciais
            self.carregar_perguntas_iniciais()

    def carregar_perguntas_iniciais(self):
        """Carregar perguntas iniciais para o quiz."""
        self.perguntas.extend([
            Pergunta("Qual desses nunca foi um mapa em League Of Legends:",
                     ["Summoner's Rift", "Aeon of Strife", "Howling Abyss", "Twisted Treeline"], "b"),
            Pergunta("Qual campeão nunca apareceu em Arcane (primeira e segunda temporada)?",
                     ["Singed", "Warwick", "Orianna", "Blitzcrank"], "d"),
            Pergunta("Qual não é uma região do League of Legends:",
                     ["Icebox", "Vazio", "Demacia", "Ionia"], "a"),
            Pergunta("Qual está na ordem incorreta dos elos (season 2024):",
                     ["Platina -> Diamante -> Esmeralda", "Ferro -> Bronze -> Prata",
                      "Bronze -> Prata -> Ouro", "Ouro -> Platina -> Esmeralda"], "a"),
            Pergunta("Qual campeão não é comumente usado na selva:",
                     ["Evelynn", "Shaco", "Thresh", "Elise"], "c"),
            Pergunta("Qual time foi o campeão do Mundial de League of Legends 2024:",
                     ["LOUD", "FNATIC", "PAIN", "SKTT1"], "d"),
            Pergunta("Qual desses campeões não são de Ionia:",
                     ["Akali e Shen", "Yasuo e Fiora", "Irelia e Ahri", "Karma e Zed"], "b"),
            Pergunta("Qual alternativa os campeões não possuem um parentesco:",
                     ["Rakan e Xayah", "Kaisa e Kassadin", "Jinx e Vi", "Talon e Katarina"], "a"),
            Pergunta("Qual desses não é um elemento presente na skin da Lux Elementalista:",
                     ["Fogo e Magma", "Natureza e Mística", "Terra e Escuridão", "Ar e Tempestade"], "c"),
            Pergunta("Qual alternativa não é considerada uma banda em League of Legends:",
                     ["HeartSteel", "Pentakill", "Psyops", "True Damage"], "c"),
            Pergunta("De acordo com o Ex-proplayer Yoda, quem não sabe jogar de Katarina?",
                     ["Dynquedo", "Tinowns", "Brtt", "Kami"], "d"),
            Pergunta("Qual alternativa contém os dois campeões que já sofreram Rework completo (visual e habilidade)?",
                     ["Urgot e Jinx", "Aatrox e Poppy", "Evelynn e Leona", "Tryndamere e Mordekaiser"], "b"),
            Pergunta("Em que ano o League of Legends surgiu com um servidor BR?",
                     ["2012", "2011", "2010", "2009"], "a"),
            Pergunta("Na cinematic AWAKEN de 2020, qual alternativa contém o campeão que não participa da Cinematic:",
                     ["Darius e Draven", "Sylas e Galio", "Ezreal e Lux", "Karma e Kennen"], "a"),
            Pergunta("A habilidade chamada “Centelha Final” pertence a qual campeão?",
                     ["Darius", "Lux", "Urgot", "Briar"], "b"),
            Pergunta("Qual das opções não é um tipo de dragão?",
                     ["Ar", "Montanha", "Água", "Fogo"], "a"),
            Pergunta("Qual campeão foi lançado em 2024?",
                     ["Briar", "Hwei", "Smolder", "Naafiri"], "c"),
            Pergunta("Qual alternativa contém o campeão existente no LoL desde o seu lançamento?",
                     ["Vayne", "Leona", "Lux", "Janna"], "d"),
            Pergunta("Qual alternativa o campeão não é de Bandópolis?",
                     ["Fizz", "Lulu", "Veigar", "Rumble"], "a"),
            Pergunta("Qual campeão não é considerado um Darkin?",
                     ["Naafiri", "Darius", "Aatrox", "Varus"], "b"),
        ])

    def salvar_perguntas(self):
        """Salvar as perguntas no arquivo JSON."""
        with open("perguntas.json", "w") as f:
            json.dump([p.__dict__ for p in self.perguntas], f, indent=4)

    def adicionar_pergunta(self, enunciado, opcoes, resposta_correta):
        """Adicionar uma nova pergunta e salvar no arquivo JSON."""
        nova_pergunta = Pergunta(enunciado, opcoes, resposta_correta)
        self.perguntas.append(nova_pergunta)
        self.salvar_perguntas()
        print("Pergunta adicionada com sucesso!")

    def adicionar_recorde(self, nome, pontos, tempo):
        self.recordes.append({"nome": nome, "pontos": pontos, "tempo": tempo})

    def obter_perguntas_aleatorias(self, quantidade):
        """Obter perguntas aleatórias para o quiz."""
        return random.sample(self.perguntas, quantidade)
