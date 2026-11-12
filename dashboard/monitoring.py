def kpis(sim):
    e=sim.estado()
    return {"tick":e["tick"], "recebidos":e["stats"]["recebidos"], "armazenados":e["stats"]["armazenados"],
            "expedidos":e["stats"]["expedidos"], "robos_ativos":sum(1 for r in e["robos"] if r["estado"]=="MOVING"),
            "utilizacao_armazem":e["utilizacao_armazem"], "alertas":e["alertas"]}
