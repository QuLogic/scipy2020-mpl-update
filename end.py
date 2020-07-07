"""
End slide.
"""

from mplslide import FONT, new_slide, slide_heading


def slides():
    """
    Create end slide.
    """
    fig = new_slide()

    slide_heading(fig, 'Thank You!')

    props = dict(fontproperties=FONT, fontsize=56, color='C0',
                 horizontalalignment='center')

    fig.text(0.5, 0.5, 'This entire presentation was made in Matplotlib.',
             **props)

    t = fig.text(0.5, 0.4, '\nhttps://github.com/QuLogic/scipy2020-mpl-update',
                 **props)
    t.set_url('https://github.com/QuLogic/scipy2020-mpl-update')

    return fig
