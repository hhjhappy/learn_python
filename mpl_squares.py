import matplotlib.pyplot as plt 

def drawing():
    squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    imput_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''使用两组长度相同的列表绘制简单的折线图'''
    plt.plot(squares,imput_values,'go:', color='r')
    #设置图标标题，并给坐标轴加上标签
    plt.title("Square Numbers",fontsize=10,color='r')
    plt.xlabel("Value",fontsize = 20)
    plt.ylabel("Square of Value",fontsize = 20)
    #设置刻度标记的大小
    plt.tick_params(axis='both',labelsize=20)
    plt.show()


drawing()
