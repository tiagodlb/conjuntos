from dataclasses import dataclass

from conjuntos.constantes import MARGEM_ALEATORIO, MAX_ELEMENTOS, MIN_ELEMENTOS


@dataclass(frozen=True, slots=True)
class ResultadoOperacoes:
    """Armazena todos os resultados das operações entre dois conjuntos."""

    a: frozenset[int]
    b: frozenset[int]
    universo: frozenset[int]
    uniao: frozenset[int]
    intersecao: frozenset[int]
    diferenca_ab: frozenset[int]
    diferenca_ba: frozenset[int]
    diferenca_simetrica: frozenset[int]
    complemento_a: frozenset[int]
    complemento_b: frozenset[int]


@dataclass(frozen=True, slots=True)
class ConfigGeracao:
    """Configuração para geração do conjunto aleatório."""

    referencia: frozenset[int]
    margem: int = MARGEM_ALEATORIO
    tamanho_min: int = MIN_ELEMENTOS
    tamanho_max: int = MAX_ELEMENTOS

    @property
    def limite_inferior(self) -> int:
        return min(self.referencia) - self.margem

    @property
    def limite_superior(self) -> int:
        return max(self.referencia) + self.margem
