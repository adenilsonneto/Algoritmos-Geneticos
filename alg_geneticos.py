import random

# Função fitness: quanto mais próximo de 7, melhor
def fitness(x):
    return -abs(7 - x)

# Gerar um indivíduo aleatório (número de 0 a 15)
def gerar_individuo():
    return random.randint(0, 15)

# Crossover simples: média dos pais arredondada
def crossover(pai1, pai2):
    return (pai1 + pai2) // 2

# Mutação simples: com chance, soma ou subtrai 1
def mutacao(filho):
    if random.random() < 0.3:  # 30% de chance de mutar
        if random.random() < 0.5:
            filho = max(0, filho - 1)
        else:
            filho = min(15, filho + 1)
    return filho

# ---- Algoritmo Genético ----
populacao = [gerar_individuo() for _ in range(4)]
print('População inicial:', populacao)

for geracao in range(5):
    # Avalia fitness e seleciona os dois melhores
    populacao.sort(key=fitness, reverse=True)
    pai1, pai2 = populacao[0], populacao[1]

    # Gera dois filhos
    filho1 = mutacao(crossover(pai1, pai2))
    filho2 = mutacao(crossover(pai1, pai2))

    # Nova população: dois pais + dois filhos
    populacao = [pai1, pai2, filho1, filho2]

    print(f'Geração {geracao + 1}: {populacao} - Melhor: {pai1} (fitness {fitness(pai1)})')

# Resultado final
melhor = max(populacao, key=fitness)
print('\nMelhor solução encontrada:', melhor, '-> Fitness:', fitness(melhor))
