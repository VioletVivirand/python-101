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

# + [markdown] id="Mf0pK2uGkw5h"
# # Chapter 5 - Control flows and Iterables：流程控制與疊代

# + [markdown] id="EL3d0Z2uCauf"
# ## `range()`：建立範圍序列物件

# + [markdown] id="oZGpw-EfUOSf"
# 在談到流程控制以前，我們會先介紹一個很實用的物件：範圍 (Range)。
#
# > 備註：為了中文教學需要，我硬是翻譯了一下，所以定名為「範圍」。但實際上，官方似乎沒有對這個物件定下官方譯名，未來如果有溝通的困難，請各位還是稱其為 Range 物件。
#
# 與 List 相似，範圍物件也是一種序列 (Sequence) 物件，用來產生一組數列，而我們可以透過設定參數，去指定序列的起始數字、結尾數字 - 1、以及每個數字之間的差值。
#
# > 備註：沒錯，這三個參數就是 `start`, `stop`, 與 `step`。是不是跟字串和串列的索引十分相似？
#
# References:
#
# * [class range - Python Documentation](https://docs.python.org/3/library/functions.html#func-range)
# * [Ranges - Python Documentation](https://docs.python.org/3/library/stdtypes.html#ranges)

# + colab={"base_uri": "https://localhost:8080/"} id="ElGT4snQCf-r" executionInfo={"status": "ok", "timestamp": 1606972748055, "user_tz": -480, "elapsed": 1482, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="928b2c4d-be3d-45bf-bcd2-45fc94ca676d"
print(range(10))  # 嘗試顯示一個串列

# + [markdown] id="YmgIlbXKU4wK"
# 直接使用 `print()` 函式來顯示串列內容的話，似乎只會看到設定值。特別的是，如果不指定 `start` 的話，參數將會被指定為 `stop` 的數值。詳情可以參考 `help(range)` 的文件內容。
#
# 所以要如何才可以顯示串列中的所有數值呢？其中一種方法是用我們先前提到的 `list()` 函式將其轉換為串列：

# + colab={"base_uri": "https://localhost:8080/"} id="0aQ7OU4BCjUe" executionInfo={"status": "ok", "timestamp": 1606972756037, "user_tz": -480, "elapsed": 722, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="52d90b7a-a382-4c38-d2b6-ea55e911c738"
print(list(range(10)))  # 將 range 物件轉換為串列，就可以顯示了

# + colab={"base_uri": "https://localhost:8080/"} id="7JnKHaC1ClYi" executionInfo={"status": "ok", "timestamp": 1606972777202, "user_tz": -480, "elapsed": 689, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="47a502e6-d7f9-4022-8971-11a21ec5b402"
print(list(range(1,10,1)))  # 試著加上一些設定值

# + colab={"base_uri": "https://localhost:8080/"} id="VJh5g3ScCqv6" executionInfo={"status": "ok", "timestamp": 1606972791440, "user_tz": -480, "elapsed": 673, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="6b18a691-1f85-4129-ac8b-2530f84c5b06"
print(list(range(1,10+1,1)))  # 如果要顯示 1 - 10，應該這樣設定

# + colab={"base_uri": "https://localhost:8080/"} id="dkD_PdvfCt39" executionInfo={"status": "ok", "timestamp": 1606972804133, "user_tz": -480, "elapsed": 645, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="656f3134-034f-4207-aa51-1c27121c83a4"
print(list(range(10,0,-2)))  # 也可以產生由大到小的數列

# + [markdown] id="L6MbiwaGlIRi"
# ## `if`：流程控制、條件判斷

# + [markdown] id="AYAdrhLKmSq_"
# `if` 陳述式是流程控制的基本元素，在後面接著給定一個成立的條件，並撰寫表達式，就可以讓程式判斷狀態並執行相對應的指令：

# + colab={"base_uri": "https://localhost:8080/"} id="BXr6uKflkmkk" executionInfo={"status": "ok", "timestamp": 1607586282222, "user_tz": -480, "elapsed": 2166, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1aea9f9d-25d9-46d4-f584-a4563b45eb4b"
name = "Vivi"  # 建立一個存放名稱字串的物件
print("The name is", name)

