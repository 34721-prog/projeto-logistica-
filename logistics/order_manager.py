from .models import Order
class OrderManager:
    def __init__(self, inventory):
        self.inventory=inventory; self.pedidos={}
    def criar(self, cliente, itens, prioridade=1):
        for p,q in itens.items():
            if q<=0: raise ValueError("item com quantidade inválida")
        o=Order(cliente, dict(itens), prioridade); self.pedidos[o.id]=o; return o
    def reservar_e_separar(self, order_id):
        """Separa somente se houver saldo total; caso contrário marca falta (teste de estoque insuficiente)."""
        o=self.pedidos[order_id]
        faltas={p:q-self.inventory.saldo(p) for p,q in o.itens.items() if self.inventory.saldo(p)<q}
        if faltas: o.status="AGUARDANDO_ESTOQUE"; return {"ok":False,"faltas":faltas}
        retiradas={}
        for p,q in o.itens.items(): retiradas[p]=self.inventory.remover(p,q)
        o.status="SEPARADO"; return {"ok":True,"retiradas":retiradas}
    def expedir(self, order_id):
        o=self.pedidos[order_id]
        if o.status!="SEPARADO": raise ValueError(f"Pedido {order_id} não está separado ({o.status})")
        o.status="EXPEDIDO"; return o
