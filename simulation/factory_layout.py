import config
def layout(): return config.SECTORS
def ponto_setor(sigla):
    x,y,w,h=config.SECTORS[sigla]["rect"]; return (x+w//2, y+h//2)
