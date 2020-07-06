"""
Feature highlights for Matplotlib 3.2.0.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from mplslide import new_slide, slide_heading


def feature32_bar3d():
    """
    Create slide for feature highlight of bar3d light source.
    """

    fig = new_slide()

    slide_heading(fig, '3.2 Feature: bar3d light source')

    for i, angle in [(1, 90), (2, 0)]:
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

        color = np.array([cmap(norm(i)) for i in range(area)])

        ax.bar3d(x=x, y=y, z=0,
                 dx=1, dy=1, dz=dz,
                 color=color, shade=True, lightsource=ls)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        feature32_bar3d(),
    )
