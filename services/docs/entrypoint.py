#!/usr/bin/env python3

import argparse
import subprocess
from termcolor import cprint


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
    print()
    result = subprocess.run('httpd -h {}'.format(args.output), shell=True)
    if result.returncode == 0:
        print('Server started successfully.')
    else:
        cprint('Failed to launch server. Open files in a browser manually as a fallback.', 'yellow')

    while True:
      print('\n====================================================================\n')
      subprocess.run('''\
        inotifywait -qq --recursive \
          --event modify --event move --event create --event delete \
          --exclude '/\..+' --exclude '/.+~' --exclude '/.+.sw?' \
          {1} && \
        sphinx-build -b {0} {1} {2} \
        '''.format(args.builder, args.source, args.output), shell=True)
      

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
