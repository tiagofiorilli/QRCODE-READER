import json
import qrcode
from pathlib import Path

BASE_DIR = Path(__file__).parent
ARQUIVO_JSON = BASE_DIR / "clientes_bikes.json"
PASTA_SAIDA = BASE_DIR / "qrcodes"

print("Lendo arquivo:", ARQUIVO_JSON)

PASTA_SAIDA.mkdir(exist_ok=True)

with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
    dados = json.load(f)

print("Códigos encontrados:", list(dados.keys()))

for codigo in dados.keys():
    img = qrcode.make(codigo)
    caminho = PASTA_SAIDA / f"{codigo}.png"
    img.save(caminho)
    print(f"QR Code gerado: {caminho}")

print("Finalizado.")