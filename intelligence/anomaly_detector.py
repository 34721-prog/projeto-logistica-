import statistics
class AnomalyDetector:
    """Detecção estatística simples (z-score) — IA/ML leve e honesta, sem resultados fabricados."""
    def __init__(self): self.serie=[]
    def registrar(self, valor): self.serie.append(valor)
    def verificar(self, valor):
        if len(self.serie)<5: return False
        m=statistics.mean(self.serie); d=statistics.pstdev(self.serie) or 1
        return abs((valor-m)/d) > 2.5
    def alertas_operacionais(self, ctx):
        a=[]
        if ctx.get("utilizacao_armazem",0)>0.9: a.append("Armazém acima de 90% de ocupação")
        if ctx.get("robos_bloqueados",0)>0: a.append(f"{ctx['robos_bloqueados']} robô(s) bloqueado(s)")
        if ctx.get("pedidos_aguardando",0)>0: a.append(f"{ctx['pedidos_aguardando']} pedido(s) aguardando estoque")
        return a
