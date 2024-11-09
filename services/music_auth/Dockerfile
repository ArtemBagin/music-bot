FROM python:3.12.6-slim

ENV POETRY_VERSION=1.8.2
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH="/opt/app/services/music_auth/src:$PYTHONPATH"
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /opt/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-root

COPY services/music_auth ./services/music_auth

RUN poetry install --no-dev

WORKDIR /opt/app/services/music_auth

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
