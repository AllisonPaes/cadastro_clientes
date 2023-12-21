# cadastro_clientes

Construção de uma aplicação para o cadastro de clientes, conexão entre bibliotecas pandas com o banco de dados.

## Pré-requisitos

- Python (3.10)
- Bibliotecas: pandas, sqlite3 (instaláveis via `pip install pandas sqlite3`)

## Instalação

1. Clone o repositório: `git clone https://github.com/AllisonPaes/cadastro_clientes.git`
2. Navegue até o diretório do projeto: `cd cadastro_clientes`
3. Instale as dependências: `pip install -r requirements.txt`

## Configuração

1. Realizando um procedimento para criar a aplicação. O procedimento é o mesmo tanto para Mac quanto para Win.
2. Inicie instalando o pacote chamado"pyinstaller". Assim, vamos até o prompt de comando com privilégios de user root. Realize a instalação:pip install pyinstaller
3. Em seguida, entre no diretório onde foram instalados os scripts da nossa aplicação. Utilize o comando cd (current directory) para isso. (cd c:\nome_do_seu_diretório_1\nome_do_se_ddiretório_2/nome_da_aplicação)
4.E por fim, utilize o pyinstaller para criar o arquivo executável. (pyinstaller --onefile --windowed --noconsole aplicacao.py)
5.Resultado: Temos um arquivo (Aplicação), um banco de dados clientes uma interface gráfica (GUI) e o Backend (estes códigos são processos internos da aplicação, operam fora do escopo do usuário, a execução deste processo deve ser transparente para quem utiliza a aplicação.)


## Estrutura do Projeto

- `janela.py`: Script principal que inicia o aplicativo.
- `database.db`: Arquivo do banco de dados SQLite.
- `app/`: Pasta contendo os arquivos relacionados à interface do cadastro de clientes.
- `scripts/`: Scripts auxiliares, se houver.

## Contribuição

Contribuições são bem-vindas! Abra um problema (issue) ou envie um pull request.





