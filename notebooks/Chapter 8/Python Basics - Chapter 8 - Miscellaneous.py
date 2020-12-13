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

# + [markdown] id="rkJsyUdEtv48"
# # Chapter 8 - Miscellaneous - 其餘補充說明

# + [markdown] id="dygVGpmaC7Jz"
# 筆者用了七個章節來介紹了筆者認為一定要理解的知識，這個章節則將剩餘的部分集合起來。這部分的知識不能說不重要，只是對於初學時來說，有些觀念易於混淆，有些則比較少有機會使用，比較沒有馬上需要理解的急迫性，所以集合在此。
#
# 讀者們可以試著先嘗試理解，但如果不懂也沒有關係，等到前幾個章節都消化完、開發程式一段時間以後再回頭看，或許會更容易融會貫通！

# + [markdown] id="hH-rr92wt7iU"
# ## Tuples

# + [markdown] id="j8vfojiaEQn8"
# Tuples 也是一種序列 (Sequence) 物件，與串列 Lists 不一樣的是，Tuples 的內容不可以再被更新，也就是屬於不可變型態 (Immutable) 的物 件。
#
# 建立 Tuples 的方法為：將物件用小括號 (`()`, Parentheses) 集合。雖然與運算時用的括號是一樣的，但用途卻不同。
#
# > 備註：關於 Tuples 物件，官方並沒有翻譯，比較常見的大概是元組、數對一類的名詞。

# + colab={"base_uri": "https://localhost:8080/"} id="NYRaJP6LpjDV" executionInfo={"status": "ok", "timestamp": 1607863014703, "user_tz": -480, "elapsed": 811, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1c408742-1792-4756-fe37-d9ba5acafee0"
t = ("Bird", "Cat", "Dog")  # 建立 Tuple 物件
print(t)
print(type(t))

# + colab={"base_uri": "https://localhost:8080/"} id="3GAK7BM6qEOB" executionInfo={"status": "ok", "timestamp": 1607083842254, "user_tz": -480, "elapsed": 1048, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1ffe3667-bac1-407e-92dd-27d981131a99"
print(t[2])  # 索引
# t[2] = "Puppy"  # 因為 Tuples 無法被修改，所以對其指定物件會發生錯誤

# + colab={"base_uri": "https://localhost:8080/"} id="tGAoGepJG1Ug" executionInfo={"status": "ok", "timestamp": 1607863102018, "user_tz": -480, "elapsed": 742, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3d4613c6-d931-4ca0-afa4-2b259b6715b9"
for animal in t:  # 因為也是序列物件，所以可以用 For loop 進行處理
    print(animal)

# + colab={"base_uri": "https://localhost:8080/"} id="1xGApX52IMBj" executionInfo={"status": "ok", "timestamp": 1607863572984, "user_tz": -480, "elapsed": 938, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="31d7b8a2-5b6b-4b82-ab20-a80a3d306e92"
l = ["A", "B", "C"]
t = tuple(l)  # 要將其他序列型態物件轉換為 tuples，可以使用 tuple() 函式
print(t)
print(type(t))

# + [markdown] id="WampJ2R-uDlf"
# ## Sets:：集合

# + colab={"base_uri": "https://localhost:8080/"} id="xb4vIgnhqWkp" executionInfo={"status": "ok", "timestamp": 1607083918623, "user_tz": -480, "elapsed": 1099, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f02bdee7-66eb-45ae-a17a-2b86971c14e0"
s = {1, 2, 3, 4}
print(s)
print(type(s))

# + id="yEUga8k4qoMx"
# print(s[0])  # Sets do not support indexing

# + colab={"base_uri": "https://localhost:8080/"} id="oz6QNXRxrNpE" executionInfo={"status": "ok", "timestamp": 1607084121735, "user_tz": -480, "elapsed": 687, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="cbb9899d-9a00-45d5-fd73-2c5564af900b"
l = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4]
s = set(l)
print(s)


# + [markdown] id="YSzcgugCxB1H"
# ## Lambda expressions

# + [markdown] id="bGGtJD2KxpzP"
# References:
#
# * [Lambda expressions - Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
# * [Lambdas - Python Documentation](https://docs.python.org/3/reference/expressions.html#lambda)

# + id="8yeMussJy0NF"
def add(x, y):
    return x+y


# + colab={"base_uri": "https://localhost:8080/"} id="jy9J7nTY24DR" executionInfo={"status": "ok", "timestamp": 1606986476137, "user_tz": -480, "elapsed": 745, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="9c8409c4-eb77-4e57-9033-1855483e62fd"
print(add(1, 2))

# + id="e8h6F4Rj28Bj"
add = lambda x, y: x+y

