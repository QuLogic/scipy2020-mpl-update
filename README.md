Matplotlib Project Update for SciPy 2020
========================================

This repository contains code to create the presentation for the Matplotlib
project update at SciPy 2020.

Requirements
------------

* Python 3.7+
* NumPy
* Matplotlib >= 3.3.0rc1
* A git checkout of the `matplotlib` source code, to produce the timeline.
* The title fonts, currently Carlito to match the Matplotlib logo.

Optionally, you may also make available:

* [`qpdf`](http://qpdf.sourceforge.net/), to linearize the final PDF.
* Matplotlib built and installed from [this Pull
  Request](https://github.com/matplotlib/matplotlib/pull/17832), so that the
  links in the PDF work.

Building
--------

The slides can be created by running:

```bash
$ ./make.py /path/to/matplotlib/checkout
```

which will produce `slides.pdf` directly from Matplotlib and
`scipy2020-mpl-update.pdf` as either a copy or a linearized version, depending
on whether `qpdf` is installed.

Overview
--------

Some general setup is contained in `mplslide.py`, namely setting slide size,
picking the font Carlito, and headings and other shortcut functions. Other
styling is mostly consistent, but usually set in the individual files.

All slides are produced in the remaining Python files:

* `title.py`: The title page.
* `news.py`: General news.
* `timeline.py`: A timeline of releases.
* `feature32.py`: Feature highlights for Matplotlib 3.2.0.
* `feature33.py`: Feature highlights for Matplotlib 3.3.0.
* `plan.py`: Future plans.
