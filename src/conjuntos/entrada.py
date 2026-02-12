from conjuntos.constantes import MAX_ELEMENTOS, MIN_ELEMENTOS
from conjuntos.formatacao import imprimir_cabecalho


class ValidacaoError(Exception):
    """Exceção para erros de validação da entrada do usuário."""


def parsear_entrada(texto: str) -> frozenset[int]:
    """
    Converte uma string de números separados por espaço em um frozenset.

    Raises:
        ValidacaoError: Se a entrada for vazia, contiver não-inteiros
                       ou a quantidade de elementos únicos estiver fora do intervalo.
    """
    texto = texto.strip()
    if not texto:
        raise ValidacaoError("Entrada vazia.")

    try:
        elementos: list[int] = list(map(int, texto.split()))
    except ValueError as err:
        raise ValidacaoError("Digite apenas números inteiros separados por espaço.") from err

    conjunto: frozenset[int] = frozenset(elementos)
    duplicatas: int = len(elementos) - len(conjunto)

    if duplicatas > 0:
        print(f"  ⚠  {duplicatas} elemento(s) duplicado(s) removido(s).")

    if len(conjunto) < MIN_ELEMENTOS:
        raise ValidacaoError(f"Poucos elementos únicos ({len(conjunto)}). Mínimo: {MIN_ELEMENTOS}.")

    if len(conjunto) > MAX_ELEMENTOS:
        raise ValidacaoError(f"Muitos elementos únicos ({len(conjunto)}). Máximo: {MAX_ELEMENTOS}.")

    return conjunto


def ler_conjunto_usuario() -> frozenset[int]:
    """
    Loop de leitura que solicita ao usuário um conjunto válido.
    Retorna somente quando a entrada passa por toda a validação.
    """
    imprimir_cabecalho("ENTRADA DO CONJUNTO A")
    print("  Digite números inteiros separados por espaço.")
    print(f"  Quantidade permitida: {MIN_ELEMENTOS} a {MAX_ELEMENTOS} elementos únicos.\n")

    while True:
        try:
            entrada: str = input("  ❯ ")
            return parsear_entrada(entrada)
        except ValidacaoError as erro:
            print(f"  ✗ {erro}\n")
