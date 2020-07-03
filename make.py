#!/usr/bin/env python3

import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements
check_requirements()  # noqa: F402

from mplslide import BULLET, FONT
from title import create_icon_axes, slides as title_slides
from timeline import slides as history_slides
from feature32 import slides as feature32_slides
from feature33 import slides as feature33_slides


def release_plan():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, 'Release Plan',
             fontproperties=FONT, color='C0', fontsize=72)

    fig.text(0.05, 0.6, 'Next feature release: 3.4',
             fontproperties=FONT, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.5, f'{BULLET} September 2020',
             fontproperties=FONT, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.4, f'{BULLET} Dropping Python 3.6 support',
             fontproperties=FONT, alpha=0.7, fontsize=56)

    return fig


MPL_PATH = sys.argv[1]
PAGES = [
    (title_slides, ),
    (history_slides, MPL_PATH, ),
    (feature32_slides, ),
    (feature33_slides, ),
    (release_plan, ),
]

with PdfPages('slides.pdf') as pdf:
    for i, (page, *args) in enumerate(PAGES):
        figs = page(*args)
        if not isinstance(figs, (tuple, list)):
            figs = (figs, )
        for fig in figs:
            if i != 0:
                create_icon_axes(fig, (0.825, 0.825, 0.2, 0.15),
                                 0.3, 0.3, 0.3, [5])
            pdf.savefig(fig)
