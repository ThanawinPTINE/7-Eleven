import matplotlib.pyplot as plt
import networkx as nx

# สร้างกราฟแบบ Undirected Graph
G = nx.Graph()

# เพิ่มเส้นเชื่อมระหว่างจุด
G.add_edge('KMUTNB', 'NUENHOM', weight=3)  # ระยะทางระหว่าง A และ B เป็น 4
G.add_edge('NUENHOM', 'WONGWIAN', weight=2)  # ระยะทางระหว่าง B และ C เป็น 2
G.add_edge('WONGWIAN', 'PTT Talad', weight=2)  # ระยะทางระหว่าง C และ D เป็น 5
G.add_edge('PTT Talad', 'PTT DongKheelhenk', weight=5)  # ระยะทางระหว่าง D และ E เป็น 3
G.add_edge('PTT DongKheelhenk', 'Talad DongBang', weight=3)  # ระยะทางระหว่าง E และ F เป็น 6
G.add_edge('WONGWIAN', 'Yag Mhai Khed', weight=4)
G.add_edge('Yag Mhai Khed', 'Talad DongBang', weight=11)
G.add_edge('WONGWIAN', 'Talad NhongChaAom', weight=7)
G.add_edge('Talad NhongChaAom', 'PTT NhongChaAom', weight=2)
G.add_edge('Yag Mhai Khed', 'In front of Jakkaphong', weight= 5)
G.add_edge('In front of Jakkaphong', 'Prachin Trainstation', weight=1)
G.add_edge('Prachin Trainstation', 'Mueng Prachin', weight=1)
G.add_edge('Mueng Prachin', 'PTT Prachin', weight=1)
G.add_edge('PTT Prachin', 'BKS Prachin', weight=1)
G.add_edge('BKS Prachin', 'DunrhiRoad', weight=1)
G.add_edge('DunrhiRoad', 'Talad TedsabanPrachin', weight=1)
G.add_edge('BKS Prachin','BanAue', weight=1)

# กำหนดตำแหน่งของแต่ละจุด
pos = nx.spring_layout(G)

# วาดเส้นเชื่อมระหว่างจุดทั้งหมด
nx.draw_networkx_edges(G, pos, width=[G[u][v]['weight']*2 for u, v in G.edges()])  # สูงขึ้นเพื่อแสดงความชัดเจน

# วาดจุด
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12)

# ทำ Graph Traversal ด้วย Depth-first Search
dfs_edges = list(nx.dfs_edges(G, source='KMUTNB'))  # เริ่มต้น DFS ที่จุด KMUTNB
dfs_edges.append((dfs_edges[-1][1], dfs_edges[0][0]))  # เพิ่มเส้นเชื่อมระหว่างจุดสุดท้ายกับจุดเริ่มต้นเพื่อปิดวง

# วาดเส้นทางที่ผ่าน
for edge in dfs_edges:
    nx.draw_networkx_edges(G, pos, edgelist=[edge], width=3, edge_color='red')

# แสดงกราฟ
plt.title("Depth-first Search Traversal")
plt.show()
