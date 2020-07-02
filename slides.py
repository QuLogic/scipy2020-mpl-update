#!/usr/bin/env python3

from datetime import datetime
import json
import sys
import urllib.request

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
    ax = fig.add_axes((0, 0.5, 1, 0.5))
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
    ax_pos = (0.535, 0.62, 0.17, 0.28)
    create_icon_axes(fig, ax_pos, 1.4, 1, 2, [1, 3, 5, 7])

    fig.text(0.5, 0.4, 'SciPy 2020',
             fontproperties=font, color='C0', fontsize=72)
    fig.text(0.5, 0.3, '@matplotlib',
             fontproperties=font, color='C0', fontsize=72)

    pdf.savefig(fig)


def history(pdf):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.8, 'Release History',
             fontproperties=font, color='C0', fontsize=72)

    try:
        url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
        url += '?per_page=100'
        data = json.loads(
            urllib.request.urlopen(url, timeout=.4).read().decode())

        dates = []
        names = []
        for item in data:
            if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
                dates.append(item['published_at'].split("T")[0])
                names.append(item['tag_name'])
        # Convert date strings (e.g. 2014-10-18) to datetime
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

    except Exception:
        # In case the above fails, e.g. because of missing internet connection
        # use the following lists as fallback.
        names = ['v2.2.4', 'v3.0.3', 'v3.0.2', 'v3.0.1', 'v3.0.0', 'v2.2.3',
                 'v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0',
                 'v2.0.2', 'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1',
                 'v1.5.0', 'v1.4.3', 'v1.4.2', 'v1.4.1', 'v1.4.0']

        dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
                 '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
                 '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
                 '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
                 '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
                 '2014-10-26', '2014-10-18', '2014-08-26']

        # Convert date strings (e.g. 2014-10-18) to datetime
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

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

    pdf.savefig(fig)


if 'Carlito' not in matplotlib.font_manager.findfont('Carlito:bold'):
    sys.exit('Carlito font must be installed.')
font = matplotlib.font_manager.FontProperties(family='Carlito', weight='bold')
with PdfPages('slides.pdf') as pdf:
    title(pdf)
    history(pdf)
