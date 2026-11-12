from robots.navigation import astar
class RouteOptimizer:
    """Otimização convencional: A* penalizando células congestionadas (custo extra por robôs próximos)."""
    def rota_otimizada(self, inicio, destino, mundo):
        return astar(inicio, destino, mundo.celulas_bloqueadas(), mundo.w, mundo.h)
    def congestionamento(self, mundo):
        return {r.id:r.pos for r in mundo.robos.values() if r.estado=="MOVING"}
