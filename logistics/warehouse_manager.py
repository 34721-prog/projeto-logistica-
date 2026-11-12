import config
class WarehouseManager:
    """Endereçamento do Setor D: prateleiras D-R{rua}P{pos} com capacidade finita."""
    def __init__(self, ruas=4, posicoes=6):
        self.enderecos = [f"D-R{r}P{p}" for r in range(1,ruas+1) for p in range(1,posicoes+1)]
        self.ocupacao = {e:0 for e in self.enderecos}; self.cap = config.STORAGE_CAPACITY_PER_ADDRESS
    def alocar(self, qtd):
        # Prefere o endereço mais vazio que comporte a carga: distribui lotes e
        # evita que vários AMRs disputem a mesma célula de destino.
        candidatos=[e for e in self.enderecos if self.cap-self.ocupacao[e]>=qtd]
        if not candidatos: raise ValueError("Armazém sem espaço para a quantidade")
        e=min(candidatos, key=lambda x: self.ocupacao[x]); self.ocupacao[e]+=qtd; return e
    def liberar(self, endereco, qtd): self.ocupacao[endereco]=max(0,self.ocupacao[endereco]-qtd)
    def utilizacao(self): return sum(self.ocupacao.values())/(len(self.enderecos)*self.cap)
    def posicao_grid(self, endereco):
        r=int(endereco.split('R')[1].split('P')[0]); p=int(endereco.split('P')[1])
        return (16+p*4, 15+r*2)
