from .models import Batch
class CargoManager:
    def __init__(self): self.lotes={}; self.movimentacoes=[]
    def receber(self, produto, quantidade):
        if produto not in __import__('config').PRODUCTS: raise ValueError(f"Produto desconhecido: {produto}")
        b=Batch(produto, quantidade); self.lotes[b.id]=b
        self.movimentacoes.append((b.id, produto, quantidade, "RECEBIDO", "A-ENTRADA")); return b
    def mover(self, lote_id, destino):
        b=self.lotes[lote_id]; b.localizacao=destino
        self.movimentacoes.append((lote_id,b.produto,b.quantidade,"MOVIDO",destino))