# + colab={"base_uri": "https://localhost:8080/"} id="Wx7fcHWllR1c" executionInfo={"status": "ok", "timestamp": 1607586282233, "user_tz": -480, "elapsed": 1983, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3f5dbc42-eb36-4693-c587-8e0527943419"
if name == "Vivi":  # 判斷名稱後作出相應的動作
    print("Welcome,", name+"!")

# + [markdown] id="KCTJsskcldHN"
# ### `else`：設定所有判斷式均不成立時執行的動作

# + [markdown] id="Sf2nmciSnE-Z"
# 或 `if` 陳述式判斷的條件不成立時，用 `else` 關鍵字來設定此時要執行的動作：

# + id="DCfANjlSl3FP"
name = "Gigi"  # 建立一個存放名稱字串的物件
print("The name is", name)

# + colab={"base_uri": "https://localhost:8080/"} id="W9ZbM3MKloAL" executionInfo={"status": "ok", "timestamp": 1606965233997, "user_tz": -480, "elapsed": 744, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a2a13fe7-5c1a-4e65-9c27-b0c29e691e4e"
if name == "Vivi":  # 判斷名稱是否等於 'Vivi'
    print("Welcome,", name+"!")
else:               ## 若前項所有條件都不成立時，執行此處的動作
    print("Do I know you?")

# + [markdown] id="1w_MtCLfl1KB"
# ### `elif`：設定前一個判斷式不成立時，接著執行的判斷式及動作

# + [markdown] id="UQA2xIdgnq7f"
#  在 `if` 陳述式判斷條件之後，還可以加上 `elif` 來繼續執行多次的判斷：

# + colab={"base_uri": "https://localhost:8080/"} id="xdx-VA8ll87S" executionInfo={"status": "ok", "timestamp": 1606965292958, "user_tz": -480, "elapsed": 641, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d3253564-fee9-412a-bbef-852cac4e1aef"
name = 'Kiki'  # 建立一個存放名稱字串的物件
print("The name is", name)

# + colab={"base_uri": "https://localhost:8080/"} id="LuZrPv3FmGzO" executionInfo={"status": "ok", "timestamp": 1606965360929, "user_tz": -480, "elapsed": 686, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="28ecaa85-0397-4068-a37c-d5866125a715"
if name == 'Vivi':    # 判斷名稱是否等於 'Vivi'
    print("Welcome,", name+"!")
elif name == 'Kiki':  # 判斷名稱是否等於 'Kiki'
    print("Long time no see!", name+".")
else:                 # 若前項所有條件都不成立時，執行此處的動作
    print("Do I know you?")

# + [markdown] id="w__-iBSUsRT7"
# > 備註：其他程式語言裡通常是寫作 `else if`

# + [markdown] id="Qd10n2WvmU0k"
# ### 經典範例：foo & bar

# + [markdown] id="wppKnuLLojDF"
# 記得題目是：驗證一個數字，當她是：
#
# * `2` 的倍數：顯示 `Foo`
# * `3` 的倍數：顯示 `Bar`
# * `6` 的倍數：顯示 `Foo Bar`
# * 以上均不成立時，回傳該數字

# + colab={"base_uri": "https://localhost:8080/"} id="XInrcJqJqr0q" executionInfo={"status": "ok", "timestamp": 1606966956979, "user_tz": -480, "elapsed": 686, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="57bc701d-187d-4535-cce4-b2cf174a9dac"
n = 12

if n % 3 == 0 and n % 2 == 0:
    print("Foo Bar")
elif not(n % 2):
    print("Foo")
elif not(n % 3):
    print("Bar")
else:
    print(n)

# + [markdown] id="c-5kbJW2sgCi"
# ## 疊代、迴圈

