FROM python:3.9 AS builder

RUN pip install --user pipenv
ENV PIPENV_VENV_IN_PROJECT=1
ADD Pipfile.lock Pipfile /usr/src/
WORKDIR /usr/src
RUN /root/.local/bin/pipenv sync

FROM python:3.9 AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -v /usr/src/venv
COPY --from=builder /usr/src/.venv/ /usr/src/venv/
COPY app /usr/src/app
COPY run.py /usr/src/
WORKDIR /usr/src/

CMD ["./venv/bin/python", "run.py", "--host", "0.0.0.0", "--port", "8080"]