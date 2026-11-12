# 🌾 AgroLogistics AI — Central Logística Agrícola Automatizada
Sistema funcional em Python (somente stdlib) que simula de ponta a ponta um centro logístico do agronegócio: recebimento → classificação → separação → armazenamento → preparação → carregamento → expedição, com robôs móveis autônomos (A*), braço robótico, esteiras, sensores com injeção de falha, estoque endereçado, pedidos, expedição e dashboard web em tempo real.

## Executar
```bash
python3 main.py            # demonstração headless completa
python3 main.py --serve    # dashboard: http://localhost:8000
python3 -m unittest discover -s tests -v   # testes
```
## Limitação documentada (BrowserBotics)
O BrowserBotics é uma plataforma web fechada, sem SDK Python instalável/acessível neste ambiente de desenvolvimento (nenhum pacote ou API pública foi encontrado no repositório/ambiente). Portanto a simulação física 3D foi substituída pela melhor alternativa compatível: um motor de simulação próprio em grid 2D (abstração planta-baixa do galpão 3D), com a mesma lógica de robôs, sensores, rotas e logística que seria portada ao BrowserBotics. Detalhes em `docs/architecture.md`.
