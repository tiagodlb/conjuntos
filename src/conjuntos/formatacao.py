from conjuntos.constantes import LARGURA
from conjuntos.modelos import ResultadoOperacoes


def formatar_conjunto(s: frozenset[int]) -> str:
    """Formata um frozenset como string ordenada. Retorna ∅ se vazio."""
    if not s:
        return "∅"
    return "{" + ", ".join(map(str, sorted(s))) + "}"


def imprimir_cabecalho(titulo: str) -> None:
    """Imprime um cabeçalho visual."""
    print()
    print("─" * LARGURA)
    print(f"  {titulo}")
    print("─" * LARGURA)
    print()


def _imprimir_linha(rotulo: str, valor: str, indent: int = 4) -> None:
    """Imprime uma linha formatada com rótulo alinhado."""
    espacamento: str = " " * indent
    print(f"{espacamento}{rotulo:<12}{valor}")


def exibir_resultados(r: ResultadoOperacoes) -> None:
    """Exibe todos os resultados das operações de forma organizada."""
    imprimir_cabecalho("CONJUNTOS DE ENTRADA")
    _imprimir_linha("A =", formatar_conjunto(r.a))
    _imprimir_linha("B =", formatar_conjunto(r.b))
    _imprimir_linha("U =", formatar_conjunto(r.universo))

    imprimir_cabecalho("OPERAÇÕES")
    _imprimir_linha("A ∪ B  =", formatar_conjunto(r.uniao))
    _imprimir_linha("A ∩ B  =", formatar_conjunto(r.intersecao))
    _imprimir_linha("A − B  =", formatar_conjunto(r.diferenca_ab))
    _imprimir_linha("B − A  =", formatar_conjunto(r.diferenca_ba))
    _imprimir_linha("A Δ B  =", formatar_conjunto(r.diferenca_simetrica))

    imprimir_cabecalho("COMPLEMENTOS (em relação a U)")
    _imprimir_linha("Aᶜ =", formatar_conjunto(r.complemento_a))
    _imprimir_linha("Bᶜ =", formatar_conjunto(r.complemento_b))

    imprimir_cabecalho("CARDINALIDADES")
    cardinalidades: list[tuple[str, int]] = [
        ("|A|", len(r.a)),
        ("|B|", len(r.b)),
        ("|A ∪ B|", len(r.uniao)),
        ("|A ∩ B|", len(r.intersecao)),
        ("|A − B|", len(r.diferenca_ab)),
        ("|B − A|", len(r.diferenca_ba)),
        ("|A Δ B|", len(r.diferenca_simetrica)),
        ("|U|", len(r.universo)),
    ]
    for rotulo, valor in cardinalidades:
        _imprimir_linha(rotulo, str(valor))

    print()
