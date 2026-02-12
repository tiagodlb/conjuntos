import random

from conjuntos.constantes import MARGEM_UNIVERSO
from conjuntos.modelos import ConfigGeracao, ResultadoOperacoes


def gerar_conjunto_aleatorio(config: ConfigGeracao) -> frozenset[int]:
    """
    Gera um frozenset aleatório de inteiros.
    O intervalo é baseado nos valores do conjunto de referência
    para possibilitar interseção parcial.
    """
    tamanho: int = random.randint(config.tamanho_min, config.tamanho_max)
    elementos: set[int] = set()

    while len(elementos) < tamanho:
        elementos.add(random.randint(config.limite_inferior, config.limite_superior))

    return frozenset(elementos)


def construir_universo(a: frozenset[int], b: frozenset[int]) -> frozenset[int]:
    """
    Constrói o conjunto universo U como um intervalo contínuo
    que engloba A ∪ B com uma margem de ±MARGEM_UNIVERSO.
    """
    todos: frozenset[int] = a | b
    minimo: int = min(todos) - MARGEM_UNIVERSO
    maximo: int = max(todos) + MARGEM_UNIVERSO
    return frozenset(range(minimo, maximo + 1))


def calcular_operacoes(a: frozenset[int], b: frozenset[int]) -> ResultadoOperacoes:
    """Executa todas as operações de conjuntos e retorna um ResultadoOperacoes."""
    universo: frozenset[int] = construir_universo(a, b)

    return ResultadoOperacoes(
        a=a,
        b=b,
        universo=universo,
        uniao=a | b,
        intersecao=a & b,
        diferenca_ab=a - b,
        diferenca_ba=b - a,
        diferenca_simetrica=a ^ b,
        complemento_a=universo - a,
        complemento_b=universo - b,
    )