# + [markdown] id="MGh_uGgMp__w"
# 維基百科對「疊代」的解釋：
#
# > 疊代是重複回饋過程的活動，其目的通常是為了接近併到達所需的目標或結果。每一次對過程的重複被稱為一次「疊代」，而每一次疊代得到的結果會被用來作為下一次疊代的初始值。
#
# 而「迴圈」的部分則是：
#
# > 迴圈是計算機科學運算領域的用語，也是一種常見的控制流程。迴圈是一段在程式中只出現一次，但可能會連續執行多次的程式碼。迴圈中的程式碼會執行特定的次數，或者是執行到特定條件成立時結束迴圈，或者是針對某一集合中的所有項目都執行一次。
#
# 所以這兩個名詞，講的都是我們接下來要做的事情：讓程式重複地進行某個動作。
#
# References:
#
# * [請問到底是在「疊代」或是在「迭代」？ - Medium](https://ryo6.medium.com/請問到底是在-疊代-或是在-迭代-f5bdba4c31eb)

# + [markdown] id="a9yh5Z15vT5g"
# ### `for`：For 迴圈 (For loop)

# + [markdown] id="4qkRXugDs-z2"
# 透過 `for` 陳述句以及 `in` 運算子，可以對序列物件裡的各個物件依序進行處理：

# + colab={"base_uri": "https://localhost:8080/"} id="eIwa2EyxsjCl" executionInfo={"status": "ok", "timestamp": 1607588729594, "user_tz": -480, "elapsed": 1271, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="ed929393-b2f8-4f5f-8db1-2c6cc8b1bcb9"
animals = ["bird", "cat", "dog"]  # 建立一個有許多動物名稱字串的串列物件
print(animals)

# + colab={"base_uri": "https://localhost:8080/"} id="X3pJQ9sjs1aL" executionInfo={"status": "ok", "timestamp": 1606967119284, "user_tz": -480, "elapsed": 870, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="c2d44989-ea1f-4b14-83bb-7c2a28ea3add"
for animal in animals:  # 讀取每個動物的名稱
    print("Hey, there is a", animal+"!")

# + colab={"base_uri": "https://localhost:8080/"} id="Sq2U6wR6tAve" executionInfo={"status": "ok", "timestamp": 1606967167951, "user_tz": -480, "elapsed": 663, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="00e87d20-43df-41c6-9370-72ae47ad2a47"
for number in range(10):  # range 物件也是個序列，也可以依序處理
    print(number)

print("Boom!")

# + [markdown] id="tmBlv7jtkkK8"
# #### 用 `enumerate()` 搭配串列

# + [markdown] id="caMAUdxrvd3B"
# 使用 `enumerate()` 函式，將可以把串列物件轉換為多個 `(索引, 內容)` 的序列物件：
#
# > 備註：序列物件裡，裝的是一個一個的 Tuple 物件，是個不可變型態的物件。由於初學比較少使用，被我把介紹的篇幅移到最後去了，在最後會一併介紹。

# + colab={"base_uri": "https://localhost:8080/"} id="K6GNregqkuxj" executionInfo={"status": "ok", "timestamp": 1607589191706, "user_tz": -480, "elapsed": 1218, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="dfd500b9-9964-4611-8976-f72b4e9f9e4f"
animals = ["Bird", "Cat", "Dog", "Eagle"]  # 建立一個有許多動物名稱字串的串列物件
print(animals)

# + colab={"base_uri": "https://localhost:8080/"} id="I0b7_8A5lJxT" executionInfo={"status": "ok", "timestamp": 1607589192537, "user_tz": -480, "elapsed": 1739, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f0fa2d9c-c2f3-4cd7-bdda-9b80e75b56ad"
for key, value in enumerate(animals):  # 透過 enumerate() 函式轉換後
                                       # 會產生多個 (索引值, 內容) 的物件，
                                       # 所以也需要用兩個物件去承接讀取出來的內容
                                       # 在這裡，key 是物件在這個串列中的索引值，value 則為物件內容
    print("The animal", value, "has the index", key)

