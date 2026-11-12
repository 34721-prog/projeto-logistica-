class LoadingSystem:
    def __init__(self): self.carregamentos=[]
    def carregar(self, shipment):
        if shipment["status"]!="EXPEDIDO": raise ValueError("Somente expedição conferida pode carregar")
        shipment["status"]="CARREGADO"; self.carregamentos.append(shipment); return shipment
