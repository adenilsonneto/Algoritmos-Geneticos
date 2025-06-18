import random


def fitness(x):
    return -abs(7 - x)


def gerar_individuo():
    return random.randint(0, 15)


def crossover(pai1, pai2):
    return (pai1 + pai2) // 2

def mutacao(filho):
    if random.random() < 0.3:  
        if random.random() < 0.5:
            filho = max(0, filho - 1)
        else:
            filho = min(15, filho + 1)
    return filho


populacao = [gerar_individuo() for _ in range(4)]
print('População inicial:', populacao)

for geracao in range(5):
    
    populacao.sort(key=fitness, reverse=True)
    pai1, pai2 = populacao[0], populacao[1]

    
    filho1 = mutacao(crossover(pai1, pai2))
    filho2 = mutacao(crossover(pai1, pai2))

 
    
    populacao = [pai1, pai2, filho1, filho2]

    print(f'Geração {geracao + 1}: {populacao} - Melhor: {pai1} (fitness {fitness(pai1)})')


melhor = max(populacao, key=fitness)
print('\nMelhor solução encontrada:', melhor, '-> Fitness:', fitness(melhor))
