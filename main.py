"""AgroLogistics AI — ponto de entrada.
Uso: python3 main.py           (demonstração headless completa)
     python3 main.py --serve   (dashboard web em http://localhost:8000)
"""
import sys
def demo():
    from simulation.simulation_controller import SimulationController
    sim=SimulationController()
    sim.receber_carga("SOJA", 40); sim.receber_carga("MILHO", 30); sim.receber_carga("CAFE", 20)
    sim.rodar(300)
    print("Estoque após recebimento:", sim.estoque.snapshot())
    r1=sim.processar_pedido("Cooperativa Sul", {"SOJA":15,"MILHO":10}, destino="Campinas-SP")
    r2=sim.processar_pedido("Exportadora Norte", {"CAFE":50}, destino="Porto de Santos-SP")  # insuficiente
    print("Pedido 1:", r1["ok"], "| Pedido 2 (café insuficiente):", r2["ok"], r2.get("faltas"))
    print("Stats:", sim.stats); print("Últimos eventos:"); [print(" ",e) for e in sim.eventos[-8:]]
    return sim
if __name__=="__main__":
    if "--serve" in sys.argv:
        from dashboard.web_server import serve; serve()
    else: demo()
