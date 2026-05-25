import requests, time

GITHUB_PAGES_URL = "https://tiagofiorilli.github.io/qrcode-reader/index.html"
LOCAL_FILE = "index.html"

def ler_arquivo_local(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read().strip()

def ler_arquivo_remoto(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text.strip()
        else:
            return ""
    except:
        return ""

def main():
    local = ler_arquivo_local(LOCAL_FILE)

    while True:
        remoto = ler_arquivo_remoto(GITHUB_PAGES_URL)
        if remoto and local == remoto:
            print("✅ O GitHub Pages já está atualizado com a versão local!")
            break
        else:
            print("⌛ Ainda está com a versão antiga... verificando novamente em 30s.")
            time.sleep(30)

if __name__ == "__main__":
    main()
