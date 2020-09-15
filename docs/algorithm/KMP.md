# 字符串匹配算法：KMP

Knuth–Morris–Pratt（KMP）算法是一种改进的字符串匹配算法，

它的核心是利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的

它的时间复杂度是 O(m+n)


## 解决问题
假设现在我们面临这样一个问题：有一个文本串S，和一个模式串P，现在要查找P在S中的位置，怎么查找呢？


## 常规操作 - 暴力破解法

如果用暴力匹配的思路, 并假设现在文本串S匹配到 i 位置, 模式串P匹配到 j 位置, 则有:

::: tip 算法过程
如果当前字符匹配成功,即<b class="vue-color grey-bg">S[i] == P[j]</b>，则<b class="vue-color grey-bg">i++, j++</b>，继续匹配下一个字符;

如果失配, 即 <b class="vue-color grey-bg">S[i]! = P[j]</b> , 令 <b class="vue-color grey-bg">i = i - (j - 1), j = 0</b>

相当于每次匹配失败时, i 回溯, j 被置为0
:::

具体流程如下：

举个例子:
```python
# 给定文本串
S = "BBC ABCDAB ABCDABCDABDE"
# 模式串
P = "ABCDABD"
```

现在要拿模式串P去跟文本串S匹配, 整个过程如下所示：

1. S[0]为B，P[0]为A:
* S[1]跟P[0]不匹配: <b class="vue-color grey-bg">S[i]! = P[j],令i = i - (j - 1),j = 0</b>
* S[1]跟P[0]匹配: 模式串要往右移动一位 <b class="vue-color grey-bg">i=1, j=0</b>

2. S[1]跟P[0]:
* S[1]跟P[0]不匹配: <b class="vue-color grey-bg">S[i]! = P[j],令i = i - (j - 1),j = 0</b>
* S[1]跟P[0]匹配: 模式串不断的往右移动一位 <b class="vue-color grey-bg">i=2, j=0</b>

3. 直到S[4]跟P[0]匹配成功 <b class="vue-color grey-bg">i=4, j=0</b>
此时按照上面的暴力匹配算法的思路，转而执行第①条指令:

<b class="grey-bg">如果当前字符匹配成功(即S[i] == P[j]), 则i++, j++,可得S[i]为S[5],P[j]为P[1],即接下来S[5]跟P[1]匹配(i=5, j=1)</b>

4. S[5]跟P[1]匹配成功，继续执行第①条指令:

<b class="grey-bg">如果当前字符匹配成功,即S[i] == P[j],则i++, j++, 得到S[6]跟P[2]匹配(i=6，j=2)如此进行下去</b>

5. 直到S[10]为空格字符，P[6]为字符D(i=10，j=6)，因为不匹配，重新执行第②条指令：

<b class="grey-bg">如果失配(S[i]! = P[j]),令i = i - (j - 1), j = 0，相当于S[5]跟P[0]匹配(i=5, j=0)</b>

6. 至此，我们可以看到，如果按照暴力匹配算法的思路，尽管之前文本串和模式串已经分别匹配到了<b class="vue-color">S[9], P[5]</b>

但因为<b class="vue-color">S[10]</b>跟<b class="vue-color">P[6]</b>不匹配，所以文本串回溯到<b class="vue-color">S[5]</b>

模式串回溯到<b class="vue-color">P[0]</b>，从而让<b class="vue-color">S[5]</b>跟<b class="vue-color">P[0]</b>匹配

而<b class="vue-color">S[5]</b>肯定跟<b class="vue-color">P[0]</b>失配。为什么呢？

因为在之前第4步匹配中，我们已经得知<b class="vue-color">S[5] = P[1] = B</b>，

而<b class="vue-color">P[0] = A</b>，

即<b class="vue-color">P[1] != P[0]</b>，

故<b class="vue-color">S[5]</b>必定不等于<b class="vue-color">P[0]</b>，所以回溯过去必然会导致失配。





