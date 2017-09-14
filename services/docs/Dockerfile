FROM alpine
 
RUN apk update && apk upgrade

RUN apk add --no-cache \
    python3 \
  && pip3 install -U --no-cache-dir \
    termcolor \
    sphinx \
    sphinx_bootstrap_theme \
    sphinxbootstrap4theme \
    sphinx_rtd_theme \
    guzzle_sphinx_theme \
    sphinxcontrib-plantuml \
    recommonmark

RUN apk add --no-cache --virtual=dependencies \
    build-base \
    jpeg-dev \
    python3-dev \
    zlib-dev \
  && pip3 install -U --no-cache-dir \
    sphinxcontrib-blockdiag \
    sphinxcontrib-actdiag \
    sphinxcontrib-nwdiag \
    sphinxcontrib-seqdiag \
  && apk del dependencies

RUN apk add --no-cache \
    doxygen \
  && pip3 install -U --no-cache-dir \
    breathe

ENV PLANTUML_VERSION 1.2017.16
RUN apk add --no-cache curl && \
  curl -L -o /usr/bin/plantuml.jar \
    https://sourceforge.net/projects/plantuml/files/${PLANTUML_VERSION}/plantuml.${PLANTUML_VERSION}.jar/download && \
  apk del curl
RUN apk add --no-cache \
    graphviz \
    openjdk8-jre \
    ttf-dejavu
RUN printf '#!/bin/sh\n\
  java -jar -Djava.awt.headless=true /usr/bin/plantuml.jar -failfast2 "$@"\n' \
  > /usr/bin/plantuml && \
  chmod +x /usr/bin/plantuml

RUN apk add --no-cache \
  inotify-tools

WORKDIR /home
COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
EXPOSE 80
