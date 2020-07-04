import numpy as np
import matplotlib.pyplot as plt

from mplslide import new_slide, slide_heading


CODE = dict(verticalalignment='top', fontsize=40, fontfamily='monospace')


def axline():
    fig = new_slide()

    slide_heading(fig, '3.3 Feature: axline for infinite lines')

    fig.text(0.05, 0.8, """\
fig, ax = plt.subplots()
ax.axline((0.1, 0.1), slope=5, color='C0')
ax.axline((0.1, 0.2), (0.8, 0.7), color='C3')
    """, **CODE)

    ax = fig.add_axes((0.1, 0.1, 0.8, 0.5))

    ax.axline((0.1, 0.1), slope=5, color='C0', lw=3, label='by slope')
    ax.axline((0.1, 0.2), (0.8, 0.7), color='C3', lw=3, label='by points')

    ax.legend()

    return fig


def identify_axes(ax_dict):
    kw = dict(ha='center', va='center', fontsize=48, color='darkgrey')
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)


def mosaic():
    example1 = """
    '''
    A.C
    BBB
    .D.
    '''"""
    example2 = """[
    ['.', 'histx'],
    ['histy', 'scat'],
]"""

    for text in [example1, example2]:
        fig = new_slide()

        slide_heading(fig, '3.3 Feature: subplot_mosaic')

        fig.text(0.05, 0.8, f'plt.figure().subplot_mosaic({text})', **CODE)

        ax_dict = fig.subplot_mosaic(eval(text.lstrip()),
                                     # Don't overlay title and code.
                                     gridspec_kw=dict(left=0.3, top=0.7,
                                                      right=0.97))
        identify_axes(ax_dict)

        yield fig


def sharing():
    fig = new_slide()

    slide_heading(fig, '3.3 Feature: post-hoc Axes sharing')

    fig.text(0.05, 0.8, """\
axd['histx'].sharex(axd['scat'])
axd['histy'].sharey(axd['scat'])""", **CODE)

    np.random.seed(0)
    x = np.random.random(100) * 100 + 20
    y = np.random.random(100) * 50 + 25
    c = np.random.random(100) - 0.5

    with plt.rc_context({'xtick.labelsize': 20, 'ytick.labelsize': 20}):
        axd = fig.subplot_mosaic([['.', 'histx'], ['histy', 'scat']],
                                 gridspec_kw={'width_ratios': [1, 7],
                                              'height_ratios': [2, 7],
                                              'top': 0.65})

        im = axd['scat'].scatter(x, y, c=c, cmap='RdBu', picker=True)
        fig.colorbar(im, ax=[axd['scat'], axd['histy']],
                     orientation='horizontal')

        _, _, patchesx = axd['histx'].hist(x)
        _, _, patchesy = axd['histy'].hist(y, orientation='horizontal')

    axd['histy'].invert_xaxis()
    axd['histx'].sharex(axd['scat'])
    axd['histy'].sharey(axd['scat'])

    return fig


def slides():
    return (
        axline(),
        *mosaic(),
        sharing(),
    )
