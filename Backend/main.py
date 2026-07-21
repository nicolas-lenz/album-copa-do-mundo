import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Cria a aplicação FastAPI
app = FastAPI()

# Configuração do Middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definição dos caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de todas as 30 figurinhas da Copa do Mundo.
# Todas estão ativas porque seus respectivos arquivos de imagem existem na pasta figurinhas/
figurinhas = [
    {
        "id": 1,
        "nome": "Lionel Messi",
        "categoria": "ARTILHEIROS",
        "imagem_url": "/figurinhas/1/imagem/01-messi2026.webp"
    },
    {
        "id": 2,
        "nome": "Kylian Mbappé",
        "categoria": "ARTILHEIROS",
        "imagem_url": "/figurinhas/2/imagem/02-mbappe.avif"
    },
    {
        "id": 3,
        "nome": "Miroslav Klose",
        "categoria": "ARTILHEIROS",
        "imagem_url": "/figurinhas/3/imagem/03-klose.jpg"
    },
    {
        "id": 4,
        "nome": "Ronaldo Nazário",
        "categoria": "ARTILHEIROS",
        "imagem_url": "/figurinhas/4/imagem/04-ronaldonazario.webp"
    },
    {
        "id": 5,
        "nome": "Gerd Müller",
        "categoria": "ARTILHEIROS",
        "imagem_url": "/figurinhas/5/imagem/05-gerd-muller.webp"
    },
    {
        "id": 6,
        "nome": "Pelé",
        "categoria": "LENDAS",
        "imagem_url": "/figurinhas/6/imagem/06-pelé.jpg"
    },
    {
        "id": 7,
        "nome": "Diego Maradona",
        "categoria": "LENDAS",
        "imagem_url": "/figurinhas/7/imagem/07-maradona.jpg"
    },
    {
        "id": 8,
        "nome": "Franz Beckenbauer",
        "categoria": "LENDAS",
        "imagem_url": "/figurinhas/8/imagem/08-fran-beckenbauer.webp"
    },
    {
        "id": 9,
        "nome": "Johan Cruyff",
        "categoria": "LENDAS",
        "imagem_url": "/figurinhas/9/imagem/09-cruyff.webp"
    },
    {
        "id": 10,
        "nome": "Zinedine Zidane",
        "categoria": "LENDAS",
        "imagem_url": "/figurinhas/10/imagem/10-zidane.webp"
    },
    {
        "id": 11,
        "nome": "Uruguai x Argentina (1930)",
        "categoria": "FINAIS",
        "imagem_url": "/figurinhas/11/imagem/11-uruguai-argentina-1930.jpg"
    },
    {
        "id": 12,
        "nome": "Brasil x Uruguai (1950)",
        "categoria": "FINAIS",
        "imagem_url": "/figurinhas/12/imagem/12-uruguai-brazil-1950.jpg"
    },
    {
        "id": 13,
        "nome": "Brasil x Itália (1970)",
        "categoria": "FINAIS",
        "imagem_url": "/figurinhas/13/imagem/13-brazil-italia-1970.webp"
    },
    {
        "id": 14,
        "nome": "Itália x França (2006)",
        "categoria": "FINAIS",
        "imagem_url": "/figurinhas/14/imagem/14-italia-franca-2006.jpg"
    },
    {
        "id": 15,
        "nome": "Argentina x França (2022)",
        "categoria": "FINAIS",
        "imagem_url": "/figurinhas/15/imagem/15-argentina-franca-2022.webp"
    },
    {
        "id": 16,
        "nome": "Uruguai",
        "categoria": "SEDES",
        "imagem_url": "/figurinhas/16/imagem/16-estadio_centenario-1930.jpg"
    },
    {
        "id": 17,
        "nome": "Brasil",
        "categoria": "SEDES",
        "imagem_url": "/figurinhas/17/imagem/17-maracana-brazil.webp"
    },
    {
        "id": 18,
        "nome": "México",
        "categoria": "SEDES",
        "imagem_url": "/figurinhas/18/imagem/18-estadio-azteca.webp"
    },
    {
        "id": 19,
        "nome": "África do Sul",
        "categoria": "SEDES",
        "imagem_url": "/figurinhas/19/imagem/19-africa.webp"
    },
    {
        "id": 20,
        "nome": "Estados Unidos, Canadá e México",
        "categoria": "SEDES",
        "imagem_url": "/figurinhas/20/imagem/20-eua-canada-mex.png"
    },
    {
        "id": 21,
        "nome": "Brasil",
        "categoria": "RECORDES",
        "imagem_url": "/figurinhas/21/imagem/21-pentacampea.jpg"
    },
    {
        "id": 22,
        "nome": "Maior Goleada",
        "categoria": "RECORDES",
        "imagem_url": "/figurinhas/22/imagem/22-hungria-elsalvador.jpg"
    },
    {
        "id": 23,
        "nome": "Mais Partidas",
        "categoria": "RECORDES",
        "imagem_url": "/figurinhas/23/imagem/23-messi-2022.webp"
    },
    {
        "id": 24,
        "nome": "Mais Gols em uma Copa",
        "categoria": "RECORDES",
        "imagem_url": "/figurinhas/24/imagem/24-fontaine.jpg"
    },
    {
        "id": 25,
        "nome": "Gol Mais Rápido",
        "categoria": "RECORDES",
        "imagem_url": "/figurinhas/25/imagem/25-golmaisrapido.jpg"
    },
    {
        "id": 26,
        "nome": "Taça Jules Rimet",
        "categoria": "CURIOSIDADE",
        "imagem_url": "/figurinhas/26/imagem/26-taca-julesrimet.jpg"
    },
    {
        "id": 27,
        "nome": "Taça FIFA",
        "categoria": "CURIOSIDADE",
        "imagem_url": "/figurinhas/27/imagem/27-taca-fifaworldcuptrophy.jpg"
    },
    {
        "id": 28,
        "nome": "Bola Telstar",
        "categoria": "CURIOSIDADE",
        "imagem_url": "/figurinhas/28/imagem/28-bola.jpg"
    },
    {
        "id": 29,
        "nome": "Primeira Copa do Mundo",
        "categoria": "CURIOSIDADE",
        "imagem_url": "/figurinhas/29/imagem/29-cartaz-1930.jpg"
    },
    {
        "id": 30,
        "nome": "Copa do Mundo de 2026",
        "categoria": "CURIOSIDADE",
        "imagem_url": "/figurinhas/30/imagem/30-logo-fifa.webp"
    }
]

