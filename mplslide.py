import sys

import matplotlib.font_manager


MPL_BLUE = '#11557c'
BULLET = '$\N{Bullet}$'
FONT = None


def check_requirements():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    if 'Carlito' not in matplotlib.font_manager.findfont('Carlito:bold'):
        sys.exit('Carlito font must be installed.')
    global FONT
    FONT = matplotlib.font_manager.FontProperties(family='Carlito',
                                                  weight='bold')
