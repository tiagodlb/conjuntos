# Operações com Conjuntos

**Disciplina:** Lógica e Matemática Discreta (EECP0015)  
**Curso:** Engenharia da Computação – UFMA  
**Professor:** Rondineli Seba

---

## Descrição

CLI que implementa as operações fundamentais da **teoria dos conjuntos**: união, interseção, diferença, diferença simétrica, complemento e cardinalidade.

O programa trabalha com dois conjuntos de **números inteiros**:

- **Conjunto A** — definido pelo usuário (4 a 8 elementos).
- **Conjunto B** — gerado aleatoriamente (4 a 8 elementos), com possibilidade de interseção parcial com A.

Um **conjunto universo U** é construído automaticamente a partir de A ∪ B com margem, permitindo o cálculo dos complementos.

---

## Como executar

### Com `uv` (recomendado)

```bash
# Instalar dependências e executar
uv run conjuntos

# Ou via módulo
uv run python -m conjuntos
```

### Com Python direto

```bash
pip install -e .
conjuntos
```

### Com Docker

```bash
docker build -t conjuntos .
docker run -it --rm conjuntos
```

---

## Tooling

| Ferramenta | Função |
|---|---|
| [uv](https://docs.astral.sh/uv/) | Gerenciamento de pacotes e ambiente virtual |
| [ruff](https://docs.astral.sh/ruff/) | Linter e formatter |
| [ty](https://docs.astral.sh/ty/) | Type checker |

```bash
# Lint
uv run ruff check src/

# Formatar
uv run ruff format src/

# Type check
uv run ty check src/
```

---

## Estrutura do projeto

```
conjuntos/
├── pyproject.toml          # Manifesto do projeto (uv, ruff, ty)
├── uv.lock                 # Lockfile gerado pelo uv
├── Dockerfile
├── .python-version
└── src/
    └── conjuntos/
        ├── __init__.py
        ├── __main__.py     # python -m conjuntos
        ├── cli.py          # Ponto de entrada e loop principal
        ├── constantes.py   # Constantes globais (Final[int])
        ├── modelos.py      # Dataclasses imutáveis (ResultadoOperacoes, ConfigGeracao)
        ├── entrada.py      # Leitura e validação de entrada do usuário
        ├── operacoes.py    # Geração aleatória e cálculo das operações
        └── formatacao.py   # Exibição formatada no terminal
```

---

## Operações implementadas

| Operação | Notação | Python |
|---|---|---|
| União | A ∪ B | `a \| b` |
| Interseção | A ∩ B | `a & b` |
| Diferença | A − B | `a - b` |
| Diferença Simétrica | A Δ B | `a ^ b` |
| Complemento | Aᶜ = U − A | `universo - a` |
| Cardinalidade | \|A\| | `len(a)` |

---

## Relação com a teoria dos conjuntos

O programa aplica diretamente os conceitos estudados em sala. O tipo `frozenset` do Python garante a propriedade fundamental de **não conter elementos duplicados** e a **imutabilidade** dos conjuntos após criação — refletindo a natureza estática dos conjuntos na matemática.

As operações de união (`|`), interseção (`&`), diferença (`-`) e diferença simétrica (`^`) são mapeadas para os operadores nativos, correspondendo às definições formais:

- **A ∪ B** = {x | x ∈ A ou x ∈ B}
- **A ∩ B** = {x | x ∈ A e x ∈ B}
- **A − B** = {x | x ∈ A e x ∉ B}
- **A Δ B** = (A − B) ∪ (B − A)
- **Aᶜ** = U − A = {x ∈ U | x ∉ A}

O conjunto universo U é construído como um intervalo contínuo que engloba A ∪ B com margem, garantindo que os complementos sejam significativos e que U ⊇ A ∪ B.
