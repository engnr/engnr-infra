This repo contains various facilities for:

* documentation writing
* ~~project automation~~
* ~~environment provisioning~~
* ~~other infrastructure related tools~~


**Note.** All scripts are intended to be executed from the root of this repo.


# Documentation writing

1. Build Docker image by running `scripts/build_docs_image.sh`.

1. Create initial documentation set by running `scripts/init_docs.sh`.

   This script will create `docs` folder one level above relative to your local clone of this
   repo. Such behaviour enables linking this repo as a Git submodule into several projects at
   the same time.

   In case another name of documentation folder is needed run this script with desired name
   as a first argument.

1. Once you have documentation set configured just run `scripts/gen_docs.sh`.

   This script listens to filesystem change events and automatically generates its output into
   `build-docs` folder. In case another name of output folder is needed run this script with
   option `-o` followed by desired name.

   Note that you have to explicitly pass source documentation folder as a first positional
   argument too if you chose to use non-default naming on the previous step.

1. Now edit documentation sources using your favourite text editor.

   Use browser of your choice to open `index.html` page. Hint: there are various browser
   plugins which can reload page automatically for your further convenience.

1. Use `scripts/gen_docs.sh --once` to power up your CI system for documentation publishing
   to GitHub/GitLab pages, etc. Run this script with `--help` for more info on supported
   options.
