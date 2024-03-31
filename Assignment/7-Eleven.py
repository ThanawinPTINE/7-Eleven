import matplotlib.pyplot as plt
import networkx as nx

def find_shortest_path(G, source, target):
    shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
    shortest_path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
    shortest_path_length = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    return shortest_path_edges, shortest_path_length

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

# รับ input สถานที่ต้นทางและปลายทาง
source = input("Enter source location: ")
target = input("Enter target location: ")

# หาเส้นทางที่มีค่า weight น้อยที่สุด
shortest_path_edges, shortest_path_length = find_shortest_path(G, source, target)

# แสดงผลลัพธ์
print("Shortest path from {} to {}: ".format(source, target))
for edge in shortest_path_edges:
    print("- Pass through:", edge[0], "to", edge[1])
print("Total distance:", shortest_path_length, "kilometers")

# วาดเส้นทางที่ผ่าน
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, width=3, edge_color='red')

# แสดงกราฟ
plt.title("Shortest Path from {} to {}".format(source, target))
plt.show()
