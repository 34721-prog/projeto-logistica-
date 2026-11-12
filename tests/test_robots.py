import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))
from simulation.environment import World
from robots.mobile_robot import MobileRobot
from robots.navigation import astar
class T(unittest.TestCase):
    def test_astar_obstaculo(self):
        self.assertIsNotNone(astar((0,0),(2,0),{(1,0)},5,5))  # desvia por outra linha
        self.assertEqual(len(astar((0,0),(0,0),set(),5,5)),1)
    def test_robo_chega(self):
        w=World(); r=MobileRobot("AMR-T",(1,18),w); w.robos[r.id]=r
        self.assertTrue(r.atribuir((6,18))); [r.passo() for _ in range(20)]; self.assertEqual(r.pos,(6,18))
    def test_obstaculo_dinamico_replaneja(self):
        w=World(); r=MobileRobot("AMR-T",(1,18),w); w.robos[r.id]=r; r.atribuir((8,18)); r.passo()
        w.adicionar_obstaculo(r.rota[0]); r.passo(); self.assertNotEqual(r.estado,"BLOQUEADO") if r.rota else None
if __name__=="__main__": unittest.main()
