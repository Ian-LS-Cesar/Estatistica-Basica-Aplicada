# Roteiro — Aula 4: Dados em CSV só com NumPy

**Módulo 2 · Desbravadores do Ciberespaço** · Duração alvo: 12–18 min · Base: `Projeto.ipynb` → *Pequenos exemplos com dados reais*

---

## Abertura (45 s)

- “No Módulo 3 veremos Pandas; aqui carregamos CSV com **NumPy** para fixar arrays e tipos.”
- Apresentar `data/vendas_loja.csv`: dados sintéticos, 12 semanas, três colunas numéricas.

## Objetivos (30 s)

- `Path` e caminho relativo ao notebook.
- `np.genfromtxt` com `names=True`.
- Extrair colunas nomeadas, montar matriz com `column_stack`.
- Médias, desvios e matriz de correlação entre as três variáveis.

## Demonstração (8–12 min)

1. Conferir `dtype.names` e número de linhas.
2. Converter colunas para `float` com `np.asarray`.
3. Estatísticas por coluna.
4. `corrcoef` com `rowvar=False` e ler pares (gasto × visitas, visitas × vendas, etc.).

## Fechamento (60 s)

- Reforçar leitura do `README` sobre origem sintética dos dados.
- Próxima aula: gráficos para **ver** essas relações.

---

## Checklist pós-gravação (Equipe E)

- [ ] Mostrar na tela o caminho `data/vendas_loja.csv` alinhado ao repositório oficial.
- [ ] Se o repositório mudar de pasta, atualizar roteiro e notebook juntos.
