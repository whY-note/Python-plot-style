import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({

    # ===== 字体 =====
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "mathtext.fontset": "stix",   # 数学公式风格
    "font.size": 10,

    # ===== 图尺寸（论文单栏 / 双栏）=====
    "figure.figsize": (3.5, 2.6),   # 单栏 (inch)
    # "figure.figsize": (7.2, 2.6), # 双栏

    # ===== 分辨率 =====
    "figure.dpi": 300,
    "savefig.dpi": 300,

    # ===== 线条 =====
    "lines.linewidth": 1.2,
    "lines.markersize": 5,

    # ===== 坐标轴 =====
    "axes.linewidth": 1.0,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "axes.spines.top": True,
    "axes.spines.right": True,

    # ===== 刻度 =====
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 4,
    "ytick.major.size": 4,

    # ===== 图例 =====
    "legend.fontsize": 9,
    "legend.frameon": True,

    # ===== 保存 =====
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})

colors = [
    "#0072B2",  # Blue
    "#D55E00",  # Vermillion
    "#009E73",  # Bluish Green
    "#CC79A7",  # Reddish Purple
    "#E69F00",  # Orange
    "#56B4E9",  # Sky Blue   
    "#B2182B",  # Deep Red / Crimson
    "#F0E442",  # Yellow       
    "#999999",  # Gray          
    "#332288",  # Dark Blue     
    "#88CCEE",  # Light Cyan   
    "#000000",  # Black   
]

colors_blue = [
    "#0B3C5D",   # 深蓝（强调 / 最优方法）
    "#005F8F",   # 稳定蓝
    "#0072B2",   # 标准论文蓝（主线）
    "#4FA3D1",   # 浅蓝
    "#A7CFE8",   # 极浅蓝（参考 / baseline）
]

colors_purple_red = [
    "#4B1D6B",   # 深紫（强调 / 最优 / upper bound）
    "#6A1E9A",   # 紫色（稳定）
    "#8F3BB8",   # 紫红过渡（主线）
    "#C44E52",   # 论文红（对比 / 次主线）
    "#E6A4A4",   # 浅红（baseline / 参考）
]

colors_bgy = [
    "#0B3C5D",   # 深蓝（起点 / 强 / 最优）
    "#0F5E7A",   # 蓝青过渡
    "#1E7F8C",  # 青蓝
    "#2E9C89",   # 蓝绿
    "#3FAF7A",   # 绿
    "#6BBF59",   # 黄绿
    "#9FCC3A",   # 浅黄绿
    "#C9D94E",   # 柔黄
    "#E6E68A",   # 浅黄
    "#F2F2B0",   # 极浅黄（终点 / 弱 / baseline）
]