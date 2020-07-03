#!/usr/bin/env python3

import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements
check_requirements()  # noqa: F402

from mplslide import BULLET, FONT
from title import create_icon_axes, slides as title_slides
from timeline import slides as history_slides


def feature32_overview():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.2 Feature Highlights',
             fontproperties=FONT, color='C0', fontsize=72)

    fig.text(0.05, 0.8, f'''\
{BULLET} Unit converters recognize subclasses
{BULLET} $pyplot.imsave$ accepts metadata and PIL options
{BULLET} $FontProperties$ accepts $os.PathLike$
{BULLET} bar3d lightsource shading
{BULLET} Gouraud-shading alpha channel in PDF backend
{BULLET} Improvements in Logit scale ticker and formatter
{BULLET} rcParams for axes title location and color
{BULLET} 3-digit and 4-digit hex colors
{BULLET} Added support for RGB(A) images in pcolorfast
{BULLET} Shifting errorbars''',
             fontproperties=FONT, alpha=0.7, fontsize=48,
             verticalalignment='top')
    """
    import matplotlib.pyplot as plt

    # Use old kerning values:
    plt.rcParams['text.kerning_factor'] = 6
    fig, ax = plt.subplots()
    ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
    ax.set_title('Before (text.kerning_factor = 6)')
    """

    # Use new kerning values:
    # plt.rcParams['text.kerning_factor'] = 0
    # fig, ax = plt.subplots()
    # ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
    # ax.set_title('After (text.kerning_factor = 0)')

    return fig


def feature33_mosaic():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - Mosaic',
             fontproperties=FONT, color='C0', fontsize=72)

    return fig


def feature33_2():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - 2',
             fontproperties=FONT, color='C0', fontsize=72)

    return fig


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
    (feature32_overview, ),
    (feature33_mosaic, ),
    (feature33_2, ),
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
