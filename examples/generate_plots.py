#!/usr/bin/env python3
"""Generate plots for LaTeX examples"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os
sys.path.append('..')
import latexify

def create_plots():
    os.makedirs('plots', exist_ok=True)
    x = np.linspace(0, 2*np.pi, 100)
    
    # Default matplotlib (for comparison)
    latexify.reset()
    plt.figure(figsize=(5, 3.5))
    plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
    plt.plot(x, np.cos(x), 'r-', linewidth=2, label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/default.pdf', bbox_inches='tight')
    plt.close()
    
    # Article single column
    latexify.latexify(columns=1)
    plt.figure()
    plt.plot(x, np.sin(x), 'b-', label=r'$\sin(x)$')
    plt.plot(x, np.cos(x), 'r-', label=r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.legend()
    latexify.format_axes(plt.gca())
    latexify.save_fig('plots/article_single.pdf')
    plt.close()
    
    # Article double column
    latexify.latexify(columns=2)
    plt.figure()
    plt.plot(x, np.sin(x), 'b-', label=r'$\sin(x)$')
    plt.plot(x, np.cos(x), 'r-', label=r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.legend()
    latexify.format_axes(plt.gca())
    latexify.save_fig('plots/article_double.pdf')
    plt.close()
    
    # IEEE format
    latexify.latexify(fig_width=3.4, fig_height=2.3)
    plt.rcParams.update({'font.size': 8})
    plt.figure()
    plt.plot(x, np.sin(x), 'b-', label=r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\sin(x)$')
    latexify.format_axes(plt.gca())
    latexify.save_fig('plots/ieee_single.pdf')
    plt.close()
    
    # ACM format
    latexify.latexify(fig_width=3.3, fig_height=2.2)
    plt.rcParams.update({'font.size': 9})
    plt.figure()
    plt.plot(x, np.sin(x), 'b-', label=r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\sin(x)$')
    latexify.format_axes(plt.gca())
    latexify.save_fig('plots/acm_single.pdf')
    plt.close()
    
    print("All plots generated successfully!")

if __name__ == "__main__":
    create_plots()