# Como rodar o ambiente de desenvolvimento do projeto e baixar dependências?

## 1. Crie um ambiente virtual de desenvolvimento com o seguinte comando no terminal:

`
python -m venv .nome_ambiente
`

## 2. Execute o comando a seguir dependendo dependendo de onde estiver executando o seu projeto:

### Windows (Prompt de Comando):
`
.nome_ambiente\Scripts\activate
`
### Windows (PowerShell):
`
.\.nome_ambiente\Scripts\activate.ps1
`
### macOS/Linux:
`
source .nome_ambiente/bin/activate
`
## 3. Instale as dependências executando:
`
pip install -r requirements.txt
`