# + colab={"base_uri": "https://localhost:8080/"} id="cA0UPzpFmtzi" executionInfo={"status": "ok", "timestamp": 1607589192544, "user_tz": -480, "elapsed": 955, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="eea15180-e79c-47bc-ae8a-bb07cef74fac"
for index, animal in enumerate(animals):  # 一般為了講究可讀性，讀取出來的物件，會取得有意義些
    if animal == "Dog":                   # 也可以接著做條件判斷處理，像這裡就是判斷字串內容是否為 Dog
        animals[index] = "Puppy"          # 若條件成立，把串列裡此索引值的內容從 Dog 改為 Puppy

print(animals)

# + [markdown] id="r3tW2y2BxR6r"
# > 補充：如果只想要讀取索引值，不需要內容呢？我們可以把讀取出來的內容存成底線 `_`，代表忽略這個物件。
# >
# > 像以下這個範例，就是在依序讀取的過程中，判斷當索引值為 1 時，將內容改為空白字串：

# + colab={"base_uri": "https://localhost:8080/"} id="NR9nRmEfxkBn" executionInfo={"status": "ok", "timestamp": 1607589194129, "user_tz": -480, "elapsed": 1175, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="5a8e3434-dbbd-4470-f345-ef4b4b714dde"
for index, _ in enumerate(animals):
    if index == 1:
        animals[index] = ""

print(animals)

# + [markdown] id="3m2blkt7kspO"
# #### 用 `dict.items()` 搭配字典

# + [markdown] id="f0qzZBHwyN4D"
# 類似 `enumerate()` 函式搭配串列的用法，呼叫 `dict.items()` 將可以把字典物件轉換為多個 `(索引, 內容)` 的序列物件：

# + id="UnEOIDs_ydRg"
from pprint import pprint

# + id="pBusoF7cmBoK"
profile = {
    "name": "Vivi",
    "age": 18,
    "skills": [
        "eating",
        "sleeping",
        "dreaming",
    ]
}



# + colab={"base_uri": "https://localhost:8080/"} id="N-kOih8lmXWE" executionInfo={"status": "ok", "timestamp": 1607082844708, "user_tz": -480, "elapsed": 817, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="16e1051f-9b48-4018-a276-16a5841b2e83"
print("This is my profile:")

for key, value in profile.items():
    print(key, "=", value)

# + colab={"base_uri": "https://localhost:8080/"} id="v7Og2DQlnF0m" executionInfo={"status": "ok", "timestamp": 1607083083232, "user_tz": -480, "elapsed": 1457, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f3a6aef9-ec2c-45b5-9d09-f46beca8b982"
for section, content in profile.items():
    if content == 18:
        profile[section] = 32

print(profile)

# + [markdown] id="zAiotYTftefS"
# ### `while`：While 迴圈 (While loop)

# + [markdown] id="UZ11xfPn1TgY"
# While 迴圈比較簡單：只要 `while` 陳述句後面接的條件為真，就會一直重複執行接下來指定的動作，直到條件不為真時才會停止。
#
# 既然比較簡單，為什麼會放到 For loop 之後才介紹呢？是因為在我的經驗裡，While 迴圈比較危險：當一個一直為真的條件、搭配一個不會被中斷執行的動作，將會讓這個程式永無止盡的執行⋯⋯。這種情況通常稱作「無窮迴圈」。
#
# > 備註：印象中，早些年在執行有無窮迴圈的程式時，真的會把系統的記憶體吃到半點不剩，導致電腦變得超卡頓、甚至直接當機的狀況。現在好像有機會偵測出這個問題並且自動停止執行，但我也沒很想嘗試就是了⋯⋯
# >
# > 如果沒有特別的需求，請不要輕易撰寫、或執行無窮迴圈！

# + colab={"base_uri": "https://localhost:8080/"} id="JVx-KG9_vWh2" executionInfo={"status": "ok", "timestamp": 1607590716518, "user_tz": -480, "elapsed": 1196, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="2b6b68ab-5413-47c0-ae69-0535671c8943"
x = 0               # 初始化 x 物件為 0

