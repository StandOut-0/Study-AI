from matplotlib import pyplot as plt

if False:
    plt.plot(  ['hong', 'kim', 'heo'], [80, 90, 75], 
         color='red', marker='o', linestyle='-', linewidth=2, markerfacecolor='blue', markersize=10)

    plt.bar(['hong', 'kim', 'heo'], [80, 90, 75], 
        color='red', edgecolor='black', width=2)
    
    plt.hist([80, 90, 75], 
    bins=8, color='red', histtype='bar', facecolor='blue')

weight1 = [80, 90, 75]
weight2 = [80, 90, 75]
plt.scatter(weight1, weight2, color='red', edgecolors='black')

plt.show()

