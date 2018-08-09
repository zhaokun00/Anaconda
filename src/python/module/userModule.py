
def print1():
    print("print1")
    return

def print2():
    print("print2")
    return

"""
    一个模块被另一个程序第一次引用时,其主程序将运行,如果我们想在模块被引入时,模块中的某一程序
    不执行,我们可以用__name__属性来使该程序仅在该模块自身运行时执行
    
"""

# 仅在当前文件中运行时,print语句才执行
if __name__ == '__main__':
    print("userModule")
