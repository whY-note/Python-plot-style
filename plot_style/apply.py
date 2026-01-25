'''
该文件中的函数负责将styles应用到matplotlib当中
'''
# import matplotlib as mpl
import matplotlib.pyplot as plt
from .PlotStyle import PlotStyle
from cycler import cycler

def apply_style(style_name: str):
    style = PlotStyle(style_name)

    plt.rcParams.update(
        style.matplotlib_rcParams
    )

    plt.rcParams["axes.prop_cycle"] = cycler(color = style.all_colors)

