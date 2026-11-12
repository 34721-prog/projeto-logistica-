from .navigation import astar
class MobileRobot:
    """AMR: máquina de estados IDLE->MOVING->LOADED->MOVING->IDLE, com desvio de obstáculos via replanejamento A*."""
    def __init__(self, rid, pos, mundo):
        self.id=rid; self.pos=pos; self.mundo=mundo; self.estado="IDLE"; self.rota=[]; self.carga=None
        self.bateria=100.0; self.tarefas_concluidas=0; self.log=[]; self.destino=None; self._ao_chegar=None
    def atribuir(self, destino, ao_chegar=None, carga=None):
        rota=astar(self.pos, destino, self.mundo.celulas_bloqueadas(), self.mundo.w, self.mundo.h)
        if rota is None: self.estado="BLOQUEADO"; self.log.append(f"Sem rota para {destino}"); return False
        self.rota=rota[1:]; self.destino=destino; self._ao_chegar=ao_chegar
        if carga: self.carga=carga
        self.estado="MOVING"; return True
    def passo(self):
        if self.estado!="MOVING" or not self.rota: return
        proximo=self.rota[0]
        if proximo in self.mundo.celulas_bloqueadas():
            # obstáculo dinâmico detectado: replaneja
            nova=astar(self.pos, self.destino, self.mundo.celulas_bloqueadas(), self.mundo.w, self.mundo.h)
            if nova is None: self.estado="BLOQUEADO"; self.log.append("Bloqueado por obstáculo"); return
            self.rota=nova[1:]; self.log.append("Rota replanejada (obstáculo)"); return
        if self.mundo.posicao_ocupada_por_robo(proximo, exceto=self.id):
            self.log.append("Aguardando robô à frente (anti-colisão)"); return
        self.pos=self.rota.pop(0); self.bateria=max(0,self.bateria-0.05)
        if not self.rota:
            self.estado="IDLE"; cb,self._ao_chegar=self._ao_chegar,None
            if self.carga: self.tarefas_concluidas+=1
            if cb: cb(self)
