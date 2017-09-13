#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import textwrap


def build_docker_image(args):
  subprocess.run('docker-compose build docs', shell=True, check=True)


def init_docs(args):
  source_path = '../{}'.format(args.source)
  build_path_pattern = 'build-*'
  try:
    shutil.copytree('services/docs/template', source_path)
    os.mkdir('{}/_static'.format(source_path))
    print('Created initial documentation set at {}'.format(source_path))

    try:
      subprocess.run('( ! test -f ../.gitignore || ! grep -qm1 "{0}" ../.gitignore ) && echo "{0}" >> ../.gitignore'.format(build_path_pattern), shell=True, check=True)
      print('Added {} to .gitignore'.format(build_path_pattern))
    except subprocess.CalledProcessError:
      pass
  except FileExistsError:
    print('Folder {} exists. Remove it and try again.'.format(source_path))


def watch_docs(args):
  source_path = '../{}'.format(args.source)
  output_path = '../{}'.format(args.output)
  print(textwrap.dedent(
    '''
    Watching {} for change events.
    Output will be generated to {}.
    '''.format(source_path, output_path)))

  subprocess.run('docker-compose run docs -s {} -o {} -b {}'.format(args.source, args.output, args.builder), shell=True, check=True)


def build_docs(args):
  source_path = '../{}'.format(args.source)
  output_path = '../{}'.format(args.output)
  print(textwrap.dedent(
    '''
    Building from {}.
    Output will be generated to {}.
    '''.format(source_path, output_path)))

  subprocess.run('docker-compose run docs --once -s {} -o {} -b {}'.format(args.source, args.output, args.builder), shell=True, check=True)


def main():
  class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
    pass

  parser = argparse.ArgumentParser(
    description=textwrap.dedent(
        '''\
          Documentation service control tool.
          Pass --help after any command listed below for more info on its usage.
        '''),
    formatter_class=CustomFormatter)
  parser.set_defaults(func=lambda args: parser.print_help())
  subparsers = parser.add_subparsers(help='Supported commands')

  image_help = 'Build Docker image with documentation service'
  image_parser = subparsers.add_parser('image', help=image_help, description=image_help,
    formatter_class=CustomFormatter)
  image_parser.set_defaults(func=build_docker_image)

  init_help = 'Create source folder for documentation set'
  init_parser = subparsers.add_parser('init', help=init_help, description=init_help,
    formatter_class=CustomFormatter)
  init_parser.add_argument('-s', '--source', default='docs', help='Source directory')
  init_parser.set_defaults(func=init_docs)

  watch_help = 'Generate documentation each time sources change'
  watch_parser = subparsers.add_parser('watch', help=watch_help, description=watch_help,
    formatter_class=CustomFormatter)
  watch_parser.add_argument('-s', '--source', default='docs', help='Source directory')
  watch_parser.add_argument('-o', '--output', default='build-docs', help='Output directory')
  watch_parser.add_argument('-b', '--builder', default='html', help='Sphinx builder type')
  watch_parser.set_defaults(func=watch_docs)

  build_help = 'Generate documentation once'
  build_parser = subparsers.add_parser('build', help=build_help, description=build_help,
    formatter_class=CustomFormatter)
  build_parser.add_argument('-s', '--source', default='docs', help='Source directory')
  build_parser.add_argument('-o', '--output', default='build-docs', help='Output directory')
  build_parser.add_argument('-b', '--builder', default='html', help='Sphinx builder type')
  build_parser.set_defaults(func=build_docs)

  args = parser.parse_args()
  args.func(args)


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
