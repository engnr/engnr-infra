#!/usr/bin/env python3

import argparse
import subprocess


def main():
  parser = argparse.ArgumentParser(
    description='Documentation generation service.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-s', '--source', default='docs', help='Source directory')
  parser.add_argument('-o', '--output', default='build-docs', help='Output directory')
  parser.add_argument('-b', '--builder', default='html', help='Sphinx builder type')
  parser.add_argument('--once', action='store_true',
    help='Generate documentation once instead of doing so continuously')
  args = parser.parse_args()

  if args.once:
    subprocess.run('sphinx-build -b {} {} {}'.format(args.builder, args.source, args.output), shell=True, check=True)
  else:
    print('''
      Glad to see you writing documentation!
      Edit sources using your favourite text editor.
      Generated output is placed into {} folder.'''.format(args.output))

    while True:
      print('\n====================================================================\n')
      subprocess.run('''\
        inotifywait -qq --recursive \
          --event modify --event move --event create --event delete \
          --exclude '/\..+' --exclude '/.+~' --exclude '/.+.sw?' \
          {1} && \
        sphinx-build -b {0} {1} {2} \
        '''.format(args.builder, args.source, args.output), shell=True, check=True)
      

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
