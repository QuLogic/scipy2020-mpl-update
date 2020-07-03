#!/usr/bin/env python3

from datetime import datetime
import subprocess
import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as mdates

from mplslide import check_requirements
check_requirements()  # noqa: F402

from mplslide import BULLET, FONT
from title import create_icon_axes, slides as title_slides


def history(mpl_path):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, 'Release History',
             fontproperties=FONT, color='C0', fontsize=72)

    tags = subprocess.run(['git', 'tag', '-l',
                           '--format=%(refname:strip=2) %(creatordate:short)'],
                          cwd=mpl_path, capture_output=True, text=True)
    dates = []
    names = []
    for item in tags.stdout.splitlines():
        tag_name, date = item.split(' ', 1)
        if 'rc' not in tag_name and 'b' not in tag_name:
            dates.append(datetime.fromisoformat(date))
            names.append(tag_name)

    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    ax = fig.add_axes((0.05, 0.11, 0.9, 0.7))

    ax.vlines(dates, 0, levels, color="tab:red", linewidth=3)
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w", linewidth=3, markersize=10)

    # annotate lines
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top",
                    fontsize=24)

    # format xaxis with 4 month intervals
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=24)

    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y=0.1)

    # Annotate range between SciPy 2019 and SciPy 2020.
    ax.axvspan(datetime(2019, 7, 8), datetime(2020, 7, 6), alpha=0.5)

    # Only plot the last 5 years before SciPy 2020.
    ax.set_xlim(datetime(2015, 7, 6), datetime(2020, 7, 6))

    return fig


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
    (history, MPL_PATH, ),
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
