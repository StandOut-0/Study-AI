import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path

def test_plot1():
    plt.plot([1,2,3,4,5])
    plt.show()
    
def test_plot2():
    x_data = [1,2,3,4,5]
    y_data = [1,2,3,4,5]
    plt.plot(x_data, y_data)
    plt.show()

def test_plot3():
    # reslove: 이것은 파일의 절대 경로를 반환합니다. parent: 이것은 파일의 상위 디렉토리를 반환합니다.
    script_dir = Path(__file__).resolve().parent
    font_path = script_dir.parent / "clova-all" / "clova-all" / "아름드리_꽃나무" / "나눔손글씨 아름드리 꽃나무.ttf"

    if not font_path.exists():
        raise FileNotFoundError(f"Font file not found: {font_path}")

    print(f"Using font file: {font_path}")
    font_prop = fm.FontProperties(fname=str(font_path), size=18)
    fm.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = font_prop.get_name()
    plt.rcParams["font.size"] = 16

    plt.plot([1, 2, 3, 4], [1, 4, 2, 3], color='pink', lw = 5, 
             marker="*", ms=15, mec = 'blue', mfc = 'r', linestyle=":")
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    # plt.title("한글 제목 테스트", fontproperties=font_prop)
    # plt.xlabel("x 축", fontproperties=font_prop)
    # plt.ylabel("y 축", fontproperties=font_prop)

    mpl.rc('font', family=font_prop.get_name(), size=16)
    mpl.rc('axes', unicode_minus=False)
    plt.title("한글 제목 테스트")
    plt.xlabel("x 축")
    plt.ylabel("y 축")

    plt.grid(False)
    plt.show()

def test_plot4():
    x = np.linspace(-np.pi, np.pi, 100)
    c = np.cos(x)
    plt.plot(x, c)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$1$'])
    plt.show()

def test_scatter():
    # x = np.linspace(0, 2 * np.pi, 100)
    x = np.random.rand(100)
    # y = np.sin(x)
    y = np.random.rand(100)
    s_size = np.random.randint(10, 1000, size=100)
    s_color = np.random.rand(100)
    plt.scatter(x, y, s=s_size, c=s_color)
    plt.show()

def test_multi_plot():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.legend(["sin", "cos"], loc = "upper right")

    plt.show()

def test_bar():
    x = [3, 4, 5, 6, 7]
    y = [4, 5, 6, 7, 8]
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    hatches = ['/', '\\', '|', '-', '+']
    # plt.bar(x, y)
    # plt.barh(x, y, alpha=0.5, xerr=2,color='orange',
    #         edgecolor='red')

    custom_labels = ["red", "blue", "green", "orange", "purple"]
    bars = plt.bar(x, y, color=colors, hatch=hatches)
    plt.gca().bar_label(bars, labels=custom_labels, padding=3)
    plt.ylim(0, 10)

    plt.show()


def test_stamplot():
    x = np.linspace(0, 2 * np.pi, 100)
    plt.stem(x, np.sin(x))
    plt.show()


def test_hist():
    f1 = plt.figure(figsize=(3, 6))
    x = np.random.rand(100)
    plt.hist(x, bins=10)
    plt.show()

def test_pie():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    plt.pie(sizes, explode=[0, 0.1, 0, 0],  labels=labels, autopct='%1.1f%%', 
            shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()  

def test_subplot():
    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    x = np.linspace(0, 2 * np.pi, 100)
    axes[0, 0].plot(x, np.sin(x))
    axes[0, 1].plot(x, np.cos(x))
    axes[1, 0].plot(x, np.cos(x))
    axes[1, 1].plot(x, np.sin(x))
 
    print(fig, id(fig))
    print(plt.gcf(), id(plt.gcf()))
    plt.tight_layout()
    plt.show()

def test_twinx():
    fig, ax0 = plt.subplots()
    ax1 = ax0.twinx()
    ax0.plot([10, 5, 3, 4, 5] ,color='red')
    ax1.plot([10, 20, 3, 40, 50], color='blue')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # test_plot1()
    # test_plot2()
    # test_plot3()
    # test_plot4()
    # test_scatter()
    # test_multi_plot()
    test_bar()
    # test_stamplot()
    # test_hist()
    # test_pie()
    # test_subplots()
    # test_twinx()