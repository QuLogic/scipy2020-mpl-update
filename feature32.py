import matplotlib.pyplot as plt

from mplslide import BULLET, FONT


def feature32_overview():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

    fig.text(0.05, 0.85, '3.2 Feature Highlights',
             fontproperties=FONT, color='C0', fontsize=72)

    fig.text(0.05, 0.8, f'''\
{BULLET} Unit converters recognize subclasses
{BULLET} $pyplot.imsave$ accepts metadata and PIL options
{BULLET} $FontProperties$ accepts $os.PathLike$
{BULLET} bar3d lightsource shading
{BULLET} Gouraud-shading alpha channel in PDF backend
{BULLET} Improvements in Logit scale ticker and formatter
{BULLET} rcParams for axes title location and color
{BULLET} 3-digit and 4-digit hex colors
{BULLET} Added support for RGB(A) images in pcolorfast
{BULLET} Shifting errorbars''',
             fontproperties=FONT, alpha=0.7, fontsize=48,
             verticalalignment='top')
    """
    import matplotlib.pyplot as plt

    # Use old kerning values:
    plt.rcParams['text.kerning_factor'] = 6
    fig, ax = plt.subplots()
    ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
    ax.set_title('Before (text.kerning_factor = 6)')
    """

    # Use new kerning values:
    # plt.rcParams['text.kerning_factor'] = 0
    # fig, ax = plt.subplots()
    # ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
    # ax.set_title('After (text.kerning_factor = 0)')

    return fig


def slides():
    return (
        feature32_overview(),
    )
