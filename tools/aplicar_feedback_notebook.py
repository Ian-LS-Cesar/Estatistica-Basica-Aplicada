"""Aplica feedback Prof. Caio ao Projeto.ipynb e limpa saídas (diff menor no Git)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB_PATH = ROOT / "Projeto.ipynb"


def main():
    nb = json.loads(NB_PATH.read_text(encoding="utf-8"))
    cells = nb["cells"]
    by_id = {c.get("id"): i for i, c in enumerate(cells) if c.get("id")}

    def clear_out(c):
        if c.get("cell_type") == "code":
            c["outputs"] = []
            c["execution_count"] = None

    # --- Planejamento (c8fca17b) ---
    i0 = by_id["c8fca17b"]
    s = "".join(cells[i0]["source"])
    s = s.replace(
        "* Produzir gráficos **linha, dispersão e histograma** com rótulos claros.\n",
        "* Produzir gráficos **linha, dispersão, histograma, barras, pizza, boxplot, step e área** com rótulos claros.\n"
        "* Usar **indexação, fatiamento, máscaras e np.where** para selecionar e filtrar dados em arrays.\n",
    )
    s = s.replace(
        "| 1 | Arrays NumPy e vetorização | 12–18 min | Seção *Arrays* |\n",
        "| 1 | Arrays NumPy e vetorização | 12–18 min | Seção *Arrays* |\n"
        "| 1b | Indexação, seleção e filtro | 10–15 min | Seção *Indexação* |\n",
    )
    s = s.replace(
        "| 5 | Matplotlib: linha, dispersão, histograma | 15–20 min | Seção *Visualização* |\n",
        "| 5 | Matplotlib: vários tipos de gráfico | 18–25 min | Seção *Visualização* |\n",
    )
    cells[i0]["source"] = [s]

    # --- Mermaid ---
    cells[by_id["0edd0e81"]]["source"] = [
        "```mermaid\n",
        "graph TD;\n",
        "    A[Estatística Básica Aplicada] --> B[Arrays e Operações Vetorizadas];\n",
        "    A --> B2[Indexação Seleção e Filtro];\n",
        "    A --> C[Estatísticas Descritivas];\n",
        "    A --> D[Correlações];\n",
        "    A --> E[Pequenos Exemplos com Dados Reais];\n",
        "    A --> F[Visualização de Dados];\n",
        "```",
    ]

    # --- Arrays markdown ---
    cells[by_id["3dc5b754"]]["source"] = [
        "## Arrays e operações vetorizadas\n",
        "\n",
        "O **NumPy** oferece o tipo `ndarray`: arranjos **homogêneos** (mesmo `dtype` em todos os elementos) armazenados de forma eficiente. Isso permite **vetorização**: a mesma operação em muitos valores de uma vez, sem um `for` em Python por posição — em geral mais rápido e mais legível.\n",
        "\n",
        "**Por que importa em Ciência de Dados?** Colunas numéricas grandes são a regra; somar, normalizar ou comparar vetores inteiros é rotina. O NumPy delega o trabalho pesado a rotinas compiladas.\n",
        "\n",
        "Conceitos centrais:\n",
        "\n",
        "- **shape**: tamanho ao longo de cada dimensão (ex.: `(5,)` ou `(3, 4)`).\n",
        "- **dtype**: tipo dos elementos; evite `dtype=object` sem necessidade.\n",
        "- **eixos (`axis`)**: em matrizes, `axis=0` agrega sobre linhas (uma estatística por coluna) e `axis=1` sobre colunas.\n",
        "- **broadcasting**: regras para combinar arrays de formas diferentes (ex.: somar um vetor-linha a cada linha de uma matriz).\n",
        "\n",
        "![Ideia de broadcasting](img/broadcasting_conceito.png)\n",
        "\n",
        "Na próxima célula, veja operações vetorizadas e uma máscara booleana antes da seção dedicada a indexação.\n",
    ]

    # --- Arrays code ---
    ic = by_id["b3ca1db1"]
    cells[ic]["source"] = [
        "# --- Criar arrays e inspecionar metadados ---\n",
        "lista = [1, 2, 3, 4, 5]\n",
        "a = np.array(lista, dtype=np.float64)\n",
        "\n",
        "print(\"array:\", a)\n",
        "print(\"shape:\", a.shape, \"| ndim:\", a.ndim, \"| dtype:\", a.dtype)\n",
        "\n",
        "\n",
        "# --- Matriz 2D e reshape ---\n",
        "b = np.arange(12).reshape(3, 4)\n",
        "print(\"\\nmatriz 3x4:\\n\", b)\n",
        "\n",
        "\n",
        "# --- Operações vetorizadas (elemento a elemento) ---\n",
        "print(\"\\nOperações vetorizadas (elemento a elemento):\")\n",
        "print(\"a * 10:\", a * 10)\n",
        "print(\"a ** 2:\", a ** 2)\n",
        "print(\"sqrt(a):\", np.sqrt(a))\n",
        "\n",
        "\n",
        "# --- Agregações por eixo ---\n",
        "print(\"\\nAgregações ao longo de eixos:\")\n",
        "print(\"soma total de b:\", b.sum())\n",
        "print(\"soma por coluna (eixo 0):\", b.sum(axis=0))\n",
        "print(\"média por linha (eixo 1):\", b.mean(axis=1))\n",
        "\n",
        "\n",
        "# --- Máscara booleana (filtro sem loop explícito) ---\n",
        "print(\"\\nMáscaras booleanas (filtrar sem loop):\")\n",
        "print(\"elementos > 6:\", b[b > 6])\n",
        "\n",
        "\n",
        "# --- Broadcasting ---\n",
        "print(\"\\nBroadcasting simples:\")\n",
        "linha = np.array([1.0, 0.0, 2.0, 0.0])\n",
        "print(\"b + linha (linha aplicada a cada linha de b):\\n\", b + linha)\n",
    ]
    clear_out(cells[ic])

    # --- Inserir indexação após arrays code ---
    ins = ic + 1
    new_md = {
        "cell_type": "markdown",
        "id": "numpy-indexacao-md",
        "metadata": {},
        "source": [
            "## Indexação, seleção e filtro em NumPy\n",
            "\n",
            "**Indexação** escolhe posições; **fatiamento** (`início:fim:passo`) pega intervalos; **máscaras booleanas** filtram por condição; **`np.where`** devolve valores escolhidos por condição, de forma vetorizada.\n",
            "\n",
            "Em 2D: `M[i, j]` é um elemento; `M[i]` é a linha `i`; `M[:, k]` é a coluna `k`. Índices negativos contam do final (`-1` = último).\n",
            "\n",
            "![Resumo visual 1D](img/indexacao_numpy_1d.png)\n",
            "\n",
            "Com **índices avançados** (listas ou arrays de inteiros), `M[[0, 2], [1, 4]]` retorna os elementos nas posições `(0,1)` e `(2,4)` — par a par.\n",
        ],
    }
    new_code = {
        "cell_type": "code",
        "execution_count": None,
        "id": "numpy-indexacao-code",
        "metadata": {},
        "outputs": [],
        "source": [
            "# --- Fatiamento e índices em 1D ---\n",
            "arr = np.array([10, 20, 30, 40, 50])\n",
            "\n",
            "print(\"elemento 0:\", arr[0])\n",
            "print(\"último:\", arr[-1])\n",
            "print(\"índices 1 até 3 (exclusivo):\", arr[1:4])\n",
            "print(\"passo 2:\", arr[::2])\n",
            "\n",
            "\n",
            "# --- Máscara e np.where ---\n",
            "mascara = arr > 25\n",
            "\n",
            "print(\"\\nmáscara:\", mascara)\n",
            "print(\"filtrados:\", arr[mascara])\n",
            "\n",
            "rotulo = np.where(arr >= 30, \"alto\", \"baixo\")\n",
            "print(\"\\nrótulos (np.where):\", rotulo)\n",
            "\n",
            "\n",
            "# --- Matriz: linhas, colunas, bloco ---\n",
            "M = np.arange(24).reshape(4, 6)\n",
            "\n",
            "print(\"\\nM:\\n\", M)\n",
            "print(\"\\nlinha 2:\", M[2])\n",
            "print(\"coluna 1:\", M[:, 1])\n",
            "print(\"bloco [1:3, 2:5]:\\n\", M[1:3, 2:5])\n",
            "\n",
            "\n",
            "# --- Indexação avançada (pares linha, coluna) ---\n",
            "print(\"\\nM[[0, 2], [1, 4]]:\", M[[0, 2], [1, 4]])\n",
        ],
    }
    cells.insert(ins, new_md)
    cells.insert(ins + 1, new_code)

    by_id = {c.get("id"): i for i, c in enumerate(cells) if c.get("id")}

    cells[by_id["5db4a0a8"]]["source"] = [
        "## Estatísticas descritivas\n",
        "\n",
        "Resumimos dados com **tendência central** (média, mediana), **dispersão** (variância, desvio padrão) e **posição** (quartis, percentis).\n",
        "\n",
        "A **média** é sensível a valores extremos; a **mediana** (valor central ordenado) costuma ser mais **robusta** na presença de outliers. A **variância** e o **desvio padrão** medem o quanto os valores se dispersam em torno da média. Em **amostras**, costuma-se usar `ddof=1` na variância/desvio para o estimador não enviesado.\n",
        "\n",
        "Os **percentis** respondem perguntas do tipo: “abaixo de qual valor ficam 90% dos dados?”. O pacote **SciPy** oferece `scipy.stats.describe` como visão compacta de várias estatísticas.\n",
    ]

    ie = by_id["0b281e84"]
    cells[ie]["source"] = [
        "# --- Amostra simulada ---\n",
        "amostra = rng.normal(loc=50.0, scale=8.0, size=200)\n",
        "\n",
        "\n",
        "# --- Tendência e dispersão (NumPy) ---\n",
        "media = float(np.mean(amostra))\n",
        "mediana = float(np.median(amostra))\n",
        "variancia = float(np.var(amostra, ddof=0))\n",
        "variancia_amostral = float(np.var(amostra, ddof=1))\n",
        "dp = float(np.std(amostra, ddof=1))\n",
        "\n",
        "print(f\"Média: {media:.3f}\")\n",
        "print(f\"Mediana: {mediana:.3f}\")\n",
        "print(f\"Variância populacional (ddof=0): {variancia:.3f}\")\n",
        "print(f\"Variância amostral (ddof=1): {variancia_amostral:.3f}\")\n",
        "print(f\"Desvio padrão amostral (ddof=1): {dp:.3f}\")\n",
        "\n",
        "\n",
        "# --- Quartis ---\n",
        "q25, q75 = np.percentile(amostra, [25, 75])\n",
        "print(f\"Q1 (25%): {q25:.3f} | Q3 (75%): {q75:.3f}\")\n",
        "\n",
        "\n",
        "# --- SciPy describe ---\n",
        "desc = stats.describe(amostra)\n",
        "print(\"\\nscipy.stats.describe:\")\n",
        "print(desc)\n",
    ]
    clear_out(cells[ie])

    cells[by_id["4977ffdb"]]["source"] = [
        "## Correlações\n",
        "\n",
        "A **correlação linear de Pearson** mede associação **linear** entre duas variáveis (coeficiente entre -1 e 1). Valores próximos de ±1 indicam alinhamento quase perfeito a uma reta; próximo de 0 indica pouca relação **linear** (ainda pode haver padrão curvo — o gráfico de dispersão ajuda).\n",
        "\n",
        "![Intuição do coeficiente r](img/correlacao_pearson_intuicao.png)\n",
        "\n",
        "**Correlação não implica causalidade.** Duas séries podem subir juntas por um terceiro fator não medido.\n",
        "\n",
        "`numpy.corrcoef` monta a matriz entre variáveis; `scipy.stats.pearsonr` retorna o par (r, p-valor) para testar hipótese sobre correlação nula em amostras — use interpretação cautelosa fora de um curso formal de inferência.\n",
    ]

    id_corr = by_id["de453721"]
    cells[id_corr]["source"] = [
        "# --- Vetores quase colineares ---\n",
        "x = np.array([1, 2, 3, 4, 5, 6], dtype=float)\n",
        "y = np.array([2.1, 2.9, 4.2, 4.8, 6.0, 7.1])\n",
        "\n",
        "R = np.corrcoef(x, y)\n",
        "print(\"Matriz 2x2 (Pearson):\\n\", R)\n",
        "print(f\"\\nr entre x e y: {R[0, 1]:.4f}\")\n",
        "\n",
        "\n",
        "# --- SciPy ---\n",
        "r_stat, p_valor = stats.pearsonr(x, y)\n",
        "print(f\"pearsonr: r = {r_stat:.4f}, p = {p_valor:.4g}\")\n",
        "\n",
        "\n",
        "# --- Ruído reduz correlação ---\n",
        "ruido = rng.standard_normal(len(x))\n",
        "z = 0.05 * x + ruido\n",
        "print(\"\\ncorrelação x e z:\", float(np.corrcoef(x, z)[0, 1]))\n",
    ]
    clear_out(cells[id_corr])

    cells[by_id["df3d4f6f"]]["source"] = [
        "## Pequenos exemplos com dados reais\n",
        "\n",
        "Carregamos o CSV didático **`data/vendas_loja.csv`** só com **NumPy** (`np.genfromtxt`). São **12 semanas** de dados **sintéticos**: gasto em mídias, visitantes e vendas. Detalhes e licença de uso estão no `README.md`.\n",
        "\n",
        "**Pipeline:** (1) ler e conferir nomes das colunas; (2) extrair vetores `float`; (3) calcular médias, desvios e matriz de correlação; (4) na seção seguinte, **visualizar** para validar o que os números sugerem.\n",
    ]

    id_csv = by_id["b24c4a36"]
    cells[id_csv]["source"] = [
        "# --- Localizar CSV ---\n",
        "base = Path.cwd()\n",
        "csv_path = base / \"data\" / \"vendas_loja.csv\"\n",
        "\n",
        "if not csv_path.exists():\n",
        "    csv_path = Path(\"vendas_loja.csv\")\n",
        "\n",
        "\n",
        "# --- Leitura com cabeçalho ---\n",
        "raw = np.genfromtxt(csv_path, delimiter=\",\", names=True, dtype=None, encoding=\"utf-8\")\n",
        "print(\"Colunas:\", raw.dtype.names)\n",
        "print(\"Linhas:\", raw.shape[0])\n",
        "\n",
        "\n",
        "# --- Colunas numéricas ---\n",
        "gasto = np.asarray(raw[\"gasto_midias_sociais_mil_reais\"], dtype=float)\n",
        "visitas = np.asarray(raw[\"num_visitantes_loja\"], dtype=float)\n",
        "vendas = np.asarray(raw[\"vendas_mil_reais\"], dtype=float)\n",
        "\n",
        "matriz = np.column_stack([gasto, visitas, vendas])\n",
        "print(\"\\nPrimeiras 3 linhas:\\n\", matriz[:3])\n",
        "\n",
        "\n",
        "# --- Descritivas ---\n",
        "print(\"\\nMédias:\", matriz.mean(axis=0))\n",
        "print(\"Desvios (amostral, ddof=1):\", matriz.std(axis=0, ddof=1))\n",
        "\n",
        "\n",
        "# --- Correlações ---\n",
        "R_all = np.corrcoef(matriz, rowvar=False)\n",
        "labels = [\"gasto_midias\", \"visitantes\", \"vendas\"]\n",
        "print(\"\\nCorrelação (Pearson), arredondada:\")\n",
        "print(np.round(R_all, 3))\n",
        "print(\"Variáveis:\", labels)\n",
    ]
    clear_out(cells[id_csv])

    cells[by_id["4684219c"]]["source"] = [
        "## Visualização de dados (Matplotlib)\n",
        "\n",
        "O **Matplotlib** é a base mais comum para gráficos **estáticos** em Python. Boas práticas: título claro, eixos com unidades, grade leve quando ajuda, legenda se houver mais de uma série.\n",
        "\n",
        "Além de **linha**, **dispersão** e **histograma**, este módulo mostra:\n",
        "\n",
        "- **Barras** (`bar` / `barh`): comparar categorias ou períodos.\n",
        "- **Boxplot**: mediana, quartis e outliers — útil para comparar dispersão entre grupos.\n",
        "- **Pizza (`pie`)**: proporções de um todo. **Uso didático:** funciona com **poucas** fatias; com muitas categorias, prefira barras.\n",
        "- **Step**: séries que mudam em degraus.\n",
        "- **`fill_between`**: destacar área sob curva ou entre duas curvas.\n",
        "\n",
        "Primeiro uma grade **2×3** com linha, dispersão, histograma, barras, barras horizontais e boxplot; depois uma linha com pizza, step e área.\n",
    ]

    viz_src = [
        "semanas = np.arange(1, len(vendas) + 1)\n",
        "\n",
        "\n",
        "fig, axes = plt.subplots(2, 3, figsize=(13, 7))\n",
        "ax = axes.ravel()\n",
        "\n",
        "\n",
        "# --- Linha ---\n",
        "ax[0].plot(semanas, vendas, marker=\"o\", color=\"#2563eb\")\n",
        "ax[0].set_title(\"Linha — vendas por semana\")\n",
        "ax[0].set_xlabel(\"Semana\")\n",
        "ax[0].set_ylabel(\"Vendas (mil R$)\")\n",
        "ax[0].grid(True, alpha=0.3)\n",
        "\n",
        "\n",
        "# --- Dispersão ---\n",
        "ax[1].scatter(visitas, vendas, color=\"#16a34a\", edgecolors=\"black\", linewidths=0.4)\n",
        "ax[1].set_title(\"Dispersão — visitantes × vendas\")\n",
        "ax[1].set_xlabel(\"Visitantes\")\n",
        "ax[1].set_ylabel(\"Vendas (mil R$)\")\n",
        "ax[1].grid(True, alpha=0.3)\n",
        "\n",
        "\n",
        "# --- Histograma ---\n",
        "ax[2].hist(amostra, bins=15, color=\"#9333ea\", edgecolor=\"white\")\n",
        "ax[2].set_title(\"Histograma — amostra simulada\")\n",
        "ax[2].set_xlabel(\"Valor\")\n",
        "ax[2].set_ylabel(\"Frequência\")\n",
        "\n",
        "\n",
        "# --- Barras ---\n",
        "ax[3].bar(semanas, vendas, color=\"#ea580c\", edgecolor=\"white\")\n",
        "ax[3].set_title(\"Barras — vendas por semana\")\n",
        "ax[3].set_xlabel(\"Semana\")\n",
        "ax[3].set_ylabel(\"Vendas (mil R$)\")\n",
        "\n",
        "\n",
        "# --- Barras horizontais ---\n",
        "ax[4].barh(semanas, gasto, color=\"#0891b2\", edgecolor=\"white\")\n",
        "ax[4].set_title(\"Barras horiz. — gasto em mídias\")\n",
        "ax[4].set_xlabel(\"Gasto (mil R$)\")\n",
        "ax[4].set_ylabel(\"Semana\")\n",
        "\n",
        "\n",
        "# --- Boxplot (visitas em escala reduzida para comparar no mesmo eixo) ---\n",
        "dados_box = [gasto, visitas / 10.0, vendas]\n",
        "ax[5].boxplot(dados_box, tick_labels=[\"Gasto\", \"Visit./10\", \"Vendas\"])\n",
        "ax[5].set_title(\"Boxplot — dispersão (visitas ÷10)\")\n",
        "ax[5].grid(True, axis=\"y\", alpha=0.3)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "\n",
        "# --- Pizza, step, área (segunda figura) ---\n",
        "fig2, axb = plt.subplots(1, 3, figsize=(13, 3.8))\n",
        "\n",
        "partes = np.array([float(vendas[:4].sum()), float(vendas[4:8].sum()), float(vendas[8:].sum())])\n",
        "labels_pie = [\"Sem 1–4\", \"Sem 5–8\", \"Sem 9–12\"]\n",
        "axb[0].pie(partes, labels=labels_pie, autopct=\"%1.1f%%\", startangle=90)\n",
        "axb[0].set_title(\"Pizza — % das vendas por bloco de semanas\")\n",
        "\n",
        "axb[1].step(semanas, vendas, where=\"mid\", color=\"#7c3aed\")\n",
        "axb[1].set_title(\"Step — vendas\")\n",
        "axb[1].set_xlabel(\"Semana\")\n",
        "axb[1].set_ylabel(\"Vendas\")\n",
        "axb[1].grid(True, alpha=0.3)\n",
        "\n",
        "axb[2].fill_between(semanas, gasto, alpha=0.35, color=\"#0d9488\", label=\"Gasto\")\n",
        "axb[2].plot(semanas, gasto, color=\"#115e59\", linewidth=1.5)\n",
        "axb[2].set_title(\"Área — gasto (fill_between)\")\n",
        "axb[2].set_xlabel(\"Semana\")\n",
        "axb[2].set_ylabel(\"Gasto (mil R$)\")\n",
        "axb[2].legend()\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
    ]

    id_viz = by_id["805f8dbd"]
    cells[id_viz]["source"] = viz_src
    clear_out(cells[id_viz])

    # Imports: espaçamento
    cells[by_id["95d7e570"]]["source"] = [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from scipy import stats\n",
        "from pathlib import Path\n",
        "\n",
        "\n",
        "rng = np.random.default_rng(seed=42)\n",
    ]
    clear_out(cells[by_id["95d7e570"]])

    id_gab = by_id["gabarito-code"]
    cells[id_gab]["source"] = [
        "# --- Gabarito (referência) ---\n",
        "\n",
        "ex1 = np.arange(100)\n",
        "assert ex1.sum() == 4950\n",
        "assert np.isclose(ex1.mean(), 49.5)\n",
        "print(\"Ex.1 soma:\", ex1.sum(), \"média:\", ex1.mean())\n",
        "\n",
        "\n",
        "rng_ex = np.random.default_rng(seed=7)\n",
        "ex2 = rng_ex.integers(0, 10, size=(5, 5))\n",
        "print(\"Ex.2 matriz:\\n\", ex2)\n",
        "print(\"Média por linha:\", ex2.mean(axis=1))\n",
        "print(\"Média por coluna:\", ex2.mean(axis=0))\n",
        "\n",
        "\n",
        "print(\"Ex.3 std ddof=0 vs ddof=1:\", np.std(amostra, ddof=0), np.std(amostra, ddof=1))\n",
        "\n",
        "\n",
        "u = np.array([1, 2, 3, 4], dtype=float)\n",
        "v = np.array([4, 3, 2, 1], dtype=float)\n",
        "print(\"Ex.4 correlação u,v:\", np.corrcoef(u, v)[0, 1])\n",
        "\n",
        "\n",
        "sem = np.arange(1, len(gasto) + 1)\n",
        "fig, ax = plt.subplots(figsize=(6, 3))\n",
        "ax.plot(sem, gasto, marker=\"o\", color=\"#c2410c\")\n",
        "ax.set_title(\"Ex.5 Gasto em mídias por semana\")\n",
        "ax.set_xlabel(\"Semana\")\n",
        "ax.set_ylabel(\"Gasto (mil R$)\")\n",
        "ax.grid(True, alpha=0.3)\n",
        "plt.show()\n",
    ]
    clear_out(cells[id_gab])

    # Limpar saídas de todas as células de código
    for c in cells:
        clear_out(c)

    NB_PATH.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Notebook atualizado:", NB_PATH)


if __name__ == "__main__":
    main()
