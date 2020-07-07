"""
Common functions for working with slides.
"""

import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager


#: The blue used for Matplotlib logo.
MPL_BLUE = '#11557c'
#: The font to use for the Matplotlib logo.
LOGO_FONT = None
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
    and that the Carlito and/or Calibri fonts are available.
    """

    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    # The original font is Calibri, if that is not installed, we fall back
    # to Carlito, which is metrically equivalent.
    calibri = carlito = None
    if 'Calibri' in matplotlib.font_manager.findfont('Calibri:bold'):
        calibri = matplotlib.font_manager.FontProperties(family='Calibri',
                                                         weight='bold')
    if 'Carlito' in matplotlib.font_manager.findfont('Carlito:bold'):
        carlito = matplotlib.font_manager.FontProperties(family='Carlito',
                                                         weight='bold')
    global FONT, LOGO_FONT
    if calibri is not None:
        LOGO_FONT = calibri
        if carlito is None:
            FONT = calibri
            print('WARNING: Using Calibri for all text. '
                  'Non-logo text may not appear correct.')
        else:
            FONT = carlito
            print('Using Calibri for logo and Carlito for remaining text.')
    elif carlito is not None:
        print('WARNING: Using Carlito for all text. '
              'The logo may not appear correct.')
        LOGO_FONT = carlito
        FONT = carlito
    else:
        sys.exit('Calibri or Carlito font must be installed.')


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


def annotate_pr_author(fig, *authors, pr=None):
    """
    Annotate the Pull Request author(s) on the bottom-right corner of a slide.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    authors : list of str
        The GitHub usernames to use for the annotation.
    pr : int, optional
        The PR number on GitHub to link to.
    """

    text = 'PR by ' + ', '.join(f'@{author}' for author in authors)
    t = fig.text(0.95, 0.05, text,
                 fontproperties=FONT, fontsize=32, alpha=0.7,
                 horizontalalignment='right')
    if pr is not None:
        t.set_url(f'https://github.com/matplotlib/matplotlib/pull/{pr}')
