from collections import defaultdict
class InventoryManager:
    """Estoque real por produto e por endereço. Nenhuma movimentação é fictícia:
    toda entrada/saída altera estas estruturas e gera registro auditável."""
    def __init__(self):
        self.por_produto = defaultdict(int); self.por_endereco = {}  # endereco -> {produto:qtd}
        self.historico = []
    def adicionar(self, produto, qtd, endereco):
        if qtd <= 0: raise ValueError("quantidade deve ser positiva")
        self.por_produto[produto] += qtd
        self.por_endereco.setdefault(endereco, defaultdict(int))[produto] += qtd
        self.historico.append(("ENTRADA", produto, qtd, endereco))
    def remover(self, produto, qtd, endereco=None):
        if self.por_produto[produto] < qtd: raise ValueError(f"Estoque insuficiente de {produto}: {self.por_produto[produto]} < {qtd}")
        # escolhe endereço com saldo se não informado
        if endereco is None:
            endereco = next((e for e,v in self.por_endereco.items() if v.get(produto,0) >= qtd), None)
            if endereco is None: raise ValueError(f"Sem endereço único com {qtd} de {produto} (fragmentado)")
        if self.por_endereco.get(endereco,{}).get(produto,0) < qtd: raise ValueError("Saldo insuficiente no endereço")
        self.por_produto[produto]-=qtd; self.por_endereco[endereco][produto]-=qtd
        self.historico.append(("SAIDA", produto, qtd, endereco)); return endereco
    def saldo(self, produto): return self.por_produto[produto]
    def snapshot(self): return {k:v for k,v in self.por_produto.items()}
