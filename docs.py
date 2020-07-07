"""
Documentation highlights.
"""

from mplslide import FONT, BULLET, new_slide, slide_heading


def docs():
    fig = new_slide()

    slide_heading(fig, 'Documentation')

    props = dict(fontproperties=FONT, fontsize=56, alpha=0.7,
                 verticalalignment='top')

    fig.text(0.05, 0.8, 'Large and ongoing documentation rewrite', **props)
    fig.text(0.1, 0.8, f'\n{BULLET} Refreshed homepage', **props)
    fig.text(0.1, 0.8, f'\n\n{BULLET} 323 Pull Requests in 3.3 alone', **props)

    fig.text(0.05, 0.5, "3.3 What's New?", **props)
    t = fig.text(0.1, 0.5,
                 '\nhttps://matplotlib.org/3.3.0/users/whats_new.html',
                 **props)
    t.set_url('https://matplotlib.org/3.3.0/users/whats_new.html')

    fig.text(0.05, 0.3, 'Cheatsheets!', **props)
    t = fig.text(0.1, 0.3, '\nhttps://github.com/matplotlib/cheatsheets/',
                 **props)
    t.set_url('https://github.com/matplotlib/cheatsheets/')

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        docs(),
    )
