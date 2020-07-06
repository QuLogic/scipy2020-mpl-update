"""
General news.
"""

from functools import partial

from mplslide import BULLET, FONT, new_slide, slide_heading


def bullet_level1(fig, y, text):
    """
    Create a level 1 list item.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.05, y, text,
                    fontproperties=FONT, fontsize=48, alpha=0.7,
                    verticalalignment='top')


def bullet_level2(fig, y, text):
    """
    Create a level 2 list item.

    This is roughly the same as level 1, but not bolded, and indented more.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.1, y, text,
                    fontproperties=FONT, fontsize=48, fontweight='normal',
                    alpha=0.7, verticalalignment='top')


def slides():
    """
    Create slide for general news.
    """
    fig = new_slide()

    slide_heading(fig, 'General News')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    t = level1(0.8, f'{BULLET} Chan Zuckerberg Institute grant')
    t.set_url('https://matplotlib.org/matplotblog/posts/matplotlib-rsef/')
    level1(0.8, '\n    \N{EM dash} Essential Open Source Software for Science')

    level2(0.8,
           '\n\nThomas Caswell, Hannah Aizenman,\nElliott Sales de Andrade')

    t = level1(0.5, f'{BULLET} Google Summer of Code')
    t.set_url(
        'https://matplotlib.org/matplotblog/posts/introductory-gsoc2020-post/')

    level2(0.5,
           '\nSidharth Bansal \N{EM dash} test baseline images relocation')

    level1(0.35, f'{BULLET} Discourse')

    t = level2(0.35, '\nhttps://discourse.matplotlib.org/')
    t.set_url('https://discourse.matplotlib.org/')

    level1(0.2, f'{BULLET} PyPI classifier')

    t = level2(0.2, '\nFramework :: Matplotlib')
    t.set_url('https://pypi.org/search/?c=Framework+%3A%3A+Matplotlib')

    return fig
