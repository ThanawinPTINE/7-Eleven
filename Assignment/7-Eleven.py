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
G.add_edge('In front of Jakkaphong', 'Prachin Train station', weight=1)
G.add_edge('Prachin Train station', 'Mueng Prachin', weight=1)
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

my_dict = {1: 'KMUTNB', 2: 'NUENHOM', 3: 'WONGWIAN', 4: 'PTT TALAD', 5: 'PTT DongKheelhenk', 6: 'Talad DongBang', 7: 'Yag Mhai Khed', 8: 'Talad NhongChaAom', 9: 'PTT NhongChaAom', 10: 'In front of Jakkaphong', 11: 'Prachin Train station', 12: 'Mueng Prachin', 13: 'PTT Prachin', 14: 'BKS Prachin', 15: 'DunrhiRoad', 16: 'Talad TedsabanPrachin', 17: 'BanAue'}
for key, value in my_dict.items():
    print(key, ":", value)

# รับ input สถานที่ต้นทางและปลายทาง
while True:
    try:
        source = input("Enter Source location name from above : ")
        if source not in my_dict.values():
            raise ValueError("Invalid source location name.")
        
        target = input("Enter Target location name from above : ")
        if target not in my_dict.values():
            raise ValueError("Invalid target location name.")

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

        break  # ออกจากลูปหลังจากที่ได้รับข้อมูลที่ถูกต้อง
    except ValueError as e:
        print("Error:", e)
    except KeyError:
        print("Invalid input! Please enter a valid location name.")

