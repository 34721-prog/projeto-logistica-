class TaskScheduler:
    """Escalonador por prioridade + menor distância (heurística clássica, documentada como tal)."""
    def escolher(self, tarefas, robos_livres):
        if not tarefas or not robos_livres: return None
        tarefa=sorted(tarefas, key=lambda t:(-t.get("prioridade",1), t["id"]))[0]
        robo=min(robos_livres, key=lambda r: abs(r.pos[0]-tarefa["destino"][0])+abs(r.pos[1]-tarefa["destino"][1]))
        return tarefa, robo
