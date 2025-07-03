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
    print("✓ Default matplotlib")
    
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
    print("✓ Article single column")
    
    # Article double column - IMPROVED
    latexify.latexify(columns=2)
    fig, ax = plt.subplots(figsize=(6.5, 4.0))  # Better proportions
    ax.plot(x, np.sin(x), 'b-', linewidth=1.5, label=r'$\sin(x)$')
    ax.plot(x, np.cos(x), 'r-', linewidth=1.5, label=r'$\cos(x)$')
    ax.plot(x, 0.5*np.sin(2*x), 'g--', linewidth=1.5, label=r'$\frac{1}{2}\sin(2x)$')
    ax.set_xlabel(r'$x$ (radians)')
    ax.set_ylabel(r'Amplitude')
    ax.legend(loc='upper right')
    latexify.format_axes(ax)
    latexify.save_fig('plots/article_double.pdf', fig=fig)
    plt.close()
    print("✓ Article double column (improved)")
    
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
    print("✓ IEEE format")
    
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
    print("✓ ACM format")
    
    # Beamer presentation format
    latexify.latexify(largeFonts=True, fig_width=4.5, fig_height=3.0)
    plt.figure()
    plt.plot(x, np.sin(x), 'b-', linewidth=2, label=r'$\sin(x)$')
    plt.plot(x, np.cos(x), 'r--', linewidth=2, label=r'$\cos(x)$')
    plt.xlabel(r'$x$ (radians)')
    plt.ylabel(r'Amplitude')
    plt.legend(fontsize=12)
    latexify.format_axes(plt.gca())
    latexify.save_fig('plots/presentation_beamer.pdf')
    plt.close()
    print("✓ Beamer presentation")
    
    # 3 Subplots for different formats
    create_subplot_examples()
    
    print("All plots generated successfully!")

def create_subplot_examples():
    """Create 3 subplot examples for different document formats"""
    
    # Data for subplots
    x = np.linspace(0, 4*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x) 
    y3 = np.sin(x) * np.exp(-x/8)
    
    # Article format - 3 subplots across 2 columns
    latexify.latexify(columns=2)
    fig = plt.figure(figsize=(6.5, 6.0))
    
    # Subplot 1 (top left)
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(x, y1, 'b-', linewidth=1.5)
    ax1.set_title(r'(a) $\sin(x)$')
    ax1.set_xlabel(r'$x$')
    ax1.set_ylabel(r'$y$')
    latexify.format_axes(ax1)
    
    # Subplot 2 (top right)
    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(x, y2, 'r-', linewidth=1.5)
    ax2.set_title(r'(b) $\cos(x)$')
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'$y$')
    latexify.format_axes(ax2)
    
    # Subplot 3 (bottom, spanning both columns)
    ax3 = plt.subplot(2, 1, 2)
    ax3.plot(x, y3, 'g-', linewidth=1.5)
    ax3.set_title(r'(c) Damped sine: $\sin(x) \cdot e^{-x/8}$')
    ax3.set_xlabel(r'$x$ (radians)')
    ax3.set_ylabel(r'Amplitude')
    latexify.format_axes(ax3)
    
    plt.tight_layout()
    latexify.save_fig('plots/article_subplots.pdf', fig=fig)
    plt.close()
    print("✓ Article 3 subplots")
    
    # IEEE format - 3 subplots
    latexify.latexify(fig_width=3.4, fig_height=4.5)
    plt.rcParams.update({'font.size': 7})
    fig, axes = plt.subplots(3, 1, figsize=(3.4, 4.5))
    
    axes[0].plot(x[:50], y1[:50], 'b-', linewidth=1.2)
    axes[0].set_title('(a) Sine wave', fontsize=8)
    axes[0].set_ylabel(r'$\sin(x)$')
    latexify.format_axes(axes[0])
    
    axes[1].plot(x[:50], y2[:50], 'r-', linewidth=1.2)
    axes[1].set_title('(b) Cosine wave', fontsize=8)
    axes[1].set_ylabel(r'$\cos(x)$')
    latexify.format_axes(axes[1])
    
    axes[2].plot(x[:50], y3[:50], 'g-', linewidth=1.2)
    axes[2].set_title('(c) Damped sine', fontsize=8)
    axes[2].set_xlabel(r'$x$')
    axes[2].set_ylabel(r'$y$')
    latexify.format_axes(axes[2])
    
    plt.tight_layout()
    latexify.save_fig('plots/ieee_subplots.pdf', fig=fig)
    plt.close()
    print("✓ IEEE 3 subplots")
    
    # Beamer format - 3 subplots horizontal
    latexify.latexify(largeFonts=True, fig_width=8, fig_height=3)
    fig, axes = plt.subplots(1, 3, figsize=(8, 3))
    
    axes[0].plot(x[:40], y1[:40], 'b-', linewidth=2)
    axes[0].set_title('Sine', fontsize=14)
    axes[0].set_xlabel(r'$x$')
    axes[0].set_ylabel(r'$y$')
    latexify.format_axes(axes[0])
    
    axes[1].plot(x[:40], y2[:40], 'r-', linewidth=2)
    axes[1].set_title('Cosine', fontsize=14)
    axes[1].set_xlabel(r'$x$')
    latexify.format_axes(axes[1])
    
    axes[2].plot(x[:40], y3[:40], 'g-', linewidth=2)
    axes[2].set_title('Damped', fontsize=14)
    axes[2].set_xlabel(r'$x$')
    latexify.format_axes(axes[2])
    
    plt.tight_layout()
    latexify.save_fig('plots/beamer_subplots.pdf', fig=fig)
    plt.close()
    print("✓ Beamer 3 subplots")

if __name__ == "__main__":
    create_plots()