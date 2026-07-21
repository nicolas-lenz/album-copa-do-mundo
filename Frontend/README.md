# Álbum Copa do Mundo

Este projeto é um álbum digital interativo sobre a história da Copa do Mundo FIFA, cobrindo desde a primeira edição de 1930 até a Copa de 2026.

## Objetivo

O objetivo principal do projeto é apresentar um álbum estilizado com capítulos sobre maiores artilheiros, lendas do torneio, finais históricas, países-sede, recordes e curiosidades da Copa do Mundo.

## Arquivos principais

### `index.html`

- Define a estrutura HTML do álbum.
- Contém a capa, páginas com categorias da Copa do Mundo e a contracapa.
- Inclui botões de navegação e controle de som.
- Importa o estilo do projeto (`style.css`) e a lógica (`app.js`).
- Carrega a biblioteca `page-flip` para o efeito de virar páginas.

### `style.css`

- Estiliza o visual do álbum, incluindo a capa, páginas internas e contracapa.
- Cria o layout dos slots de figurinha e seus estados visuais.
- Adiciona efeitos visuais como sombras, gradientes, tipografia glitch e animações.
- Ajusta a interface para diferentes tamanhos de tela com responsividade.

### `app.js`

- Inicializa a biblioteca `St.PageFlip` para ativar o efeito de livro.
- Implementa a lógica de navegação entre páginas por botões, teclado e arrasto/touch.
- Mantém o layout de álbum com slots de figurinha prontos para conteúdo.
- Gera um som de virada de página usando a Web Audio API.
- Permite silenciar ou ativar os efeitos sonoros.

## Como usar

1. Abra o arquivo `index.html` em um navegador ou sirva o projeto com um servidor local.
2. O álbum exibirá a capa e as páginas internas com o tema da Copa do Mundo.
3. Clique nas setas ou use as teclas de seta para navegar pelas páginas.
4. Use o botão de som para alternar os efeitos sonoros.
5. O álbum contém conteúdo de exemplo em cada figurinha, sem carregar imagens automaticamente.

## Observações

- O projeto exibe um álbum com slots de figurinha prontos e textos descritivos em cada card.
- O backend não precisa ser executado para visualizar o álbum.
