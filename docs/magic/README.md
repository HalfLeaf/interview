# 魔法Python

## 连接多个列表

```python
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    18         1         17.0     17.0      4.0      a = [1, 2]
    19         1          4.0      4.0      0.9      b = [3, 4]
    20         1          3.0      3.0      0.7      c = [5, 6]
    21                                               # 方法1
    22         1         14.0     14.0      3.3      d = sum((a, b, c), [])
    24                                               # 方法2  加法运算
    25         1          5.0      5.0      1.2      e = a+b+c
    27                                               # 方法3 使用itertools.chain()可迭代对象串联起来
    28         1         11.0     11.0      2.6      f = list(chain(a, b, c))
    30                                               # 方法4  使用 * 可以解包列表 ** 可解包字典
    31         1          4.0      4.0      0.9      g = [*a, *b, *c]
    33                                               # 方法5 列表推导式
    34         1         29.0     29.0      6.8      h =  [x for l in (a, b, c) for x in l]
    36                                               # 方法6  堆排序算法merge方法可以用于合并多个列表
    37         1        150.0    150.0     35.4      i = list(merge(a, b, c))
```

## 连接多个字典

```python
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19         1         16.0     16.0      4.8      a = {"a":1, "b":2, "c":3, "d":4}
    20         1          5.0      5.0      1.5      b = {"e":1, "f":2, "g":3, "h":4}
    21                                               # update 原地更新
    22         1         13.0     13.0      3.9      c = a.update(b)
    26                                               # 方法2  ** 可以解包字典，解包完后再使用dict或者{}合并
    27         1          9.0      9.0      2.7      e = dict(**a, **b)
    29                                               # 方法3 使用 itertools.chain()
                                                     # 通过 dict() 方式合并 传入的字典 元素必须是 String 类型的
    30         1         14.0     14.0      4.2      f =dict(chain(a.items(), b.items()))
    32                                               # 方法4  使用 collections.ChainMap()
    33         1        131.0    131.0     39.1      g = dict(ChainMap(a, b))
```

# 条件判断语法

* <on_true> if <condition> else <on_false>
* <condition> and <on_true> or <on_false>
* (<on_false>, <on_true>)[condition]
  
# 优雅的嵌套循环
```python
from itertools import product
list1 = range(1, 10)
list2 = range(2, 10)
list3 = range(3, 10)
for item1,item2,item3 in product(list1, list2, list3):
    print(item1+item2+item3)
```


