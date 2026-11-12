class RoboticArm:
    def __init__(self, aid, setor): self.id=aid; self.setor=setor; self.estado="IDLE"; self.ciclos=0
    def separar(self, lote, destino):
        self.estado="OPERANDO"; lote.localizacao=destino; self.ciclos+=1; self.estado="IDLE"
        return {"arm":self.id,"lote":lote.id,"destino":destino}
