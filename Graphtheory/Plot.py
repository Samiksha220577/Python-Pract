# import networkx as nx
# import matplotlib.pyplot as plt
#
# # # G = nx.Graph()
# # # nx.draw(G,with_labels=True,font_color="whitesmoke")
# # # plt.show()
# # #----------------------------------------------
# #
# # G = nx.Graph()
# # G.add_node(1)
# # G.add_nodes_from([2,3])
# # G=nx.path_graph(10)
# # nx.draw(G,with_labels=True,font_colour="whitesmoke")
# # plt.show()
# #-------------------------------------
# #
# import networkx as nx
# import matplotlib.pyplot as plt
#
# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2,3])
# G.add_edges_from([(1,2),(1,3)])
# G.add_node("spam")
# G.add_nodes_from("spam")
# G.add_edge(3,'m')
# print(G.number_of_nodes(),G.number_of_edges())
# nx.draw(G,with_labels=True,font_color="whitesmoke")
# plt.show()
# #_______________________________________________________--
# import networkx as nx
# import matplotlib.pyplot as plt
#
# W_G=nx.Graph()
# W_G.add_edge('a','b',weight=0.6)
# nx.draw(W_G,with_labels=True,font_color="whitesmoke")
# plt.show()
# # ___________________________________
# import networkx as nx
# import matplotlib.pyplot as plt
#
# W_G=nx.Graph()
# W_G.add_edge('a','b',weight=0.6)
# W_G.add_edge('a','c',weight=0.2)
# W_G.add_edge('c','d',weight=0.1)
# W_G.add_edge('c','e',weight=0.7)
# W_G.add_edge('c','f',weight=0.9)
# W_G.add_edge('a','d',weight=0.3)
# edge_labels=dict([((u,v),d['weight'])
#     for u,v,d in W_G.edges(data=True)])
# pos=nx.planar_layout(W_G)
# nx.draw_networkx_edge_labels(W_G,pos,edge_labels=edge_labels)
# nx.draw(W_G,pos,with_labels=True)
# plt.show()
# ___________________________________________
# import networkx as nx
# import matplotlib.pyplot as plt
#
# MG=nx.MultiDiGraph()
# MG.add_weighted_edges_from([(1,2,.5),(1,2,.75),(2,3,.5)])
# nx.draw(MG,with_labels=True,font_color="whitesmoke")
# plt.show()
# print(MG.degree(1))


# ____________________________
#subplot to create multiple graphs in a single window
import networkx as nx
import matplotlib.pyplot as plt
G = nx.petersen_graph()

subax1 = plt.subplot(221)
nx.draw_random(G)
subax2 = plt.subplot(222)
nx.draw_random(G)
subax3 = plt.subplot(223)
nx.draw_random(G)
subax4 = plt.subplot(224)
nx.draw_random(G)
nx.draw_shell(G,nlist=[range(5,10),range(5)])
plt.show()