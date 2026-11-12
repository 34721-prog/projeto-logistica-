import config
class World:
    """Mundo em grid (abstração 2D do galpão 3D — ver docs sobre limitação do BrowserBotics)."""
    def __init__(self):
        self.w=config.GRID_W; self.h=config.GRID_H; self.obstaculos=set(); self.robos={}
        # paredes internas simples entre setores (com passagens)
        for y in range(1,11): self.obstaculos.add((14,y))
        self.obstaculos.discard((14,5))
    def adicionar_obstaculo(self, pos): self.obstaculos.add(pos)
    def remover_obstaculo(self, pos): self.obstaculos.discard(pos)
    def celulas_bloqueadas(self): return set(self.obstaculos)
    def posicao_ocupada_por_robo(self, pos, exceto=None):
        return any(r.pos==pos and r.id!=exceto for r in self.robos.values())
