from .loader import load_styles
    
_STYLES = load_styles()

class PlotStyle:
    def __init__(self, style_name:str):
        if style_name not in _STYLES:
            raise NotImplementedError(f"{style_name} is not supported yet")

        self._style_name = style_name
        self._config = _STYLES[style_name]

    @property
    def style_name(self):
        return self._style_name
    
    @property 
    def all_colors(self):
        return self._config['colors']
    
    def get_colors(self, n:int):
        colors = self._config['colors']
        if n > len(colors):
            raise ValueError(f"n must be less than {len(colors)}")
        return colors[:n]
    
    @property
    def matplotlib_rcParams(self):
        # 取出除了 "colors" 之外的所有参数
        rc = {}
        
        for k,v in self._config.items():
            if k == "colors":
                continue
            if not isinstance(v,dict):
                raise TypeError(f"rcParams group '{k}' must be a dict")
            rc.update(v)
        return rc
    
    def get_matplotlib_rcParams_specific(self, param_name):
        return self._config[param_name]
    
if __name__ == "__main__":
    simple_style = PlotStyle("Simple")
    print("\nCurrent style is", simple_style.style_name)
    
    print("\nGet all colors:")
    print(simple_style.all_colors)

    print("\nGet first 5 colors:")
    print(simple_style.get_colors(5))

    print("\nGet specific parameters:")
    print(f"font: {simple_style.get_matplotlib_rcParams_specific("font")}")
    print(f"dpi: {simple_style.get_matplotlib_rcParams_specific("dpi")}")

    print("\nGet all parameters:")
    print(simple_style.matplotlib_rcParams)
    

