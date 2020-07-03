from mplslide import new_slide, slide_heading


CODE = dict(verticalalignment='top', fontsize=40, fontfamily='monospace')


def identify_axes(ax_dict):
    kw = dict(ha='center', va='center', fontsize=48, color='darkgrey')
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)


def mosaic():
    example1 = """[
    ['A', 'B'],
    ['C', 'D'],
]"""
    example2 = """
    '''
    A.C
    BBB
    .D.
    '''"""

    for text in [example1, example2]:
        fig = new_slide()

        slide_heading(fig, '3.3 Feature: subplot_mosaic')

        fig.text(0.05, 0.8, f'plt.figure().subplot_mosaic({text})', **CODE)

        ax_dict = fig.subplot_mosaic(eval(text.lstrip()))
        identify_axes(ax_dict)

        # Re-arrange to not overlay title and code.
        fig.subplots_adjust(left=0.4, top=0.7, right=0.97)

        yield fig


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


def slides():
    return (
        axline(),
        *mosaic(),
    )
