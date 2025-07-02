"""
Latexify - Modern matplotlib formatting for LaTeX documents

Easy-to-use utilities for creating publication-ready plots that integrate
seamlessly with LaTeX documents.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def latexify(fig_width=None, fig_height=None, columns=1, largeFonts=False):
    """
    Set up matplotlib for LaTeX-ready plots.
    
    Parameters
    ----------
    fig_width : float, optional
        Figure width in inches. Auto-calculated if None.
    fig_height : float, optional  
        Figure height in inches. Uses golden ratio if None.
    columns : int, default 1
        LaTeX document columns (1 or 2).
    largeFonts : bool, default False
        Use larger fonts for presentations.
        
    Examples
    --------
    >>> import latexify
    >>> latexify.latexify()
    >>> plt.plot([1,2,3], [1,4,2])
    >>> latexify.format_axes(plt.gca())
    >>> plt.savefig('plot.pdf')
    """
    
    # Calculate figure dimensions
    if fig_width is None:
        fig_width = 3.5 if columns == 1 else 7.0
        
    if fig_height is None:
        golden_ratio = (np.sqrt(5.0) - 1.0) / 2.0
        fig_height = fig_width * golden_ratio
    
    # Font sizes
    if largeFonts:
        font_size = 11
        tick_size = 10
    else:
        font_size = 9
        tick_size = 8
    
    # Modern matplotlib parameters
    params = {
        'figure.figsize': [fig_width, fig_height],
        'font.size': font_size,
        'axes.labelsize': font_size,
        'axes.titlesize': font_size,
        'xtick.labelsize': tick_size,
        'ytick.labelsize': tick_size,
        'legend.fontsize': tick_size,
        'font.family': 'serif',
        'font.serif': ['Computer Modern Roman'],
        'text.usetex': True,
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
        'axes.linewidth': 0.8,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.major.size': 3,
        'xtick.minor.size': 1.5,
        'ytick.major.size': 3,
        'ytick.minor.size': 1.5,
        'legend.frameon': False,
        'legend.numpoints': 1,
        'legend.scatterpoints': 1,
    }
    
    matplotlib.rcParams.update(params)


def format_axes(ax):
    """
    Clean up axes for publication quality.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to format.
    """
    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Lighten remaining spines
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Set tick properties
    ax.tick_params(colors='#666666', which='both')
    ax.tick_params(which='major', length=3)
    ax.tick_params(which='minor', length=1.5)
    
    # Only show ticks on left and bottom
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def save_fig(filename, fig=None, **kwargs):
    """
    Save figure with optimal settings.
    
    Parameters
    ----------
    filename : str
        Output filename with extension.
    fig : matplotlib.figure.Figure, optional
        Figure to save. Uses current figure if None.
    **kwargs
        Additional savefig arguments.
    """
    defaults = {
        'bbox_inches': 'tight',
        'pad_inches': 0.05,
        'dpi': 300,
        'facecolor': 'white'
    }
    defaults.update(kwargs)
    
    if fig:
        fig.savefig(filename, **defaults)
    else:
        plt.savefig(filename, **defaults)


# Convenience function for quick setup
def setup(columns=1, largeFonts=False):
    """Quick setup for latexify plots."""
    latexify(columns=columns, largeFonts=largeFonts)


def reset():
    """Reset matplotlib to defaults."""
    matplotlib.rcdefaults()