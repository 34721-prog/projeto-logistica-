# Arquitetura
- **simulation/**: mundo em grid 60x40, setores A–G (config.py), controlador central que integra o fluxo.
- **robots/**: AMR com máquina de estados + A* (navigation.py), replanejamento ao detectar obstáculo, anti-colisão por espera; braço robótico; controlador de frota com balanceamento por nº de tarefas.
- **sensors/**: distância/proximidade/presença com ruído e injeção/recuperação de falha (SensorError).
- **logistics/**: estoque real por produto/endereço, armazém endereçado com capacidade, pedidos com reserva (falta -> AGUARDANDO_ESTOQUE), cargas/lotes, expedição/carregamento.
- **intelligence/**: otimização *convencional* (A* + heurística de prioridade/distância no escalonador) e detecção de anomalias estatística (z-score) — documentado honestamente: não há ML treinado nem resultados fabricados.
- **dashboard/**: API JSON (`/api/state`, `/api/receber`, `/api/pedido`) + canvas com setores, obstáculos e AMRs.
## Fluxo
Recebimento(A) -> esteira+classificação por categoria(B) -> braço(C) -> AMR transporta ao endereço(D) -> pedido separa do estoque(E) -> carregamento(F) -> expedição(G).