while x < 10:       # 設定在 x < 10 時皆可不斷執行
    if x % 3 == 0:  # 判斷 x 除以 3 的餘數為 0 時，才顯示該數字
        print(x)
    x += 1          # 不會造成無窮迴圈的關鍵：每次執行完時，都記得對 x 做處理
                    # 這樣條件才有不為真的一天

# + id="2ne3IBTsvh7I" executionInfo={"status": "ok", "timestamp": 1607591116710, "user_tz": -480, "elapsed": 1050, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
# 這就是個無窮迴圈的範例，不要輕易嘗試執行！
# 
# x = 1

# while x:  # x 只會一直加 1，條件永遠為真
#     print(2**x)
#     x += 1

# + [markdown] id="hqO8WT8bBT2L"
# ## 其他流程控制工具

# + [markdown] id="RtAlFKy8DQBB"
# ### `break`：中斷迴圈執行

# + [markdown] id="cCkB8hfV6NTh"
# 常見的情境是：指定在某條件發生時，中斷迴圈的執行：

# + colab={"base_uri": "https://localhost:8080/"} id="4MQI5BfbBn3G" executionInfo={"status": "ok", "timestamp": 1607591433780, "user_tz": -480, "elapsed": 1202, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0ee99f4e-3234-412d-ff8c-71fe17bdeb18"
for x in range(1,21):  # 初始化一個 1 - 20 的數列，並依序針對數列中的數字進行處理
    if x % 4 == 0:     # 判斷 x 是否為 4 的倍數
        break          # 條件為真時，中斷迴圈執行
    print(x)           # 條件不成立時，顯示該數字

# + [markdown] id="hUIWLfVhDLqm"
# ### `continue`：不執行 `continue` 陳述句底下的動作，直接進行下一輪迴圈

# + [markdown] id="ABItnGQN6t_U"
# 常見的情境是：指定在某條件發生時，不做任何處理，並返回「迴圈程式碼的第一行」再次執行迴圈：

# + colab={"base_uri": "https://localhost:8080/"} id="c014z0B8EMd7" executionInfo={"status": "ok", "timestamp": 1606973366901, "user_tz": -480, "elapsed": 797, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f565d773-ae62-4cd4-dc84-11f7d907e18d"
for x in range(1,21):
    if x % 4 == 0:
        continue
    print(x)

# + [markdown] id="Auz-uRYD7p8b"
# 為什麼強調要回到「迴圈程式碼的第一行」再次執行呢？因為裡面是有玄機的：以上面的例子來看，當執行過第一行之後，`range` 物件裡就會將以經處理過的數字給移除，所以在遇見 `continue` 陳述式時，回到第一行依然可以繼續將剩下的數字給處理完。

# + colab={"base_uri": "https://localhost:8080/"} id="uSiRBGj59Mm5" executionInfo={"status": "ok", "timestamp": 1607663996188, "user_tz": -480, "elapsed": 802, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f4eff7fa-cb59-469d-8d94-85d674906439"
# 讓我們用些方法來檢查 range 物件執行的邏輯
list(range(10))
range_iter = iter(range(10))
print(next(range_iter))
print(next(range_iter))
print(list(range_iter))

# + [markdown] id="Z7_y3rZ4Pmnh"
# 再看以下的例子：這樣會導致無窮迴圈的出現

# + id="XkMrnF4xEV5i"
# 以下的執行過程為無窮迴圈，非必要請不易執行！
# 
# x = 1
# 
# while x < 21:
#     if x % 4 == 0:
#         continue
#     print(x)
#     x += 1

# + [markdown] id="FGWGeziIP5Fl"
# 所以，在操作 While 迴圈時，如何設定一個會終止的條件就變得相當重要。上面的例子，可以改成底下的形式來避免形成無窮迴圈：

# + colab={"base_uri": "https://localhost:8080/"} id="lWDRNtPPEXfB" executionInfo={"status": "ok", "timestamp": 1607664167834, "user_tz": -480, "elapsed": 820, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="b7504043-69a3-4268-b9e9-75a72f5e6097"
x = 1

while x < 21:
    if x % 4 == 0:
        x += 1
        continue
    print(x)
    x += 1

# + id="gSWULreaGgg5"

