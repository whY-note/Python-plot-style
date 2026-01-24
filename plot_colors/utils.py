
def rgb2hex(rgb: tuple) -> str:
    '''
    convert rgb to hex

    Input: 
    rgb: tuple with 3 elements

    return: 
    hex: str
    '''
    if len(rgb) != 3:
        raise ValueError("rgb need tuple with 3 elements")

    for c in rgb:
        if not isinstance(c,int) or not (0 <= c <= 255):
            raise ValueError("each rgb value must be integer in [0, 255]")
    
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def hex2rgb(hex_str: str) -> tuple:
    '''
    convert hex to rgb

    Input: 
    hex: str, like '#ff0000'

    return: 
    rgb: tuple with 3 elements
    '''
    if not isinstance(hex_str, str):
        raise TypeError("hex_str must be a string")
    
    if len(hex_str) != 7 or not hex_str.startswith('#'):
        raise ValueError("hex_str must be like '#RRGGBB'.\n For example, hexstr='#ff0000'")

    try: 
        r = int(hex_str[1:3], 16)
        g = int(hex_str[3:5], 16)
        b = int(hex_str[5:7], 16)
        
    except ValueError:
        raise ValueError("hex_str contains invalid hex characters")

    return (r,g,b)

# test
if __name__ == "__main__":
    rgb = (255,0,0)
    hex_str = rgb2hex(rgb)
    print(hex_str)
    print(hex2rgb(hex_str))