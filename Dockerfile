# namedtuple Maker Development Container
FROM python:3.9-slim-buster

WORKDIR /workspaces/namedtuple-maker

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements/ requirements/

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt

ENV PYTHONPATH=/workspaces/namedtuple-maker:/~.

CMD ["/bin/bash"]