# Endpoint para listar todas as figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna a lista de figurinhas ativas.
    """
    return figurinhas

# Endpoint para obter as estatísticas do álbum
@app.get("/figurinhas/total")
def estatisticas_album():
    """
    Retorna estatísticas de figurinhas coladas e restantes.
    """
    total_album = 30
    coladas = len(figurinhas)
    faltam = total_album - coladas
    return {
        "total_album": total_album,
        "coladas": coladas,
        "faltam": faltam
    }

# Endpoint para obter os dados de uma figurinha específica pelo ID
@app.get("/figurinhas/{id}")
def obter_figurinha(id: int):
    """
    Busca e retorna uma figurinha pelo seu ID.
    Retorna erro 404 se o ID não for encontrado.
    """
    for f in figurinhas:
        if f["id"] == id:
            return f
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")

# Endpoint para servir a imagem da figurinha pelo seu ID usando glob.
# Aceita tanto a rota antiga "/figurinhas/{id}/imagem" quanto a rota contendo o nome do arquivo "/figurinhas/{id}/imagem/{filename}"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int, filename: str = None):
    """
    Serves the image file for a given figurine ID.
    If `filename` is provided, it attempts to serve that specific file.
    Otherwise, it returns the first image found in the figurine's image directory.
    """
    # Busca arquivos que começam com o ID formatado com dois dígitos (ex.: 01*, 02*, …)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}*")
    arquivos = glob.glob(padrao)
    if filename:
        # When a specific filename is requested, look for it directly in the base images folder
        caminho_imagem = os.path.join(PASTA_IMAGENS, filename)
        if not os.path.isfile(caminho_imagem):
            raise HTTPException(status_code=404, detail="Imagem não encontrada")
        return FileResponse(caminho_imagem)
    # No specific filename: use the files found by the initial glob (padrao)
    # (arquivos already contains matching images)
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    caminho_imagem = arquivos[0]
    return FileResponse(caminho_imagem)
