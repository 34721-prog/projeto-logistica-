"""Controlador central: integra recebimento->classificação->separação->armazenamento->pedido->expedição."""
import random
from simulation.environment import World
from simulation.factory_layout import ponto_setor
from logistics.cargo_manager import CargoManager
from logistics.inventory_manager import InventoryManager
from logistics.warehouse_manager import WarehouseManager
from logistics.order_manager import OrderManager
from logistics.shipment_manager import ShipmentManager
from automation.conveyor import Conveyor
from automation.sorting_system import SortingSystem
from automation.loading_system import LoadingSystem
from robots.mobile_robot import MobileRobot
from robots.robotic_arm import RoboticArm
from robots.robot_controller import RobotController
from sensors.sensors import DistanceSensor, PresenceSensor
from intelligence.anomaly_detector import AnomalyDetector
from intelligence.task_scheduler import TaskScheduler

class SimulationController:
    def __init__(self, seed=42, n_robos=4):
        random.seed(seed)
        self.tick=0; self.mundo=World()
        self.cargo=CargoManager(); self.estoque=InventoryManager(); self.armazem=WarehouseManager()
        self.pedidos=OrderManager(self.estoque); self.expedicao=ShipmentManager()
        self.esteira=Conveyor("EST-01","B"); self.sorting=SortingSystem(); self.loading=LoadingSystem()
        self.braco=RoboticArm("ARM-01","C")
        self.sensores={"distancia":DistanceSensor("SEN-D01","B"),"presenca":PresenceSensor("SEN-P01","A")}
        robos=[MobileRobot(f"AMR-{i+1:02d}", (3+i*2,18), self.mundo) for i in range(n_robos)]
        for r in robos: self.mundo.robos[r.id]=r
        self.frota=RobotController(robos); self.detector=AnomalyDetector(); self.scheduler=TaskScheduler()
        self.eventos=[]; self.alertas=[]; self.stats={"recebidos":0,"armazenados":0,"expedidos":0}
    def log(self,msg): self.eventos.append(f"[t={self.tick}] {msg}")
    def receber_carga(self, produto, quantidade):
        lote=self.cargo.receber(produto, quantidade)
        self.sensores["presenca"].ler(True)
        self.esteira.transportar(lote, self.sorting.destino_classificacao(lote))
        self.braco.separar(lote, "C-SEPARACAO")
        endereco=self.armazem.alocar(quantidade)
        robo=self.frota.disponivel()
        destino=self.armazem.posicao_grid(endereco)
        def concluir(r, lote=lote, endereco=endereco):
            self.estoque.adicionar(lote.produto, lote.quantidade, endereco); lote.localizacao=endereco
            self.stats["armazenados"]+=1; self.log(f"{r.id} armazenou {lote.produto} x{lote.quantidade} em {endereco}")
        if robo is None:
            # sem robô livre: armazenamento direto registrado (fila física aguardaria; aqui conclui no endereço)
            self.estoque.adicionar(produto, quantidade, endereco); lote.localizacao=endereco; self.stats["armazenados"]+=1
        else:
            robo.carga=lote; robo.atribuir(destino, ao_chegar=concluir, carga=lote)
        self.stats["recebidos"]+=1; self.log(f"Recebido {produto} x{quantidade} lote {lote.id} -> {endereco}")
        return lote
    def processar_pedido(self, cliente, itens, prioridade=1, destino="São Paulo-SP"):
        pedido=self.pedidos.criar(cliente, itens, prioridade)
        res=self.pedidos.reservar_e_separar(pedido.id)
        if not res["ok"]:
            self.log(f"Pedido {pedido.id} aguardando estoque: {res['faltas']}"); return {"pedido":pedido,"ok":False,"faltas":res["faltas"]}
        for prod,ender in res["retiradas"].items(): self.armazem.liberar(ender, itens[prod])
        self.pedidos.expedir(pedido.id)
        ship=self.expedicao.registrar_saida(pedido, destino=destino); self.loading.carregar(ship)
        self.stats["expedidos"]+=1; self.log(f"Pedido {pedido.id} expedido e carregado para {destino}")
        return {"pedido":pedido,"ok":True,"shipment":ship}
    def passo(self):
        self.tick+=1; self.frota.passo()
        ctx={"utilizacao_armazem":self.armazem.utilizacao(),
             "robos_bloqueados":sum(1 for r in self.mundo.robos.values() if r.estado=="BLOQUEADO"),
             "pedidos_aguardando":sum(1 for p in self.pedidos.pedidos.values() if p.status=="AGUARDANDO_ESTOQUE")}
        self.alertas=self.detector.alertas_operacionais(ctx)
    def rodar(self, ticks=200):
        for _ in range(ticks): self.passo()
    def estado(self):
        return {"tick":self.tick,"estoque":self.estoque.snapshot(),
                "robos":[{"id":r.id,"pos":r.pos,"estado":r.estado,"bateria":round(r.bateria,1),"tarefas":r.tarefas_concluidas} for r in self.mundo.robos.values()],
                "stats":self.stats,"alertas":self.alertas,"eventos":self.eventos[-30:],
                "pedidos":[{"id":p.id,"cliente":p.cliente,"itens":p.itens,"status":p.status} for p in self.pedidos.pedidos.values()],
                "utilizacao_armazem":round(self.armazem.utilizacao(),3),
                "obstaculos":list(self.mundo.obstaculos)}
