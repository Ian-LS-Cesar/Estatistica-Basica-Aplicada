# Módulo 2 — Estatística básica aplicada (NumPy, SciPy, Matplotlib)

**Curso:** Python para Ciência de Dados (CCEX) · **Disciplina:** Ciência dos Dados (T326) — UNIFOR · **Equipe:** Desbravadores do Ciberespaço

Este repositório concentra o material do **Módulo 2** (arrays, estatísticas descritivas, correlações, exemplo com dados reais e visualização com Matplotlib). O notebook principal é `[Projeto.ipynb](Projeto.ipynb)`. Roteiros para gravação das aulas estão em `[roteiros/](roteiros/)`.

---

## Trilha sugerida (aluno)

1. Configurar o ambiente (seção abaixo).
2. Abrir `Projeto.ipynb` e seguir a ordem: Imports → Arrays → **Indexação** → Estatísticas descritivas → Correlações → Dados reais → Visualização → Exercícios.
3. Resolver os exercícios; conferir o gabarito ao final do notebook (tente antes sem olhar).

**Pré-requisitos:** conceitos do Módulo 1 (variáveis, listas, funções, fluxo básico em Python).

---

## Como rodar o ambiente

1. Crie um ambiente virtual:

```text
python -m venv .venv
```

1. Ative o ambiente:

**Windows (PowerShell):** `.\.venv\Scripts\activate.ps1`  
**Windows (cmd):** `.venv\Scripts\activate`  
**macOS/Linux:** `source .venv/bin/activate`

1. Instale as dependências:

```text
pip install -r requirements.txt
```

**Python:** use **3.11 ou superior** (3.12+ recomendado). O arquivo `requirements.txt` usa versões compatíveis com essa faixa.

**Reprodutibilidade:** com o ambiente ativado, após `pip install nbconvert`, você pode validar o notebook com:

```text
jupyter nbconvert --execute --to notebook Projeto.ipynb --output /tmp/Projeto_validado.ipynb
```

(No Windows, troque `/tmp/` por uma pasta temporária local.)

1. Inicie o Jupyter e abra `Projeto.ipynb`:

```text
python -m ipykernel install --user --name=estatistica-modulo2
jupyter notebook Projeto.ipynb
```

*(O nome do kernel é opcional; pode abrir o notebook com o interpretador do `.venv` diretamente no VS Code/Cursor.)*

---

## Figuras didáticas (`img/`)

Imagens estáticas (PNG) referenciadas no `Projeto.ipynb` para reforçar conceitos no GitHub: indexação 1D, ideia de broadcasting e intuição da correlação de Pearson. Se clonar o repositório e as imagens não aparecerem, gere-as com:

```text
python tools/gerar_figuras_notebook.py
```

## Dados (`data/`)


| Arquivo                                        | Descrição                                                                                                                                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `[data/vendas_loja.csv](data/vendas_loja.csv)` | Dados **sintéticos** de exemplo (12 semanas): gasto em mídias sociais (mil R$), visitantes à loja e vendas (mil R$). Uso exclusivamente didático; não representa empresa real. |


Se a **Equipe E** definir outro local ou nomenclatura para datasets no repositório unificado do curso, ajuste os caminhos no notebook para manter a reprodutibilidade.

---

## Integração com a Equipe E (checklist)

Use esta lista nos checkpoints com o professor e com a equipe de integração. Marque itens quando recebidos ou concluídos.

- Template oficial de **notebook** (cabeçalho, células obrigatórias, estilo).
- Template de **slides** (se obrigatório para o módulo).
- **Checklist de vídeo** (resolução, formato, intro/outro, legendas, nome de arquivo).
- **Estrutura de pastas** e convenção de nomes no repositório global do curso.
- Prazo para **pull request** ou envio do pacote final (notebooks + `data/` + links).
- **Playlist:** títulos padronizados e descrições com links para este repositório.

**Modelo de report em aula de acompanhamento:** “Feito: … | Em andamento: … | Bloqueado: … (dependência: Equipe E / outro) | Próximos passos até …”

---

## Dreamshaper e divulgação

- **Dreamshaper:** registre planejamento, execução (entregas, reuniões, gravações) e **reflexão** sobre a ação de extensão. Sem o registro completo, a extensão pode não ser validada (conforme orientação do projeto na disciplina).
- **Divulgação:** o curso é público no YouTube; quando a Equipe E divulgar o calendário e os materiais de campanha, participe compartilhando o link da playlist e deste repositório nos canais combinados com a turma.

---

## Repositório e links da equipe

- **GitHub (este repo):** *[https://github.com/Ian-LS-Cesar/Estatistica-Basica-Aplicada.git](https://github.com/Ian-LS-Cesar/Estatistica-Basica-Aplicada.git)*

---

## Tópicos do notebook

- Imports  
- Arrays e operações vetorizadas  
- Indexação, seleção e filtro em NumPy *(conteúdo pedido pelo Prof. Caio)*  
- Estatísticas descritivas  
- Correlações  
- Pequenos exemplos com dados reais  
- Visualização de dados (vários tipos de gráfico Matplotlib)  
- Exercícios de fixação e gabarito

### Feedback do professor (abril/2026)

Refletido no `Projeto.ipynb`: textos e figuras em `img/`, maior espaçamento nos blocos de código, seção **Indexação, seleção e filtro**, e gráficos adicionais (**barras, boxplot e heatmap**, além de linha, dispersão e histograma). Para regenerar os PNGs: `python tools/gerar_figuras_notebook.py`. Para reaplicar o patch do notebook a partir do repositório base: `python tools/aplicar_feedback_notebook.py` (uso interno; o notebook versionado já contém o resultado).