from dataclasses import dataclass, field
import itertools, time
_ids = itertools.count(1)
def new_id(prefix): return f"{prefix}-{next(_ids):04d}"
@dataclass
class Batch:
    produto: str; quantidade: int; lote: str = ""; id: str = field(default_factory=lambda: new_id("LOTE"))
    localizacao: str = "A-ENTRADA"; recebido_em: float = field(default_factory=time.time)
    def __post_init__(self):
        if not self.lote: self.lote = f"L-{self.produto}-{self.id.split('-')[1]}"
@dataclass
class Order:
    cliente: str; itens: dict; prioridade: int = 1; id: str = field(default_factory=lambda: new_id("PED"))
    status: str = "PENDENTE"; criado_em: float = field(default_factory=time.time)
