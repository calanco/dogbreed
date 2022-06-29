FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /dogbreed
RUN python -m pip install --upgrade pip

COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy --clear

COPY ./app ./app
CMD ["pipenv", "run", "uvicorn", "app.main:app", \
        "--host", "0.0.0.0", "--port", "8080"]