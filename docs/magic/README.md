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