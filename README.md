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

### OBS<sub>1</sub>: Para entrarem no ambiente de desenvolvimento, repitam o 2º passo:
### OBS<sub>2</sub>: Caso necessitem adicionar alguma nova biblioteca ao projeto utilizem:
```
pip install -r requirements.txt
pip freeze > requirements.txt
```

# Tópicos do Notebook
> - Imports 
> - Arrays e Operações Vetorizadas
> - Estatísticas Descritivas
> - Correlações
> - Pequenos Exemplos com Dados Reais
> - Visualização de Dados