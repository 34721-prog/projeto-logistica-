class Conveyor:
    def __init__(self, cid, setor, velocidade=2):
        self.id=cid; self.setor=setor; self.velocidade=velocidade; self.estado="OPERACIONAL"; self.fila=[]
    def parar(self): self.estado="PARADA"
    def retomar(self): self.estado="OPERACIONAL"
    def transportar(self, lote, destino):
        if self.estado!="OPERACIONAL": raise RuntimeError(f"Esteira {self.id} parada — interrupção simulada")
        lote.localizacao=destino; self.fila.append(lote.id); return destino
