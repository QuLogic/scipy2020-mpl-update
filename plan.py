from mplslide import BULLET, FONT, new_slide, slide_heading


def slides():
    fig = new_slide()

    slide_heading(fig, 'Release Plan')

    fig.text(0.05, 0.6, 'Next feature release: 3.4',
             fontproperties=FONT, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.5, f'{BULLET} September 2020',
             fontproperties=FONT, alpha=0.7, fontsize=56)
    fig.text(0.1, 0.4, f'{BULLET} Dropping Python 3.6 support',
             fontproperties=FONT, alpha=0.7, fontsize=56)

    return fig
