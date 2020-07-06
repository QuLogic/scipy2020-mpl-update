"""
Common functions for working with slides.
"""

import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager


#: The blue used for Matplotlib logo.
MPL_BLUE = '#11557c'
#: A bullet point.
BULLET = '$\N{Bullet}$'
#: The FontProperties to use, Carlito.
FONT = None
#: The size of a slide figure.
FIGSIZE = (19.2, 10.8)
#: The DPI of a slide figure.
DPI = 100


def check_requirements():
    """
    Check requirements to create the slides.

    Currently checks whether the path to a Matplotlib repository is specified,
    and that the Carlito font is available.
    """

    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    if 'Carlito' not in matplotlib.font_manager.findfont('Carlito:bold'):
        sys.exit('Carlito font must be installed.')
    global FONT
    FONT = matplotlib.font_manager.FontProperties(family='Carlito',
                                                  weight='bold')


def new_slide(plain=False):
    """
    Create a new slide.

    Parameters
    ----------
    plain : bool, default: False
        Whether to leave out any slide decorations (e.g., logo).
    """

    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    fig.mplslide_props = {'plain': plain}
    return fig


def slide_heading(fig, text):
    """
    Add a heading to a slide, using a common style.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    text : str
        The text to place in the heading.
    """

    fig.text(0.05, 0.85, text, color='C0', fontproperties=FONT, fontsize=72)
