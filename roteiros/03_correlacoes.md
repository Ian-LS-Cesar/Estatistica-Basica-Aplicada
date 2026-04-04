# Roteiro — Aula 3: Correlação linear (Pearson)

**Módulo 2 · Desbravadores do Ciberespaço** · Duração alvo: 10–15 min · Base: `Projeto.ipynb` → *Correlações*

---

## Abertura (30–45 s)

- “Duas coisas sobem juntas — isso **prova** que uma causa a outra?” → Não.

## Objetivos (30 s)

- Interpretar coeficiente de Pearson entre -1 e 1.
- Ler matriz `np.corrcoef`.
- Opcional: mencionar `pearsonr` e o que é um p-valor sem virar aula de inferência.

## Demonstração (6–10 min)

1. Vetores `x` e `y` quase lineares; matriz 2×2 e extrair `R[0,1]`.
2. `stats.pearsonr`: coeficiente e p-valor — frase: “em projetos grandes, interpretação com cautela”.
3. Terceiro exemplo com ruído: correlação mais fraca.

## Ênfase ética/conceitual (90 s)

- Correlação ≠ causalidade; confundidores; exemplo do sorvete e afogamentos (verbal, curto).

## Fechamento (45 s)

- Próximo: aplicar isso a um CSV no notebook.

---

## Checklist pós-gravação (Equipe E)

- [ ] Gráfico de dispersão citado como “virá na aula de Matplotlib” se não mostrar ainda.
- [ ] Áudio claro nos números da matriz (falar devagar).
