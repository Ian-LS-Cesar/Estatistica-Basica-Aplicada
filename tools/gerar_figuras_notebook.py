"""Gera PNGs em img/ para o notebook (conceitos visíveis no GitHub)."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "img"


def main():
    IMG.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 2.2), dpi=130)
    ax.axis("off")
    ax.set_title("Indexação e fatiamento em arrays 1D", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.72, "arr = np.array([10, 20, 30, 40, 50])", ha="center", fontsize=10, family="monospace")
    ax.text(0.5, 0.42, "arr[0] → 10     arr[-1] → 50     arr[1:4] → [20, 30, 40]", ha="center", fontsize=9.5)
    ax.text(0.5, 0.12, "Filtro: arr[arr > 25] → [30, 40, 50]", ha="center", fontsize=9.5, color="#1d4ed8")
    plt.savefig(IMG / "indexacao_numpy_1d.png", bbox_inches="tight", facecolor="white")
    plt.close()

    fig, ax = plt.subplots(figsize=(7, 2.4), dpi=130)
    ax.axis("off")
    ax.set_title("Broadcasting (ideia)", fontsize=12, fontweight="bold")
    ax.text(
        0.5,
        0.55,
        "Matriz (3,4) + vetor (4,): o vetor é alinhado às colunas em cada linha.",
        ha="center",
        fontsize=10,
    )
    plt.savefig(IMG / "broadcasting_conceito.png", bbox_inches="tight", facecolor="white")
    plt.close()

    fig, ax = plt.subplots(figsize=(7, 2.2), dpi=130)
    ax.axis("off")
    ax.set_title("Correlação de Pearson (intuição)", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.65, "r ~ +1: sobem juntos (linear positiva)", ha="center", fontsize=9.5)
    ax.text(0.5, 0.38, "r ~ −1: um sobe, outro desce (linear negativa)", ha="center", fontsize=9.5)
    ax.text(0.5, 0.12, "r ~ 0: pouca relação linear", ha="center", fontsize=9.5)
    plt.savefig(IMG / "correlacao_pearson_intuicao.png", bbox_inches="tight", facecolor="white")
    plt.close()

    print("Figuras salvas em", IMG)


if __name__ == "__main__":
    main()
