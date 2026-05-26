import os
import math
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def setup_korean_font(
                perfer_family_name: str = "NanumGothic",
                local_font_path: str = "./clova-all/clova-all/아름드리_꽃나무/나눔손글씨 아름드리 꽃나무.ttf",
                local_bold_path: str = "./clova-all/clova-all/아름드리_꽃나무/나눔손글씨 아름드리 꽃나무.ttf"):
    mpl.rc('axes', unicode_minus=False)
    mpl.rc('font', family=perfer_family_name)

    available = set(f.name for f in fm.fontManager.ttflist)
    if perfer_family_name not in available:
        if os.path.exists(local_font_path):
            font_prop = fm.FontProperties(fname=local_font_path, size=16)
            mpl.rcParams["font.family"] = font_prop.get_name()
            mpl.rcParams["font.size"] = 16
            fm.fontManager.addfont(local_font_path)
        elif os.path.exists(local_bold_path):
            font_prop = fm.FontProperties(fname=local_bold_path, size=16)
            mpl.rcParams["font.family"] = font_prop.get_name()
        else:
            print("Warning: Preferred font not found. Using default font.")

def test_line_detail():
    setup_korean_font()
    x = list(range(1, 6))
    y = [1, 2, 10, 4, 5]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='red', linewidth=5, marker='o', markersize=10, markevery=2)
    
    max_idx = max(range(len(y)), key=lambda i: y[i])
    max_x, max_y = x[max_idx], y[max_idx]
    plt.annotate('최댓값', xy=(max_x, max_y), xytext=(50, 20), color = 'red', 
                 fontweight = 'bold', fontsize = 32, textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='red'))

    for xi, yi in zip(x, y):
        if yi > 4:
            plt.text(xi, yi, f'{yi}', ha='center', va='bottom', color='blue', fontweight='bold', fontsize=32)
    plt.grid(True, linestyle = ":", alpha = 0.5)

    plt.show()
    

        

if __name__ == "__main__":
    test_line_detail()
