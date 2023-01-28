FROM python:3.9.12-slim-bullseye as python
ENV PYTHONUNBUFFERED=true
WORKDIR /app
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-interaction --no-ansi -vvv
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT ["python", "main.py"]