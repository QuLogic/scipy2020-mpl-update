import matplotlib.pyplot as plt

from mplslide import BULLET, FONT


def slides():
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
