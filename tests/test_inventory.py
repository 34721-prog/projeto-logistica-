import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))
from logistics.inventory_manager import InventoryManager
class T(unittest.TestCase):
    def test_entrada_saida(self):
        i=InventoryManager(); i.adicionar("SOJA",50,"D-R1P1"); i.remover("SOJA",20,"D-R1P1"); self.assertEqual(i.saldo("SOJA"),30)
    def test_insuficiente(self):
        i=InventoryManager()
        with self.assertRaises(ValueError): i.remover("MILHO",10)
if __name__=="__main__": unittest.main()
