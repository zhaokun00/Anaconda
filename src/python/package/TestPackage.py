"""
包是一种管理python模块命名空间的形式,采用"点模块名称"
比如一个模块的名称是A.B,那么它表示一个包A中的子模块B
就好像使用模块的时候,不用担心模块之间的全局变量相互影响一样,采用点模块名称这种形式也不用担心不同库之间的模块重名的现象

这里给出了一种可能的包结构
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

在导入一个包的时候,python会根据sys.path中的目录来寻找这个包中包含的子目录
目录中只有包含一个叫做__init__.py的文件才会被认作是一个包,主要是为了避免一些烂俗的名字
简单的情况就是放一个空的__init__.py

用户可以每次只导入一个包里面的特定的模块,例如:

import sound.effects.echo
这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

还有一种导入子模块的方法是:
from sound.effects import echo
这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
echo.echofilter(input, output, delay=0.7, atten=4)

还有一种变化就是直接导入一个函数或者变量:
from sound.effects.echo import echofilter

"""
import sound.filters.filter
import sys

sound.filters.filter.filter()

print("路径:",sys.path)