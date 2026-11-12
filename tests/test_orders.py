import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),".."))
from logistics.inventory_manager import InventoryManager
from logistics.order_manager import OrderManager
class T(unittest.TestCase):
    def test_pedido_ok_e_insuficiente(self):
        inv=InventoryManager(); inv.adicionar("CAFE",10,"D-R1P1"); om=OrderManager(inv)
        o1=om.criar("Cli",{"CAFE":4}); self.assertTrue(om.reservar_e_separar(o1.id)["ok"]); self.assertEqual(inv.saldo("CAFE"),6)
        o2=om.criar("Cli",{"CAFE":99}); r=om.reservar_e_separar(o2.id); self.assertFalse(r["ok"]); self.assertEqual(om.pedidos[o2.id].status,"AGUARDANDO_ESTOQUE")
if __name__=="__main__": unittest.main()
