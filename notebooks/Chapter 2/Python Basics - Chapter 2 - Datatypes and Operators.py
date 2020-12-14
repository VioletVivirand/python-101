# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] id="dmiY5io3vjmu"
# # Chapter 2 - Datatypes and Operators：資料型態與運算子

# + [markdown] id="3hHJ1yHgSoCR"
# 電腦發展快速所帶來的直接效益，就是計算量大大地增加了，而計算正是一個讓電腦幫我們做事情的入門點。本章節我們先從簡單的數學運算開始介紹 Python 的功能、以及一些不同的資料型態 (Datatype)。

# + [markdown] id="X6UpX9khvvBJ"
# ## Numbers：數字類的資料型態

# + [markdown] id="n0r1JDXIU3_m"
# 數字的資料型態有兩種，分別是：
#
# * `int`：整數 (Integer)
# * `float`：浮點數 (Float)
#
# References:
#
# * [Numbers - Python Documentation](https://docs.python.org/3/tutorial/introduction.html#numbers)
# * [int - Python Documentation](https://docs.python.org/3/library/functions.html#int)
# * [float - Python Documentation](https://docs.python.org/3/library/functions.html#float)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 893, "status": "ok", "timestamp": 1607329666644, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="mwWzZc6VFxzA" outputId="5289e15d-45ba-41d0-cf5e-1124f7239784"
# 試著顯示數字在畫面上
print(1)
print(2.0)

# + [markdown] id="0KjO9RJ3GISo"
# 配合 `type()` 函式，我們可以觀察不同樣態的數字，分別是什麼資料型態。

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1010, "status": "ok", "timestamp": 1606721974334, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="GTkRlVIwFzkv" outputId="1b12aa47-028c-4f15-df06-de69402d4995"
# 顯示整數 (int) 的資料型態
print(type(1))
# 顯示浮點數 (float)的資料型態
print(type(2.0))

# + [markdown] id="7OuiLd1VFu0I"
# ### Opeators：運算子

