#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# General
#

project = 'Engnr project'
version = '0.1'
release = '0.1'

copyright = '2017, Engnr'
author = 'Engnr team'

extensions = [
    'sphinx.ext.mathjax',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.nwdiag',                  
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.seqdiag'
]
actdiag_html_image_format = 'svg'
blockdiag_html_image_format = 'svg'
nwdiag_html_image_format = 'svg'
plantuml_output_format = 'svg'
seqdiag_html_image_format = 'svg'

templates_path = ['_templates']

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']
master_doc = 'index'

exclude_patterns = []

pygments_style = 'sphinx'

#
# HTML
#

html_theme = 'alabaster'

html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html'
    ]
}
