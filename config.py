"""Configuração central do AgroLogistics AI."""
GRID_W, GRID_H = 60, 40
TICK_SECONDS = 0.2
RANDOM_SEED = 42
PRODUCTS = {
 "SOJA": {"nome":"Soja","categoria":"graos","peso_kg":25},
 "MILHO": {"nome":"Milho","categoria":"graos","peso_kg":25},
 "CAFE": {"nome":"Café","categoria":"graos","peso_kg":20},
 "TRIGO": {"nome":"Trigo","categoria":"graos","peso_kg":25},
 "ARROZ": {"nome":"Arroz","categoria":"graos","peso_kg":20},
 "ALGODAO": {"nome":"Algodão","categoria":"fibras","peso_kg":30},
 "FERTILIZANTE": {"nome":"Fertilizantes","categoria":"insumos","peso_kg":50},
 "INSUMO": {"nome":"Insumos Agrícolas","categoria":"insumos","peso_kg":15},
}
# Setores: (x,y,w,h) no grid
SECTORS = {
 "A":{"nome":"Recebimento","rect":(1,1,12,10),"cor":"#38bdf8"},
 "B":{"nome":"Classificação","rect":(15,1,13,10),"cor":"#a78bfa"},
 "C":{"nome":"Separação","rect":(30,1,13,10),"cor":"#f472b6"},
 "D":{"nome":"Armazenamento","rect":(15,14,28,11),"cor":"#34d399"},
 "E":{"nome":"Preparação de Pedidos","rect":(45,14,13,11),"cor":"#fbbf24"},
 "F":{"nome":"Carregamento","rect":(45,27,13,11),"cor":"#fb7185"},
 "G":{"nome":"Expedição","rect":(30,27,13,11),"cor":"#60a5fa"},
}
STORAGE_CAPACITY_PER_ADDRESS = 100
LOW_STOCK_THRESHOLD = 20