# + colab={"base_uri": "https://localhost:8080/"} id="6iivwkAh3FFa" executionInfo={"status": "ok", "timestamp": 1606986544197, "user_tz": -480, "elapsed": 700, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="20af54a6-3005-4f67-e6c0-2fc87c0df7bf"
print(add(1, 2))

# + [markdown] id="U5A4zZ8cthrH"
# ## Additional useful built-in functions

# + [markdown] id="tJtDcPxQy636"
# ### `map()`

# + colab={"base_uri": "https://localhost:8080/"} id="g81wU8LMzGX9" executionInfo={"status": "ok", "timestamp": 1606985496059, "user_tz": -480, "elapsed": 556, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a2bd8a3b-5841-4472-93da-4552a2968206"
numbers = list(range(1, 6))
print(numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="vyWklrFVzLfj" executionInfo={"status": "ok", "timestamp": 1606985545148, "user_tz": -480, "elapsed": 779, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="44b55a5f-cac8-4796-ed3f-c3c4b8e9e384"
map(lambda x: x**2, numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="fxkseO3vzXi7" executionInfo={"status": "ok", "timestamp": 1606985582490, "user_tz": -480, "elapsed": 861, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="b57598c0-e09c-417a-c274-7a25255ddacc"
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# + [markdown] id="DoOTHdJmy8pt"
# ### `filter()`

# + colab={"base_uri": "https://localhost:8080/"} id="Lkf66nfqzrze" executionInfo={"status": "ok", "timestamp": 1606985650710, "user_tz": -480, "elapsed": 791, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="31fdfd6d-cf52-4172-8b46-d8da35c0c22a"
numbers = list(range(1, 6))
print(numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="BGLuyaGWzyhZ" executionInfo={"status": "ok", "timestamp": 1606985663614, "user_tz": -480, "elapsed": 796, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d3b2a05e-e6b7-4b21-9197-0965bbdd73e1"
filter(lambda x: x%2==0, numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="s_UpGPt_zi-U" executionInfo={"status": "ok", "timestamp": 1606985675999, "user_tz": -480, "elapsed": 527, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="dc70ccba-019d-4ed8-d980-6d62a269120c"
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

# + id="X-9yaZrRudzi"


# + [markdown] id="oM3qryUSy-9H"
# ### `zip()`

# + colab={"base_uri": "https://localhost:8080/"} id="DfNGqccsz5Nf" executionInfo={"status": "ok", "timestamp": 1606985723120, "user_tz": -480, "elapsed": 815, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="44a53880-7b3b-4b29-dfde-032160ba7c87"
t1 = ('one', 'two', 'three')
print(t1)
print(type(t1))
t2 = (1, 2, 3)
print(t2)
print(type(t2))

# + colab={"base_uri": "https://localhost:8080/"} id="xbaiL3nS0J8e" executionInfo={"status": "ok", "timestamp": 1606985755255, "user_tz": -480, "elapsed": 830, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="08667ee7-7597-4e60-f58b-89bba7ce0da6"
zip(t1, t2)

# + colab={"base_uri": "https://localhost:8080/"} id="RasvXoH-0DZp" executionInfo={"status": "ok", "timestamp": 1606985761119, "user_tz": -480, "elapsed": 717, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="eede5f81-629c-4630-fcb5-5da728211f08"
zipped = list(zip(t1, t2))
print(zipped)

# + colab={"base_uri": "https://localhost:8080/"} id="8CI8F-Vk0MYc" executionInfo={"status": "ok", "timestamp": 1606985779896, "user_tz": -480, "elapsed": 578, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="273a8d83-be10-4ac8-df58-9efe38c644c2"
zipped_dict = dict(zipped)
print(zipped_dict)
print(type(zipped_dict))

# + [markdown] id="FrJR6hv5zA1e"
# ### `reduce()`

# + id="ScVbqRub01p8"
from functools import reduce

# + colab={"base_uri": "https://localhost:8080/"} id="xfDC9Jtm0hpV" executionInfo={"status": "ok", "timestamp": 1606986240035, "user_tz": -480, "elapsed": 1047, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="398304c4-2d88-4e43-ebb7-e12c2661a718"
numbers = list(range(1, 6))
print(numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="0I2pS-h61IyJ" executionInfo={"status": "ok", "timestamp": 1606986240556, "user_tz": -480, "elapsed": 1344, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="be23ba72-c0ae-4360-cdc5-63028f3fe9c4"
reduce(lambda x, y: x+y, numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="4Zdb3ypv0nat" executionInfo={"status": "ok", "timestamp": 1606986240562, "user_tz": -480, "elapsed": 1215, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f5cf127f-5227-44b5-cf44-3bbb65db34b0"
suqared_sum = reduce(lambda x, y: x+y, numbers)
print(suqared_sum)

# + id="6_kz6kNouBzG"


# + id="XWNpJtcluF2Z"


# + [markdown] id="3LXFgmMtuLjB"
# ### `print()`

# + [markdown] id="77z-exEkaPD3"
# References:
#
# * [printf-style string formatting - Python Documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
# * [Built-in functions print() - Python Documentation](https://docs.python.org/3/library/functions.html#print)
# * [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format)
# * [Format string syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
# * [Fancier output formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
# * [PEP 498 -- Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)

# + [markdown] id="Ljn1W3l2dmzN"
# #### printf-style formatting

# + id="7WaXNZB6aOFz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607080439763, "user_tz": -480, "elapsed": 2733, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="56df0d6f-23e0-4484-a8a7-398bab8e7f3f"
myname = 'Vivi'
print(myname)

# + colab={"base_uri": "https://localhost:8080/"} id="4qiCnF-FcWg2" executionInfo={"status": "ok", "timestamp": 1607080780612, "user_tz": -480, "elapsed": 1017, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="cde6d4d5-b0c1-4822-8fbd-5b3e8bcc1ddc"
print("Hello %s!" % myname)
print("Hello %(name)s!" % {'name': myname})

# + [markdown] id="RtX38ahrdtcY"
# #### Format string syntax

# + id="hnMcJcXjeUjm"
myname = 'Vivi'
print(myname)

# + colab={"base_uri": "https://localhost:8080/"} id="3qEskychedF6" executionInfo={"status": "ok", "timestamp": 1607080771607, "user_tz": -480, "elapsed": 967, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d91a7346-84d8-4f6b-937d-13aff449626e"
print("Hello {}!".format(myname))
print("Hello {name}!".format(name=myname))

# + [markdown] id="5vFrg8TDfCAp"
# #### Fancier output formatting (f-string)

# + colab={"base_uri": "https://localhost:8080/"} id="MWwgMfHAfa_5" executionInfo={"status": "ok", "timestamp": 1607080990323, "user_tz": -480, "elapsed": 1089, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3eb41bfb-3f7f-4190-9bde-d9d2111c96af"
myname = 'Vivi'
print(myname)

# + colab={"base_uri": "https://localhost:8080/"} id="bBPVOvzmfdNt" executionInfo={"status": "ok", "timestamp": 1607081176273, "user_tz": -480, "elapsed": 1072, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1f0c30ea-79da-40cc-86fd-ce33803be1a4"
print(f"Hello {myname}!")

# + colab={"base_uri": "https://localhost:8080/"} id="v2-OXsf5f8CF" executionInfo={"status": "ok", "timestamp": 1607081136043, "user_tz": -480, "elapsed": 1125, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="b7879f75-f776-4487-fb0c-f18f421ce6be"
x, y = 1, 2
print(x, y)

# + colab={"base_uri": "https://localhost:8080/"} id="7nvBbun3gBX5" executionInfo={"status": "ok", "timestamp": 1607081167644, "user_tz": -480, "elapsed": 625, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="c68af9fa-14c7-4a0c-e651-1104262d7289"
print(f"x + y = {x+y}")

# + [markdown] id="Si_vmND6uXIw"
# ### `isinstance()`

# + colab={"base_uri": "https://localhost:8080/"} id="nh10LyXJgtEB" executionInfo={"status": "ok", "timestamp": 1607081340466, "user_tz": -480, "elapsed": 941, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="bc531a08-4841-439c-f267-e1a279a9cb1c"
s = "Hello world!"
print(s)
print(type(s))

# + colab={"base_uri": "https://localhost:8080/"} id="K-I7uXjEgytT" executionInfo={"status": "ok", "timestamp": 1607081378241, "user_tz": -480, "elapsed": 731, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="9385a538-1960-455b-b3df-97cc5597ab03"
print(isinstance(s, str))

# + [markdown] id="xLxww2c1ujMw"
# ### `del()`

# + colab={"base_uri": "https://localhost:8080/"} id="pFRFTB9VhFd2" executionInfo={"status": "ok", "timestamp": 1607081462687, "user_tz": -480, "elapsed": 669, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3a42d6d4-a37a-4fc7-f9e4-722132eb6059"
x = 10
print(x)

# + id="v6gdv3xqhHYi"
del(x)
# print(x)  # NameError: name 'x' is not defined

# + [markdown] id="qPbu-qdWuauN"
# ### `id()`

# + id="4I-Gf6AmiVP1"
import gc

# + colab={"base_uri": "https://localhost:8080/"} id="PhSn0kWUg-WK" executionInfo={"status": "ok", "timestamp": 1607081796023, "user_tz": -480, "elapsed": 1295, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f5034b8a-1376-4fee-d3d9-c733fd1cf841"
x = 10
print(id(x))

# + colab={"base_uri": "https://localhost:8080/"} id="oym5aI2ohU67" executionInfo={"status": "ok", "timestamp": 1607081796024, "user_tz": -480, "elapsed": 1020, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="25b08294-d778-4898-d465-50eea53840c3"
x = 20
print(id(x))

# + colab={"base_uri": "https://localhost:8080/"} id="loJbhQ6SiF67" executionInfo={"status": "ok", "timestamp": 1607081835451, "user_tz": -480, "elapsed": 1072, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="473ff450-265e-44c9-d097-41bcf0dd8312"
l1 = [1, 2, 3]
print(id(l1))
l2 = l1
print(id(l2))

# + [markdown] id="dr2xQU-cuGXR"
# ## Errors and Exceptions

# + colab={"base_uri": "https://localhost:8080/"} id="5q8HqkL8uv2M" executionInfo={"status": "ok", "timestamp": 1606985026182, "user_tz": -480, "elapsed": 5122, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="43ea5a12-71ba-4a37-f896-e9891f525598"
x = None

while True:
    try:
        x = int(input("Please enter a number: "))
        print("The number you input was:", x)
        break
    except Exception as e:
        print("Error occurs!", e)
    finally:
        print("The whole process is end.")

# + colab={"base_uri": "https://localhost:8080/"} id="t0R0CrqwwgH8" executionInfo={"status": "ok", "timestamp": 1606985034921, "user_tz": -480, "elapsed": 8094, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="cc0dbb75-1c4a-43eb-9804-838960c11579"
x = None

while True:
    try:
        x = int(input("Please enter a number: "))
        print("The number you input was:", x)
        break
    except ValueError as ve:
        print("Oops!  That was no valid number.  Try again...")
        print("Error details:", ve)
    except Exception as e:
        print("Unknown error occurs:", e)
    finally:
        print("The whole process is end.")

# + [markdown] id="_AvizkRajNCZ"
# ## List comprehensions

# + [markdown] id="dKRq9vuc0fXG"
# References:
#
# * [PEP 202 -- List Comprehensions](https://www.python.org/dev/peps/pep-0202/)
# * [PEP 274 -- Dict Comprehensions](https://www.python.org/dev/peps/pep-0274/)

# + colab={"base_uri": "https://localhost:8080/"} id="Zrz1guCcjPay" executionInfo={"status": "ok", "timestamp": 1607082048662, "user_tz": -480, "elapsed": 1685, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a978ee3a-1cf8-4c2a-95d9-4372689f9bde"
l = []

for x in range(1, 11):
    l.append(x**2)

print(l)

# + colab={"base_uri": "https://localhost:8080/"} id="jfe_1Pc7jfUN" executionInfo={"status": "ok", "timestamp": 1607082102349, "user_tz": -480, "elapsed": 1304, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d4dee982-7126-4aba-8345-35ca8ff0eeb4"
l = list(map(lambda x: x**2, range(1, 11)))

print(l)

# + colab={"base_uri": "https://localhost:8080/"} id="LPGPFro5joGB" executionInfo={"status": "ok", "timestamp": 1607082124470, "user_tz": -480, "elapsed": 798, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="53f085ff-ad17-4e97-b9c2-a2be381723a1"
l = [x**2 for x in range(1, 11)]

print(l)


# + [markdown] id="tU2gVl-45ps7"
# ## Generators

# + [markdown] id="pNFf-yId5_HT"
# References:
#
# * [Generators - Python Documentation](https://docs.python.org/3/tutorial/classes.html#generators)
# * [sys.getsizeof() - Python Documentation](https://docs.python.org/3/library/sys.html?highlight=getsizeof#sys.getsizeof)

# + id="4khM00oW425z"
def fib_list(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        l.append(a)
    return l


# + colab={"base_uri": "https://localhost:8080/"} id="MYc1lDFN5B_K" executionInfo={"status": "ok", "timestamp": 1607310039322, "user_tz": -480, "elapsed": 1010, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="26bf0299-8091-43a9-ccda-ec8aa3bc6176"
print("The list contains first 100 Fibonacci numbers consumes",sys.getsizeof(fib_list(100)), "bytes")
print("The list contains first 1000 Fibonacci numbers consumes",sys.getsizeof(fib_list(1000)), "bytes")


# + id="BPiTmL7t4fNf"
def fib_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# + colab={"base_uri": "https://localhost:8080/"} id="UX23_Uck4gtC" executionInfo={"status": "ok", "timestamp": 1607310076887, "user_tz": -480, "elapsed": 934, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0e3ed38f-5b5f-42a1-fea7-b01493415169"
print("The generator contains first 100 Fibonacci numbers consumes", sys.getsizeof(fib_generator(100)), "bytes")
print("The generator contains first 1000 Fibonacci numbers consumes", sys.getsizeof(fib_generator(1000)), "bytes")

# + id="_5jGwjReIC3N"

