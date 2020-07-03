import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager


MPL_BLUE = '#11557c'
BULLET = '$\N{Bullet}$'
FONT = None
FIGSIZE = (19.2, 10.8)
DPI = 100


def check_requirements():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    if 'Carlito' not in matplotlib.font_manager.findfont('Carlito:bold'):
        sys.exit('Carlito font must be installed.')
    global FONT
    FONT = matplotlib.font_manager.FontProperties(family='Carlito',
                                                  weight='bold')


def new_slide(plain=False):
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    fig.mplslide_props = {'plain': plain}
    return fig


def slide_heading(fig, text):
    fig.text(0.05, 0.85, text, color='C0', fontproperties=FONT, fontsize=72)
