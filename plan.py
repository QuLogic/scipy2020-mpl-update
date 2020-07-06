"""
Future plans.
"""

from mplslide import BULLET, FONT, new_slide, slide_heading


def slides():
    """
    Create slide for future plans.
    """
    fig = new_slide()

    slide_heading(fig, 'Future Plans')

    props = dict(fontproperties=FONT, fontsize=56, alpha=0.7,
                 verticalalignment='top')

    fig.text(0.05, 0.8, 'Next feature release: 3.4', **props)
    fig.text(0.1, 0.7, f'{BULLET} September 2020', **props)
    fig.text(0.1, 0.6,
             f'{BULLET} Dropping support for Python 3.6 & NumPy 1.15',
             **props)

    fig.text(0.05, 0.4, 'Google Season of Docs 2020', **props)

    fig.text(0.05, 0.2, 'Check out our blog!', **props)
    t = fig.text(0.1, 0.2, '\nhttps://matplotlib.org/matplotblog/',
                 **props)
    t.set_url('https://matplotlib.org/matplotblog/')

    return fig
