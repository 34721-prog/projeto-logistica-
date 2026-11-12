class RobotController:
    def __init__(self, robos): self.robos={r.id:r for r in robos}
    def disponivel(self):
        livres=[r for r in self.robos.values() if r.estado=="IDLE"]
        return min(livres, key=lambda r: r.tarefas_concluidas) if livres else None  # balanceamento por uso
    def passo(self):
        for r in self.robos.values(): r.passo()
