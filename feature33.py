import matplotlib.pyplot as plt

from mplslide import FONT


def feature33_mosaic():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - Mosaic',
             fontproperties=FONT, color='C0', fontsize=72)

    return fig


def feature33_2():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.3 Feature Highlight - 2',
             fontproperties=FONT, color='C0', fontsize=72)

    return fig


def slides():
    return (
        feature33_mosaic(),
        feature33_2(),
    )
