class ShipmentManager:
    def __init__(self): self.expedicoes=[]
    def registrar_saida(self, order, caminhao="CAM-001", destino="Destino não informado"):
        reg={"pedido":order.id,"cliente":order.cliente,"itens":dict(order.itens),"caminhao":caminhao,"destino":destino,"status":"EXPEDIDO"}
        self.expedicoes.append(reg); return reg
