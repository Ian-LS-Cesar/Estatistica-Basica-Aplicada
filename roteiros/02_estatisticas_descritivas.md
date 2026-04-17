# Roteiro — Aula 2: Estatísticas descritivas (NumPy e SciPy)

**Módulo 2 · Desbravadores do Ciberespaço** · Duração alvo: 12–18 min · Base: `Projeto.ipynb` → *Estatísticas descritivas*

---

## Abertura (30–60 s)

- Conectar com a aula 1: “Já temos arrays; agora vamos **resumir** o que há dentro deles.”
- Pergunta rápida: “Média ou mediana — quando uma mente e a outra não?”

## Objetivos (30 s)

- Calcular média, mediana, variância e desvio padrão com NumPy.
- Explicar `ddof` (populacional vs amostral) em uma frase simples.
- Usar percentis e `scipy.stats.describe` como visão geral.

## Demonstração (8–14 min)

1. Gerar amostra com `default_rng` e semente fixa (reprodutibilidade).
2. `np.mean`, `np.median`, `np.var` com `ddof=0` e `ddof=1`, `np.std`.
3. `np.percentile` para Q1 e Q3.
4. `stats.describe`: comentar `minmax`, `nobs`, `skewness`, `kurtosis` sem aprofundar demais.

## Conceito-chave (90 s)

- Média sensível a outliers; mediana mais robusta — exemplo verbal (salários) se não houver tempo de novo código.

## Fechamento (60 s)

- Resumo em três bullets: tendência central, dispersão, percentis.
- Próxima aula: correlação.

---

## Checklist pós-gravação (Equipe E)

- Template de vídeo aplicado.
- Legenda ou cards com definições de variância/desvio se o template pedir.