"""
Feature highlights for Matplotlib 3.2.0.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from mplslide import new_slide, slide_heading, annotate_pr_author


def feature32_bar3d():
    """
    Create slide for feature highlight of bar3d light source.
    """

    fig = new_slide()

    slide_heading(fig, '3.2 Feature: bar3d light source')

    # Plot two different light source angles.
    for i, angle in [(1, 90), (2, 0)]:
        # This example comes from the Pull Request adding this support:
        # https://github.com/matplotlib/matplotlib/pull/15099#issuecomment-523981989
        ax = fig.add_subplot(1, 2, i, projection="3d")

        ls = mcolors.LightSource(azdeg=45, altdeg=angle)
        cmap = plt.get_cmap("coolwarm")

        length, width = 3, 4
        area = length * width

        norm = mcolors.Normalize(0, area-1)

        x, y = np.meshgrid(np.arange(length), np.arange(width))
        x = x.ravel()
        y = y.ravel()
        dz = x + y

        color = cmap(norm(np.arange(area)))

        ax.bar3d(x=x, y=y, z=0,
                 dx=1, dy=1, dz=dz,
                 color=color, shade=True, lightsource=ls)

    annotate_pr_author(fig, 'fourpoints', pr=15099)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        feature32_bar3d(),
    )
