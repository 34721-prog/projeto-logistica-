import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from simulation.simulation_controller import SimulationController
sim=SimulationController()
sim.receber_carga("SOJA",40); sim.receber_carga("MILHO",30); sim.receber_carga("CAFE",20); sim.receber_carga("TRIGO",25)
HTML=open("static/index.html",encoding="utf-8").read() if __import__('os').path.exists("static/index.html") else "<h1>AgroLogistics AI</h1>"
class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def _send(self,body,ctype="application/json"):
        b=body.encode() if isinstance(body,str) else body
        self.send_response(200); self.send_header("Content-Type",ctype); self.send_header("Content-Length",len(b)); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path=="/": return self._send(HTML,"text/html; charset=utf-8")
        if self.path=="/api/state": sim.passo(); return self._send(json.dumps(sim.estado()))
        if self.path.startswith("/api/receber"):
            from urllib.parse import urlparse,parse_qs; q=parse_qs(urlparse(self.path).query)
            try: sim.receber_carga(q.get("produto",["SOJA"])[0], int(q.get("qtd",["10"])[0])); return self._send(json.dumps({"ok":True}))
            except Exception as e: return self._send(json.dumps({"ok":False,"erro":str(e)}))
        if self.path.startswith("/api/pedido"):
            from urllib.parse import urlparse,parse_qs; q=parse_qs(urlparse(self.path).query)
            try:
                r=sim.processar_pedido(q.get("cliente",["Cliente"])[0], {q.get("produto",["SOJA"])[0]:int(q.get("qtd",["5"])[0])})
                return self._send(json.dumps({"ok":r["ok"],"faltas":r.get("faltas",{})}))
            except Exception as e: return self._send(json.dumps({"ok":False,"erro":str(e)}))
        self.send_response(404); self.end_headers()
def serve(host="0.0.0.0", port=8000):
    print(f"Dashboard em http://{host}:{port}"); HTTPServer((host,port),H).serve_forever()
