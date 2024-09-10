from math import radians, sin, cos, sqrt, atan2
import networkx as nx
 
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
 
coords = {
    "Gilroy": (37.0057, -121.5698),
    "Cheyenne": (41.1390, -104.8202),
    "Fargo": (46.8772, -96.7898),
    "Zanesville": (39.9406, -82.0138),
    "Worcester": (42.2626, -71.8023),
    "Tupelo": (34.2570, -88.7036),
    "Lubbock": (33.5779, -101.8552),
}
 
edges = [
    ("Lubbock", "Gilroy"),
    ("Lubbock", "Fargo"),
    ("Lubbock", "Zanesville"),
    ("Gilroy", "Cheyenne"),
    ("Cheyenne", "Fargo"),
    ("Cheyenne", "Lubbock"),
    ("Fargo", "Zanesville"),
    ("Tupelo", "Lubbock"),
    ("Tupelo", "Zanesville"),
    ("Zanesville", "Worcester"),
    ("Worcester", "Tupelo")
]
 
G = nx.Graph()
 
for city, (lat, lon) in coords.items():
    G.add_node(city, pos=(lon, lat))
 
for city1, city2 in edges:
    dist = haversine(coords[city1][0], coords[city1][1], coords[city2][0], coords[city2][1])
    G.add_edge(city1, city2, weight=dist)
 
def shortest_path(start, end):
    try:
        path = nx.dijkstra_path(G, start, end, weight='weight')
        length = nx.dijkstra_path_length(G, start, end, weight='weight')
        return path, length
    except nx.NetworkXNoPath:
        return [], float('inf')
 
def find_routes():
    routes = [
        ("Gilroy", "Lubbock"),
        ("Gilroy", "Zanesville"),
        ("Tupelo", "Fargo"),
        ("Worcester", "Gilroy")
    ]
    for start, end in routes:
        path, length = shortest_path(start, end)
        print(f"{start} to {end}: Path = {path}, Length = {length:.2f} km")
 
find_routes()