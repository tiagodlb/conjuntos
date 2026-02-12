FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync

COPY src/ src/

RUN uv sync

CMD ["uv", "run", "conjuntos"]
