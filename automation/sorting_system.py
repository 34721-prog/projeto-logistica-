import config
class SortingSystem:
    """Classifica por categoria do produto (regra determinística, não 'IA')."""
    def classificar(self, lote):
        return config.PRODUCTS[lote.produto]["categoria"]
    def destino_classificacao(self, lote): return f"B-{self.classificar(lote).upper()}"
