#!/usr/bin/env python3

from datetime import datetime
import subprocess
import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.cm as cm
import matplotlib.dates as mdates
import matplotlib.font_manager
from matplotlib.patches import Rectangle, PathPatch
from matplotlib.textpath import TextPath
import matplotlib.transforms as mtrans


MPL_BLUE = '#11557c'
BULLET = '$\N{Bullet}$'


def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    Create a polar axes containing the Matplotlib radar plot.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to draw into.
    ax_position : (float, float, float, float)
        The position of the created Axes in figure coordinates as
        (x, y, width, height).
    lw_bars : float
        The linewidth of the bars.
    lw_grid : float
        The linewidth of the grid.
    lw_border : float
        The linewidth of the Axes border.
    rgrid : array-like
        Positions of the radial grid.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The created Axes.
    """
    with plt.rc_context({'axes.edgecolor': MPL_BLUE,
                         'axes.linewidth': lw_border}):
        ax = fig.add_axes(ax_position, projection='polar')
        ax.set_axisbelow(True)

        N = 7
        arc = 2. * np.pi
        theta = np.arange(0.0, arc, arc / N)
        radii = np.array([2, 6, 8, 7, 4, 5, 8])
        width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])
        bars = ax.bar(theta, radii, width=width, bottom=0.0, align='edge',
                      edgecolor='0.3', lw=lw_bars)
        for r, bar in zip(radii, bars):
            color = *cm.jet(r / 10.)[:3], 0.6  # color from jet with alpha=0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # the actual visible background - extends a bit beyond the axis
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax


def create_text_axes(fig, height_px):
    """Create an axes in *fig* that contains 'matplotlib' as Text."""
    ax = fig.add_axes((0, 0.4, 1, 0.5))
    ax.set_aspect("equal")
    ax.set_axis_off()

    path = TextPath((0, 0), "matplotlib", size=height_px * 0.8, prop=font)

    angle = 4.25  # degrees
    trans = mtrans.Affine2D().skew_deg(angle, 0)

    patch = PathPatch(path, transform=trans + ax.transData, color=MPL_BLUE,
                      lw=0)
    ax.add_patch(patch)
    ax.autoscale()


def title(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    create_text_axes(fig, 110)
    ax_pos = (0.535, 0.52, 0.17, 0.28)
    create_icon_axes(fig, ax_pos, 1.4, 1, 2, [1, 3, 5, 7])

    fig.text(0.5, 0.3, 'SciPy 2020',
             fontproperties=font, color='C0', fontsize=72)
    fig.text(0.5, 0.2, '@matplotlib',
             fontproperties=font, color='C0', fontsize=72)

    pdf.savefig(fig)


def history(pdf, mpl_path):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, 'Release History',
             fontproperties=font, color='C0', fontsize=72)

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

    pdf.savefig(fig)


def feature32_overview(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.2 Feature Highlights',
             fontproperties=font, color='C0', fontsize=72)

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
             fontproperties=font, alpha=0.7, fontsize=48,
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

    pdf.savefig(fig)


def feature33_mosaic(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - Mosaic',
             fontproperties=font, color='C0', fontsize=72)

    pdf.savefig(fig)


def feature33_2(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - 2',
             fontproperties=font, color='C0', fontsize=72)

    pdf.savefig(fig)


def release_plan(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, 'Release Plan',
             fontproperties=font, color='C0', fontsize=72)

    fig.text(0.05, 0.6, 'Next feature release: 3.4',
             fontproperties=font, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.5, f'{BULLET} September 2020',
             fontproperties=font, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.4, f'{BULLET} Dropping Python 3.6 support',
             fontproperties=font, alpha=0.7, fontsize=56)

    pdf.savefig(fig)


if len(sys.argv) < 2:
    sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
mpl_path = sys.argv[1]

if 'Carlito' not in matplotlib.font_manager.findfont('Carlito:bold'):
    sys.exit('Carlito font must be installed.')
font = matplotlib.font_manager.FontProperties(family='Carlito', weight='bold')
with PdfPages('slides.pdf') as pdf:
    title(pdf)
    history(pdf, mpl_path)
    feature32_overview(pdf)
    feature33_mosaic(pdf)
    feature33_2(pdf)
    release_plan(pdf)
