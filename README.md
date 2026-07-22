# 🏆 Álbum Virtual da Copa do Mundo

Um álbum digital interativo de figurinhas da Copa do Mundo, desenvolvido para reunir história, jogadores, seleções e momentos marcantes do maior torneio de futebol do mundo.

O projeto possui uma interface de álbum com páginas interativas, sistema de figurinhas carregadas por uma API própria e integração entre Frontend e Backend.

---

## 🚀 Tecnologias utilizadas

### Frontend
- HTML5
- CSS3
- JavaScript
- St.PageFlip (efeito de virar páginas)

### Backend
- Python
- FastAPI
- Uvicorn

---

## 📂 Estrutura do projeto

```text
album-copa-do-mundo/
│
├── Backend/
│   ├── main.py
│   └── figurinhas/
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

---

## 📚 Sobre o projeto

Projeto desenvolvido durante a **Imersão Arquitetura Web com IA da Alura**, aplicando conceitos de desenvolvimento web, criação de APIs e integração entre frontend e backend.

O objetivo foi criar um álbum virtual interativo inspirado nos tradicionais álbuns de figurinhas da Copa do Mundo.

---

## ⚙️ Como executar

## Backend

Entre na pasta do backend:

```bash
cd Backend
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn main:app --reload
```

O backend estará disponível em:

```text
http://127.0.0.1:8000
```

---

## Frontend

Entre na pasta do frontend:

```bash
cd Frontend
```

Execute um servidor HTTP local:

```bash
python -m http.server 5500
```

Abra `http://127.0.0.1:5500` no navegador. Evite abrir `index.html` com
`file://`, pois navegadores podem impor restrições de origem nesse modo.
Mantenha o backend em execução em `http://localhost:8000`.

---

## 🔌 Endpoints da API

### `GET /`
Retorna uma mensagem inicial da API.

### `GET /figurinhas`
Retorna a lista de todas as figurinhas disponíveis no álbum.

### `GET /figurinhas/{id}`
Busca uma figurinha específica pelo seu ID.

### `GET /figurinhas/total`
Retorna informações sobre o progresso do álbum, como total de figurinhas, figurinhas preenchidas e faltantes.

---

## ✨ Funcionalidades

✅ Álbum digital interativo  
✅ Efeito de virar páginas  
✅ Sistema de figurinhas carregadas pela API  
✅ Organização de figurinhas históricas da Copa do Mundo  
✅ Tema claro e escuro  
✅ Integração entre Frontend e Backend  
✅ API desenvolvida com FastAPI
---

## 📸 Demonstração

*(Adicionar imagens ou GIFs do projeto funcionando)*

---

## 👨‍💻 Autor

Desenvolvido por **Nicolas Lenz da Cunha**

Projeto criado para estudos de desenvolvimento Web, Python, APIs e arquitetura de aplicações.
