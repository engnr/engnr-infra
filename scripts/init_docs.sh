#!/usr/bin/env sh -e

DOCS_DIR=${1:-docs}

mkdir -p ../${DOCS_DIR}/_static

cp -Rf docs/template/* ../${DOCS_DIR}

if [ ! -f ../.gitignore ] || ! grep -qm1 'build-*' ../.gitignore; then
  echo 'build-*' >> ../.gitignore
fi
