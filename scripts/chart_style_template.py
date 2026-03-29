"""
Reusable matplotlib chart style template for presentation graphics.

Usage: Copy this file to your project's graphics/src/chart_style.py
and customize COLORS and SERIES_COLORS with your brand palette.
"""
import matplotlib.pyplot as plt
import matplotlib as mpl


# Replace these with your brand colors from style_guide.md
COLORS = {
    'primary':       '#B31B1B',   # Main brand color (titles, emphasis)
    'secondary':     '#073949',   # Dark accent (headers, chart series)
    'accent_warm':   '#CF4520',   # Warm accent
    'accent_bright': '#E7751D',   # Highlights, current-state indicators
    'accent_gold':   '#FFC72C',   # Special emphasis (e.g., IP questions)
    'success':       '#6EB43F',   # Positive/growth indicators
    'info':          '#006699',   # Links, secondary data series
    'muted':         '#9FAD9F',   # Subdued elements
    'warm_gray':     '#A2998B',   # Inactive, disabled
    'light_bg':      '#F7F7F7',   # Light backgrounds, alt rows
    'text':          '#222222',   # Body text
    'alert':         '#EF4035',   # Risk, decline
}

# Map data series names to colors -- keeps charts consistent across slides
SERIES_COLORS = {
    # Customize for your presentation's data categories
    'Category A': COLORS['primary'],
    'Category B': COLORS['secondary'],
    'Category C': COLORS['accent_warm'],
    'Category D': COLORS['success'],
    'Category E': COLORS['info'],
    'Category F': COLORS['accent_bright'],
}


def apply_style():
    """Apply brand styling to all matplotlib charts."""
    mpl.rcParams.update({
        # Fonts -- uses system fonts, no installation needed
        'font.family': 'sans-serif',
        'font.sans-serif': ['Segoe UI', 'Helvetica Neue', 'Arial'],
        'font.size': 14,

        # Axes
        'axes.titlesize': 22,
        'axes.titleweight': 'bold',
        'axes.labelsize': 14,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.edgecolor': COLORS['warm_gray'],
        'axes.labelcolor': COLORS['text'],

        # Ticks
        'xtick.color': COLORS['text'],
        'ytick.color': COLORS['text'],

        # Background
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',

        # Grid
        'grid.color': '#DDDDDD',
        'grid.linestyle': '--',
        'grid.alpha': 0.7,

        # Legend
        'legend.frameon': False,
        'legend.fontsize': 12,

        # Export quality
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.3,
    })
