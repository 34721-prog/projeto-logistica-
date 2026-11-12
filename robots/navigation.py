import heapq
def astar(inicio, destino, bloqueadas, w, h):
    """A* em grid 4-direções. Retorna lista de células ou None se sem rota."""
    if inicio==destino: return [inicio]
    bloq=set(bloqueadas)-{inicio,destino}
    aberta=[(0,inicio)]; veio={inicio:None}; g={inicio:0}
    def heur(p): return abs(p[0]-destino[0])+abs(p[1]-destino[1])
    while aberta:
        _,atual=heapq.heappop(aberta)
        if atual==destino:
            rota=[]
            while atual: rota.append(atual); atual=veio[atual]
            return list(reversed(rota))
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            v=(atual[0]+dx,atual[1]+dy)
            if not (0<=v[0]<w and 0<=v[1]<h) or v in bloq: continue
            ng=g[atual]+1
            if v not in g or ng<g[v]: g[v]=ng; veio[v]=atual; heapq.heappush(aberta,(ng+heur(v),v))
    return None
