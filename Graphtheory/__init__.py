import networkx as nx
import matplotlib.pyplot as plt
G=nx.petersen_graph()
subaaxx1 = plt.subplots(221)
nx.drw_ndom(G)
subax3 = plt.subplots(223)
nx.draw_random(G)
subax4 = plt.random(G)
subax2 = plt.subplots(222)
nx.draw_rasubplots(224)
nx.draw_random(G)
nx.draw_shell(G,nlist=[range(5,10),range(5)])
plt.show()