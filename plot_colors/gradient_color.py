

def color_gradient(rgb_start, rgb_end, n):
    """
    在两种 RGB 颜色之间生成 n 个渐变色（包含起始和结束颜色）

    参数:
        rgb_start: tuple(int, int, int)  如 (255, 0, 0)
        rgb_end:   tuple(int, int, int)  如 (0, 0, 255)
        n: int  生成颜色数量（>=2）

    返回:
        List[Tuple[int, int, int]]
    """
    if n < 2:
        raise ValueError("n 必须 >= 2")

    gradient = []
    for i in range(n):
        t = i / (n - 1)  # 插值系数 [0,1]
        r = int(rgb_start[0] + t * (rgb_end[0] - rgb_start[0]))
        g = int(rgb_start[1] + t * (rgb_end[1] - rgb_start[1]))
        b = int(rgb_start[2] + t * (rgb_end[2] - rgb_start[2]))
        gradient.append((r, g, b))

    return gradient

def color_gradient_norm(rgb_start, rgb_end, n):
    colors = color_gradient(rgb_start, rgb_end, n)
    return [(r/255, g/255, b/255) for r, g, b in colors]


if __name__ == "__main__":
    colors = color_gradient_norm((255, 0, 0), (0, 0, 255), 5)
    print(colors)
