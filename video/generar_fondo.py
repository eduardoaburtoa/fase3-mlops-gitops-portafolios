"""Build eight offline recording slides from versioned text and existing figures."""
from pathlib import Path
import json,html,base64
R=Path(__file__).resolve().parents[1]
def image(name):
    data=(R/'evidencias'/name).read_bytes()
    return 'data:image/png;base64,'+base64.b64encode(data).decode()
def build():
    slides=json.loads((R/'video/laminas.json').read_text());blocks=[]
    assert len(slides)==8
    for n,s in enumerate(slides,1):
        points=''.join('<li>'+html.escape(x)+'</li>' for x in s['points'])
        blocks.append(f'<section><small>VÉRTICE AI · FASE III · {n}/8</small><h1>{html.escape(s["title"])}</h1><ul>{points}</ul><img src="{image(s["image"])}"><footer>Eduardo Aburto Angulo · Evidencia académica / proyecciones identificadas</footer></section>')
    output='''<!doctype html><html lang="es"><meta charset="utf-8"><title>Fase III · Fondo de entrevista</title><style>body{margin:0;background:#072146;color:white;font:24px Arial}section{display:none;padding:4vh 5vw;height:90vh;box-sizing:border-box}section.active{display:block}small{color:#5BBEFF}h1{font-size:42px;max-width:85%;margin:20px 0}li{margin:12px 0}img{object-fit:contain;object-position:left top;width:68vw;height:42vh;background:white}footer{position:fixed;bottom:18px;font-size:16px;color:#bde8ff}@media print{section,section.active{display:block;height:95vh;page-break-after:always}footer{position:static}body{-webkit-print-color-adjust:exact;print-color-adjust:exact}}</style>'''+''.join(blocks)+'''<script>let n=0;const s=[...document.querySelectorAll('section')];function show(){s.forEach((e,i)=>e.classList.toggle('active',i===n));}document.onkeydown=e=>{if(e.key==='ArrowRight')n=Math.min(7,n+1);if(e.key==='ArrowLeft')n=Math.max(0,n-1);show()};show();</script></html>'''
    p=R/'video/fondo_presentacion.html';p.write_text(output);print(p)
if __name__=='__main__':build()
