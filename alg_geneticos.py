import random
import matplotlib.pyplot as plt
import networkx as nx


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


def plotar_grafo(historico):
    G = nx.DiGraph()
    labels = {}
    fitness_vals = {}
    generations = {}

    for geracao, dados in historico.items():
        for individuo, pais in dados:
            node_id = f'{individuo}_G{geracao}'
            labels[node_id] = f'{individuo}\nG{geracao}'
            fitness_vals[node_id] = fitness(individuo)
            generations[node_id] = geracao

            G.add_node(node_id)

            if pais:
                for pai in pais:
                    pai_id = None
                    for ind, _ in historico[geracao - 1]:
                        if ind == pai:
                            pai_id = f'{pai}_G{geracao - 1}'
                            break
                    if pai_id:
                        G.add_edge(pai_id, node_id)

    # Definir layout hierárquico manual
    pos = {}
    layers = {}
    for node, gen in generations.items():
        if gen not in layers:
            layers[gen] = []
        layers[gen].append(node)

    # Distribuir os nós na horizontal por geração
    max_len = max(len(nodes) for nodes in layers.values())

    for gen, nodes in layers.items():
        n = len(nodes)
        x_spacing = 1.5
        x_positions = [
            (i - (n - 1) / 2) * x_spacing
            for i in range(n)
        ]
        for i, node in enumerate(nodes):
            pos[node] = (x_positions[i], -gen)  # y negativo para geração descer

    # Cores e tamanhos
    max_fit = max(fitness_vals.values())
    min_fit = min(fitness_vals.values())

    colors = []
    sizes = []
    for node in G.nodes():
        fit = fitness_vals[node]
        norm = (fit - min_fit) / (max_fit - min_fit + 0.01)
        colors.append((1 - norm, norm, 0))
        sizes.append(1000 + norm * 2000)

    plt.figure(figsize=(14, 8))
    nx.draw(
        G, pos,
        labels=labels,
        with_labels=True,
        node_color=colors,
        node_size=sizes,
        font_size=9,
        edge_color='gray',
        arrows=True
    )
    plt.title('Árvore Genealógica do Algoritmo Genético (Layout Organizado)', fontsize=14)
    plt.show()


# =====================
# Execução do Algoritmo
# =====================

populacao = [gerar_individuo() for _ in range(4)]
print('População inicial:', populacao)

historico = {0: [(ind, None) for ind in populacao]}

for geracao in range(1, 6):
    populacao.sort(key=fitness, reverse=True)
    pai1, pai2 = populacao[0], populacao[1]

    filho1 = mutacao(crossover(pai1, pai2))
    filho2 = mutacao(crossover(pai1, pai2))

    populacao = [pai1, pai2, filho1, filho2]

    historico[geracao] = [
        (pai1, None),
        (pai2, None),
        (filho1, (pai1, pai2)),
        (filho2, (pai1, pai2))
    ]

    print(f'Geração {geracao}: {populacao} - Melhor: {pai1} (fitness {fitness(pai1)})')

melhor = max(populacao, key=fitness)
print('\nMelhor solução encontrada:', melhor, '-> Fitness:', fitness(melhor))

# Plotar o grafo organizado
plotar_grafo(historico)
