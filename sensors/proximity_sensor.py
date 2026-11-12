import random
class SensorError(Exception): pass
class BaseSensor:
    def __init__(self, sid, setor):
        self.id=sid; self.setor=setor; self.estado="OPERACIONAL"; self.leituras=[]; self._falhar=False
    def injetar_falha(self): self._falhar=True; self.estado="FALHA"
    def recuperar(self): self._falhar=False; self.estado="OPERACIONAL"
    def _check(self):
        if self._falhar: raise SensorError(f"Sensor {self.id} em falha (simulação de falha injetada)")
class DistanceSensor(BaseSensor):
    def ler(self, distancia_real):
        self._check(); v=max(0.0, distancia_real + random.uniform(-0.05,0.05)); self.leituras.append(v); return v
class ProximitySensor(BaseSensor):
    def ler(self, distancia_real, limiar=2.0): self._check(); return distancia_real <= limiar
class PresenceSensor(BaseSensor):
    def ler(self, ocupado): self._check(); return bool(ocupado)
# aliases por arquivo exigido na especificação
