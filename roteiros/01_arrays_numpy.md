# Roteiro — Aula 1: Arrays NumPy e vetorização

**Módulo 2 · Desbravadores do Ciberespaço** · Duração alvo: 12–18 min · Base: `Projeto.ipynb` → *Arrays e operações vetorizadas*

---

## Abertura (30–60 s)

- Apresentação curta: nome, equipe, módulo.
- Frase-gancho: “Em dados, quase nunca queremos somar um número por vez — queremos operações em lote. O NumPy existe para isso.”

## Objetivos de aprendizagem (30 s)

- Explicar o que é um `ndarray` e por que é mais eficiente que listas para números.
- Mostrar `shape`, `dtype` e operações vetorizadas.
- Mostrar uma máscara booleana e um exemplo mínimo de broadcasting.

## Demonstração no notebook (8–14 min)

1. Criar array a partir de lista; imprimir `shape`, `ndim`, `dtype`.
2. `reshape`: transformar sequência em matriz 3×4.
3. Operações `*`, `**`, `np.sqrt` em cima do vetor inteiro.
4. `sum`, `mean` com e sem `axis` na matriz.
5. Filtrar com `b[b > 6]`.
6. Somar uma “linha” a todas as linhas (broadcasting).

Enquanto codifica: comentar em voz alta **por que** não usar `for` por elemento na maioria dos casos.

## Erros comuns (60–90 s)

- Misturar tipos e cair em `dtype=object` sem perceber.
- Confundir eixo 0 (linhas/colunas dependendo do contexto) — mostrar `axis=0` vs `axis=1` na mesma matriz.

## Fechamento (60 s)

- Recapitular: ndarray + vetorização + eixos.
- Próximo passo: estatísticas descritivas (aula 2).
- Lembrar: repositório com notebook e exercícios.

---

## Checklist pós-gravação (Equipe E)

- [ ] Áudio sem ruído forte; volume estável.
- [ ] Código e fonte legíveis na tela.
- [ ] Intro/outro e nome do arquivo conforme template da Equipe E.
