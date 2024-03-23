import networkx as nx
import matplotlib.pyplot as plt

tree_dict = {
    1: {
        "Group 1.1":"Root",
        "Group 1.2":"Root",
        "Group 1.3":"Root",
        "Group 1.4":"Root",
        "Group 1.5":"Root"
        },
    2: {
        "Group 2.1":"Group 1.1",
        "Group 2.2":"Group 1.2",
        "Group 2.3":"Group 1.3",
        "Group 2.4":"Group 1.4",
        "Group 2.5":"Group 1.5"
        },
    3: {
        "Group 3.1":"Group 2.1",
        "Group 3.2":"Group 2.2",
        "Group 3.3":"Group 2.3",
        "Group 3.4":"Group 2.4",
        "Group 3.5":"Group 2.5"
        },
    4: {
        "Group 4.1":"Group 3.1",
        "Group 4.2":"Group 3.2",
        "Group 4.3":"Group 3.3",
        "Group 4.4":"Group 3.4",
        "Group 4.5":"Group 3.5"
        }
    }

# Create a NextworkX directed graph
g = nx.DiGraph()
g.add_nodes_from(['Root'], subset=4)
g.add_nodes_from(tree_dict[1].keys(), subset=3)
g.add_nodes_from(tree_dict[2].keys(), subset=2)
g.add_nodes_from(tree_dict[3].keys(), subset=1)
g.add_nodes_from(tree_dict[4].keys(), subset=0)

# Add Title to Plot
plt.title('Multipartite Tree Graph')

# Create a list of the edges
edges = []
for subset_stuff in tree_dict.values():
    for node, prev_node in subset_stuff.items():
        edges.append((prev_node, node))

# Draw the nodes with the multipartite layout
pos = nx.multipartite_layout(g, align='horizontal')
nx.draw(g, pos, with_labels=True, node_size=1500, font_size=8)

# Draw the edges with the multipartite layout
nx.draw_networkx_edges(g, pos, edgelist=edges, arrows=True, node_size=1500)

# Show the plot
plt.show()