# + [markdown] id="pt2vA0CVTTdG"
# 程式是由許多的表達式 (Expression) 組成的，最直覺的表達式就是使用各種運算子執行四則運算：加 `+`、減 `-`、乘 `*`、除 `/`。除此之外，還有一些特別的運算：
#
# References:
#
# * [Mapping Operators to Functions - Python Documentation](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1703, "status": "ok", "timestamp": 1607330012732, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="pQf-bsE2vTzl" outputId="239f9b6d-3a14-4b71-df02-033e9a9c838a"
print(1 + 2)  # Addition：加法運算
print(4 - 3)  # Substraction：減法運算
print(5 * 6)  # Multiplication：乘法運算
print(8 / 7)  # Division：除法運算

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1059, "status": "ok", "timestamp": 1606716571900, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="kWheV8mhwmIX" outputId="e64c8196-025a-4b9f-8ffe-2b74f58f9b9e"
print(2 ** 3)  # Exponentiation：指數運算
print(7 // 6)  # Division：整除運算

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 695, "status": "ok", "timestamp": 1606716605675, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="mbQFejWBxTwr" outputId="ec54882b-864d-48c8-e6f9-9dfca609f4ae"
print(10 % 3)  # Modulo：求餘數

# + [markdown] id="r6LpW04YWmJA"
# 也可以搭配括號 `()` 執行。

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1314, "status": "ok", "timestamp": 1606716985868, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="qrjclaxLxY3m" outputId="ec4cc7b9-0a89-4b2b-f356-c69cccbc9d9c"
# 小括號 () 的應用
print(1 + 2 * 3)    # 沒有小括號
print((1 + 2) * 3)  # 使用小括號

# + [markdown] id="waG9RNiGWxV2"
# 如果需要表示數值之間的相對關係，可以使用比較運算子，而比較的結果將會以布林值 (Boolean) 回傳
#
# > 備註：不認識布林值？不用擔心，我們很快地會在下一個小節提到布林值！

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 810, "status": "ok", "timestamp": 1606717032666, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="KphgJknWyz6O" outputId="00f8cdee-90be-40d5-bca4-987fdb387570"
print(5 > 3)    # 大於
print(1 >= 10)  # 大於或等於

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1009, "status": "ok", "timestamp": 1606717061023, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="SICT2VB8zAj6" outputId="95a04877-9447-4246-e0c7-e89f60e75c04"
print(7 < 4)   # 小於
print(2 <= 9)  # 小於或等於

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 509, "status": "ok", "timestamp": 1606717163191, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="DgawRXrlzLNV" outputId="c9f26117-3dad-4347-ba01-c2c14bc13946"
print(3 == 1 + 2)  # 等於
print(8 != 9)      # 不等於

# + [markdown] id="PHlv9G4SzvLF"
# ### 浮點數計算的陷阱

# + [markdown] id="xaH4Zy97YKOJ"
# 由於大部分的電腦的浮點數計算都是透過二進位小數來表示，而目前幾乎所有浮點數的計算都採用了 IEEE 754 的標準來執行，所以可能會顯示近似值：

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 817, "status": "ok", "timestamp": 1607398832383, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="HtXaS3t37bWj" outputId="dee97ed8-118b-427e-fed9-243cf68505d5"
print(0.1 + 0.1 + 0.1)

# + [markdown] id="2Ibv2h97b9dk"
# Python 官方文件中也提供了解決方法，大致羅列：
#
# * 採用 [Decimal module](https://docs.python.org/3/library/decimal.html#module-decimal)
# * 採用 [Fractions module](https://docs.python.org/3/library/fractions.html#module-fractions)
# * （推薦）採用 [Numpy](https://numpy.org/) / [Scipy](https://scipy.org/)
#
# References:
#
# * [Floating Point Arithmetic: Issues and Limitations - Python documentation](https://docs.python.org/3/tutorial/floatingpoint.html)
#    * [浮點數運算：問題與限制](https://docs.python.org/zh-tw/3/tutorial/floatingpoint.html)
# * [IEEE 754 - Wikipedia](https://en.wikipedia.org/wiki/IEEE_754)
#    * [IEEE 754 - 維基百科](https://zh.wikipedia.org/zh-tw/IEEE_754)

# + [markdown] id="6cxTFYYjABDa"
# ## Booleans：布林值，標示是、否的資料型態

# + [markdown] id="ZzYeX7s-BDLy"
# 布林值用 `True` 表示真值、而用 `False` 表示假值。
#
# 布林值也是整數 (int) 型態的子集合，用 `0` 表示 `False`，而其他的數值均表示 `True`。
#
# > 備註：初學的時候最容易忘記的是布林值的 `True` 跟 `False` 的首字都是大寫！
#
# References:
#
# * [bool - Python documentation](https://docs.python.org/3/library/functions.html#bool)
# * [Truth Table - Wikipedia](https://en.wikipedia.org/wiki/Truth_table)
#    * [真值表 - 維基百科](https://zh.wikipedia.org/zh-tw/%E7%9C%9F%E5%80%BC%E8%A1%A8)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 790, "status": "ok", "timestamp": 1607399787486, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="LjwG2y7efhG7" outputId="255ba635-3b10-4ba3-a4d0-c3e1d618d7d6"
bool(0.01)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 736, "status": "ok", "timestamp": 1607399686002, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="rdxDij7wAwvy" outputId="737d3d54-e52a-48ce-ef41-30b86b022aad"
print(True)   # 是
print(False)  # 否
# -

print(type(True))

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1056, "status": "ok", "timestamp": 1607399969411, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="2VPLB5oPAy6f" outputId="61c67bac-5d17-47b9-e293-8609f9830c52"
print(True == 1)   # 驗證 0 以外的數字是否代表 True
print(False == 0)  # 驗證 0 以外的數字是否代表 False

# + [markdown] id="FMWOLKalgUz0"
# 在 Python 中，有兩個類似的運算子，是可以用來比較兩物件是否相等的：
#
# * `==`：相等 (Equality) 運算子
# * `is`：標示 (Identity) 運算子
#
# 若要用一個表達式與布林值相比較，正確的用法應該是用標示運算子 `is` 來比較（即使兩者回傳的結果相當，仍會有些許的效率差異）。

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1213, "status": "ok", "timestamp": 1606722963853, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="BHb_Yk6mE26n" outputId="fc0e3c45-d26b-4456-a6db-fd21f5a82422"
# 用 `is` 來驗證兩表達式是否相等
print((3 + 1 == 4) is True)
print((3 + 1 == 4) == True)  # 此方式執行較慢

# + [markdown] id="stHJ2InVzk9n"
# 而標示運算子除了 `is`（是）以外，常用的還有 `or`（或）與 `not`（非）：

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1718, "status": "ok", "timestamp": 1606877864961, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="JEY-yiInYGcK" outputId="2a2e6422-3522-45c4-97ef-1ee6f0f5c53a"
# not 的用法：將真偽逆轉
print(not(True) is False)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1162, "status": "ok", "timestamp": 1606877881312, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="-JQeT5EbYkJU" outputId="0b7f208d-e1b6-4529-8b64-afbf2a026d46"
# or 的用法：任意表達式為真，即為真
print(True or False)

# + [markdown] id="qwpCcOnoYp7S"
# ## Strings：字串的資料型態

# + [markdown] id="TpH4Sd4Pdkhf"
# 若需要表達一串字元，可以將字元至於成對單引號（`'`, Single quote）或是雙引號（`"`, Double quote）之中。型別名稱為 `str`。
#
# 而若有特殊符號需作為字串表示時，可以使用倒斜線（`\`, Backslash） 作為「逃脫字元 (Escape character)」，讓逃脫字元之後的字元被視為一般字元來顯示。
#
# References:
#
# * [Text Sequence Type — str - Python Documentation](https://docs.python.org/3/library/stdtypes.html#textseq)
# * [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings)

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1723, "status": "ok", "timestamp": 1606878735926, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="OjzNKl9NbwIc" outputId="3d34eb53-fe65-435e-f937-bdace9c0c027"
print("Hello world!")        # 試著建立一個字串物件
print(type("Hello world!"))  # 驗證物件是否為字串

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1410, "status": "ok", "timestamp": 1606878830489, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="sGLbiGb6b6cJ" outputId="124684e2-8025-422c-a813-be201c8a2a49"
print('We can also use single quotes')  # 使用成對單引號 '' 來建立字串
print("Also, double quotes are fine")   # 使用成對雙引號 "" 來建立字串

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 967, "status": "ok", "timestamp": 1607406104075, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="rX7QN-yd2ugO" outputId="55db34e5-6ea8-402d-b5b5-1b0bbf6114d2"
# 逃脫字元
# 範例：在使用雙引號的字串裡顯示雙引號
print("Hey, \"Vivi\" is my name. Don't forget!")

# + [markdown] id="_GADkSNz3s4b"
# 若是要建立多行的字串，可以使用三個重複的單引號或雙引號來建立字串物件：

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("""This is an one-line string""")
print("""And these are
multiline strings
""")  # ''' also works!

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 多行字串常見的用途，是作為函式或是方法的文件字串 (Docstrings)：

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 搭配內建函式 help()，我們將可以查看物件的說明文件內容！
# 例：查看 print() 的用法
help(print())


# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 接著我們來驗證一下 Docstrings 的製作
def foo():
    """
    This is the docstrings
    """
    pass

help(foo)

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# > 看不懂 `def` 在做什麼嗎？其實就是建立一個函式。不知道為什麼這樣用？別用擔心，後面的章節會講解到！

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# ### 索引 (Indexing) 與分割 (slicing) 字串

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 在 Python 中，並沒有單一字元的 `char` 型態，而 `str` 字串型態可以視為多個單一字元的集合，所以可以從中擷取部分的內容。
#
# 用來指定擷取的內容位置是索引值 (Index)。在電腦程式的世界裡，通常第一個物件的索引值都是 `0`，之後的索引值則為 `1`, `2`, `3`......。Python 還有提供由後往前數的功能，而最後一個字元往前算的索引值則為 `-1`, `-2`, `-3`......。
#
# 指定索引值的格式為：`[start:stop:step]`，其中：
#
# * `start`：欲擷取字串中首字的索引值
# * `stop`：欲擷取字串中末字的索引值 + 1（也就是擷取的內容不包含 `stop` 位置的字元），此值可忽略
# * `step`：從擷取首字的位置起算，每隔幾個字元擷取一次，預設為 `1`，此值可忽略
#

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 試著指定 start 索引值來取得字串中的單一字元
print("String"[3])
print("String"[-3])

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 試著指定 start 以及 stop 的索引值，來擷取數個字元
print("String"[2:6])

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("String"[:3])  # 若不指定 start，則預設從第一個字元開始擷取
print("String"[2:])  # 若不指定 stop，則預設擷取到最後一個字元

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 試著指定 step
print("String"[1:6:2])
print("String"[1::2])  # 可以不指定 start 或 stop 的任意一項

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# ### 字串相關小技巧

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 在顯示字串時，可以將字串用不同的方式組合在一起，提高閱讀性：

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("Hello " + "world!")  # 多個字串可以用 + 號連接成一個字串
print("Hello ""world!")     # 可以將字串連續放置在 print() 函式內
print("Hello", "world!")    # 字串間如果用逗號 "," 隔開，則在顯示時會自動在兩倆之間加上空格

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 而使用 `in`: 包含測試運算子，可以驗證某字串是否包含在某個字串之內

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print('lo' in "Hello")

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# ### 字串方法

# + [markdown] colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
# 字串帶有一些內建的方法 (methods) 可以使用，例如大小寫轉換、尋找字元、取代、去除字串內的空白字元⋯⋯等等。
#
# > 「方法 (methods)」容易與「函式 (functions)」稍微產生混淆。下一個章節我們會把這兩個要素放在一起講解，現在讓我們先學會操作一些實用的方法吧！

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("Hello world!".upper())  # 將字串轉換為大寫
print("Hello world!".lower())  # 將字串轉換為小寫

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("string".find('ring'))  # 在字串中，搜尋特定字串第一次出現的位置的索引值

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("string".replace("ng", "ke"))  # 將字串取代為另一個字串

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("    string    ".strip() + "<EOL>")   # 消除字串左側與右側的所有空格
print("    string    ".lstrip() + "<EOL>")  # 消除字串左側的所有空格
print("    string    ".rstrip() + "<EOL>")  # 消除字串右側的所有空格

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("1,1,2,3,5,8,13,21".split(","))  # 將字串以特定字元為界線，將其分割成許多分開的字串

# + colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1311, "status": "ok", "timestamp": 1606888701236, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}, "user_tz": -480} id="m6-SDtwLcRlU" outputId="ecf54006-4c54-4950-c482-7fb01cef45ba"
print("-".join("ENGLISH"))  # 將字串中的每個字元，用指定的字元相互連接起來
