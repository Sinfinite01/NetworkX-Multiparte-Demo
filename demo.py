import networkx as nx
import matplotlib.pyplot as plt

D_iter_current_previous =    {
    1: {
        "Group 1":{"sample_0":0.5, "sample_1":0.5, "sample_2":0, "sample_3":0, "sample_4":0},
        "Group 2":{"sample_0":0, "sample_1":0, "sample_2":1, "sample_3":0, "sample_4":0},
        "Group 3":{"sample_0":0, "sample_1":0, "sample_2":0, "sample_3":0.5, "sample_4":0.5}
        },
    2: {
        "Group 1":{"Group 1":1, "Group 2":0, "Group 3":0},
        "Group 2":{"Group 1":0, "Group 2":1, "Group 3":0},
        "Group 3":{"Group 1":0, "Group 2":0, "Group 3":1}
        },
    3: {
        "Group 1":{"Group 1":0.25, "Group 2":0, "Group 3":0.75},
        "Group 2":{"Group 1":0.25, "Group 2":0.75, "Group 3":0}
        },
    4: {
        "Group 1":{"Group 1":1, "Group 2":0},
        "Group 2":{"Group 1":0.25, "Group 2":0.75}
        }
    }

# Create a NextworkX directed graph
g = nx.DiGraph()
g.add_nodes_from(['sample_0', 'sample_1', 'sample_2', 'sample_3', 'sample_4'], subset=0)
g.add_nodes_from(['Group 1.1', 'Group 2.1', 'Group 3.1'], subset=1)
g.add_nodes_from(['Group 1.2', 'Group 2.2', 'Group 3.2'], subset=2)
g.add_nodes_from(['Group 1.3', 'Group 2.3'], subset=3)
g.add_nodes_from(['Group 1.4', 'Group 2.4'], subset=4)

# Add Title to Plot
plt.title('Multipartite Weighted Directed Graph')

# Create a list of the edges and alphas (opacity)
edges = []
alphas = []
for subset, subset_stuff in D_iter_current_previous.items():
    for node, prev_nodes in subset_stuff.items():
        for prev_node, weight in prev_nodes.items():
            if subset > 1:
                edges.append((f'{prev_node}.{subset-1}', f'{node}.{subset}'))
                alphas.append(weight)
            else:
                edges.append((f'{prev_node}', f'{node}.{subset}'))
                alphas.append(weight)

# Make a dict of the edge labels
edge_labels = dict(zip(edges, alphas))

# Draw the nodes with the multipartite layout
pos = nx.multipartite_layout(g, align='vertical')
nx.draw(g, pos, with_labels=True, node_size=1500, font_size=8)

# Draw the edges with their corresponding alphas
nx.draw_networkx_edges(g, pos, edgelist=edges, alpha=alphas, arrows=True, node_size=1500)

# Draw the edge labels with their corresponding alphas
counter = 0
for edge, alpha in edge_labels.items():
    if alpha > 0:
        nx.draw_networkx_edge_labels(g, pos, edge_labels={edge: float(alpha)}, alpha=float(alpha), font_size=7)

# Show the plot
plt.show()