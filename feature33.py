from mplslide import new_slide, slide_heading


def feature33_mosaic():
    fig = new_slide()

    slide_heading(fig, '3.3 Feature Highlight - Mosaic')

    return fig


def feature33_2():
    fig = new_slide()

    slide_heading(fig, '3.3 Feature Highlight - 2')

    return fig


def slides():
    return (
        feature33_mosaic(),
        feature33_2(),
    )
