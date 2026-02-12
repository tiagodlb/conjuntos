import sys

from conjuntos.constantes import LARGURA
from conjuntos.entrada import ler_conjunto_usuario
from conjuntos.formatacao import exibir_resultados
from conjuntos.modelos import ConfigGeracao, ResultadoOperacoes
from conjuntos.operacoes import calcular_operacoes, gerar_conjunto_aleatorio


def _executar_ciclo() -> None:
    """Executa um ciclo completo: leitura → geração → cálculo → exibição."""
    conjunto_a: frozenset[int] = ler_conjunto_usuario()
    config: ConfigGeracao = ConfigGeracao(referencia=conjunto_a)
    conjunto_b: frozenset[int] = gerar_conjunto_aleatorio(config)
    resultado: ResultadoOperacoes = calcular_operacoes(conjunto_a, conjunto_b)
    exibir_resultados(resultado)


def main() -> None:
    """Ponto de entrada do programa."""
    print()
    print("╔" + "═" * (LARGURA - 2) + "╗")
    print("║  Operações com Conjuntos".ljust(LARGURA - 1) + "║")
    print("║  Lógica e Matemática Discreta (EECP0015)".ljust(LARGURA - 1) + "║")
    print("╚" + "═" * (LARGURA - 2) + "╝")

    try:
        while True:
            _executar_ciclo()
            resposta: str = input("  Executar novamente? (s/n): ").strip().lower()
            if resposta != "s":
                break
    except (KeyboardInterrupt, EOFError):
        pass

    print("\n  Encerrando. Até mais!\n")
    sys.exit(0)
