import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))
from simulation.simulation_controller import SimulationController
from automation.conveyor import Conveyor
from sensors.sensors import PresenceSensor, SensorError
from logistics.models import Batch
class T(unittest.TestCase):
    def test_fluxo_completo_soja(self):
        s=SimulationController(); s.receber_carga("SOJA",40); s.rodar(400)
        self.assertEqual(s.estoque.saldo("SOJA"),40)
        r=s.processar_pedido("Coop",{"SOJA":15}); self.assertTrue(r["ok"]); self.assertEqual(s.estoque.saldo("SOJA"),25); self.assertEqual(s.stats["expedidos"],1)
    def test_esteira_parada(self):
        c=Conveyor("E1","B"); c.parar()
        with self.assertRaises(RuntimeError): c.transportar(Batch("MILHO",5),"B")
    def test_falha_sensor(self):
        s=PresenceSensor("S1","A"); s.injetar_falha()
        with self.assertRaises(SensorError): s.ler(True)
    def test_classificacao_milho_cafe(self):
        from automation.sorting_system import SortingSystem
        ss=SortingSystem(); self.assertEqual(ss.destino_classificacao(Batch("MILHO",1)),"B-GRAOS")
if __name__=="__main__": unittest.main()
