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

# + [markdown] id="GGnS0Q-mILcy"
# # Chapter 6 - Functions：函式

# + [markdown] id="g0va3iQRRS6i"
# 關鍵字 `def` 就是定義 Definition 的意思，透過這個方式可以建立一個函式，並接收傳入的參數，來定義我們想要讓程式執行的動作。

# + [markdown] id="ccLxH1qAkMym"
# References:
#
# * [Defining Functions - Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

# + [markdown] id="P9kdLlryIM1_"
# ### 基本用法

# + [markdown] id="TL2ewBM-xdMj"
# 建立一個函式時，可以為這個函式指定一個名字，接下來以四個空格的縮排開始一段新的表達式：

# + id="sb2PJyaCIWGT" executionInfo={"status": "ok", "timestamp": 1607673174090, "user_tz": -480, "elapsed": 1413, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def say_hello():           # 初始化一個叫做 say_hello 的函式，且不需要傳入任何參數
    print("Hello world!")  # 這個韓式之內，只有一個調用 print() 函式的動作


# + colab={"base_uri": "https://localhost:8080/"} id="4IjEhoJPIcG8" executionInfo={"status": "ok", "timestamp": 1607673201423, "user_tz": -480, "elapsed": 1235, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="76011286-57df-47e8-9d5a-e07e7bf0eea7"
say_hello()  # 執行 say_hello() 函式

# + colab={"base_uri": "https://localhost:8080/"} id="5vlywCFxIdH_" executionInfo={"status": "ok", "timestamp": 1607673281517, "user_tz": -480, "elapsed": 586, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="6068077a-fe7a-46c4-f873-bc52f579e6d8"
hello = say_hello()  # 嘗試將 say_hello() 函式執行的結果指定給 hello 物件
print(hello)


# + [markdown] id="YMHqboPtyuyf"
# 函式執行完，依情況可以用 `return` 關鍵字，來指定要回傳的物件：

# + id="iuiY0rkwIGsx" executionInfo={"status": "ok", "timestamp": 1607673106601, "user_tz": -480, "elapsed": 948, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def func():      # 初始化一個叫做 func 的函式，且不需要傳入任何參數
    return None  # 這個函式回傳了一個 None 的物件


# + id="a9WRK5hVIUcX" executionInfo={"status": "ok", "timestamp": 1607673415452, "user_tz": -480, "elapsed": 888, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
func()  # 執行 func() 函式

# + colab={"base_uri": "https://localhost:8080/"} id="hVDY8pdKzZvO" executionInfo={"status": "ok", "timestamp": 1607673478577, "user_tz": -480, "elapsed": 1311, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="85c1d363-b954-4a41-a201-0e6de2719663"
reaction = func()  # 嘗試將 func() 函式執行的結果指定給 reaction 物件
print(reaction)


# + id="EvZrktXhIiiv" executionInfo={"status": "ok", "timestamp": 1607673605166, "user_tz": -480, "elapsed": 1506, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def give_me_five():      # 初始化一個叫做 give_me_five 的函式
    print("High five!")  # 讓函式調用 print() 函式，顯示 "High five!" 的字串
    return 5             # 讓函式回傳整數 5


# + colab={"base_uri": "https://localhost:8080/"} id="etylie00z_gb" executionInfo={"status": "ok", "timestamp": 1607673607647, "user_tz": -480, "elapsed": 1377, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="e535476b-f242-40b2-d41c-e35b9e12e5e2"
give_me_five()  # 執行 give_me_five() 函式

# + colab={"base_uri": "https://localhost:8080/"} id="8Qcfj3AkIrTu" executionInfo={"status": "ok", "timestamp": 1607673633639, "user_tz": -480, "elapsed": 1303, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="ca0fa829-2200-47d7-98b9-7c7e04a22d0c"
answer = give_me_five()  # 嘗試將 give_me_five() 函式執行的結果指定給 answer 物件
print(answer)
print(type(answer))


# + [markdown] id="0rr7uVmCIvX7"
# ### 添加傳入參數 (Arguments / Parameters)

# + [markdown] id="oGDTD8tA0VS4"
# 函式可以接收參數，不同參數之間以逗點分隔：

# + id="tEt4d96QI0Yi"
def add_them(x, y):  # 新增名為 add_them 的函式，並接收兩個參數：x, y
    print("x + y = ", x+y)


# + colab={"base_uri": "https://localhost:8080/"} id="OeYLomY1JEyj" executionInfo={"status": "ok", "timestamp": 1606974497409, "user_tz": -480, "elapsed": 630, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="bbd65d65-84de-4a6c-d781-124ccc3a115c"
add_them(1, 2)      # 調用函式並對參數 x, y 分別帶入 1, 2
add_them(x=3, y=4)  # 調用函式並對參數 x, y 分別帶入 3, 4


# + id="4wpx_xZlJK1U" executionInfo={"status": "ok", "timestamp": 1607674079743, "user_tz": -480, "elapsed": 935, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def add_these(x, y, z):  # 這次接收三個參數
    print("x + y + z = ", x+y+z)


# + colab={"base_uri": "https://localhost:8080/"} id="cvM6ElfYJZ18" executionInfo={"status": "ok", "timestamp": 1607674085065, "user_tz": -480, "elapsed": 1215, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="777861a9-be3b-447b-cc10-73710b06a281"
add_these(1, 2, 3)

# + [markdown] id="i8R9j4Iq19bp"
# 調用參數時，若不指定要傳入參數的關鍵字，將會依照建立函式時的設定，依序將接收的物件帶入給各個參數。
#
# 若要將特定的物件指定給特定的參數，是以一種名為關鍵字參數 (Keyword arguments) 的方法執行，格式是`關鍵字參數名=數值` (`kwargs=value`)

# + colab={"base_uri": "https://localhost:8080/"} id="WFmO04lR6lPT" executionInfo={"status": "ok", "timestamp": 1607675314350, "user_tz": -480, "elapsed": 1384, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="b55ffc4f-0a5e-48db-80cf-6f71aa4ebd4a"
add_these(x=1, y=2, z=3)  # 指定所有的關鍵字參數

# + [markdown] id="VLAD-gaY6B3R"
# 指定關鍵字參數時，參數順序可以調換。也可以僅指定部分的關鍵字參數，但有一個原則：只要指定了一個關鍵字參數，接下來傳入的參數也都要指定為關鍵字參數。

# + id="ei8jR9Q_JmAk" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607675401601, "user_tz": -480, "elapsed": 1760, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f240e56a-f1f0-40de-8026-49a914a9655d"
add_these(1, 2, z=3)      # 僅指定一個關鍵字參數
add_these(1, y=2, z=3)    # 指定兩個關鍵字參數
add_these(1, z=2, y=3)    # 關鍵字參數的順序可以調換


# + id="NkrfWm6wJ3VM" executionInfo={"status": "ok", "timestamp": 1607675399462, "user_tz": -480, "elapsed": 1378, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
# add_these(x=1, 2, 3)    # 錯誤：指定了第一個參數為關鍵字參數，但其後的參數沒有指定為關鍵字參數
# add_these(x=1, y=2, 3)  # 錯誤：指定了第二個參數為關鍵字參數，但其後的參數沒有指定為關鍵字參數

# + [markdown] id="58umcF_a6_XW"
# 參數可以有預設值。當使用者沒有指定傳給有預設值的參數時，就以預設值作為參數的內容。
#
# 與關鍵字參數相似的概念是：如果指定了一個參數的預設值，則其後的參數也都需要被指定預設值。

# + id="GdVg4j-iKAiY" executionInfo={"status": "ok", "timestamp": 1607675505396, "user_tz": -480, "elapsed": 1105, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def add_these(x, y, z=0):  # 預先指定關鍵字 z 的傳入值為 0
    print("x + y + z =", x+y+z)


# + colab={"base_uri": "https://localhost:8080/"} id="yrFvd_kabZwq" executionInfo={"status": "ok", "timestamp": 1607675536584, "user_tz": -480, "elapsed": 989, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0dabf274-af74-4afd-c9cc-e80b713a58e9"
add_these(1, 2)  # 僅代入 x, y 參數，z 則維持預設值 0


# + id="pJfAUjxSKRNV" executionInfo={"status": "ok", "timestamp": 1607675575049, "user_tz": -480, "elapsed": 1463, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
# def add_these(x=0, y, z):  # 錯誤：指定了第一個參數的預設值，其後的參數也都需要指定預設值。
#     print("x + y + z = ", x+y+z)

# + [markdown] id="p9yeOpJn77o9"
# References:
#
# * [More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

# + [markdown] id="UKlo-m88KV_G"
# #### `*args`：可變長度參數 (Arbitrary number of arguments)

# + [markdown] id="azb8JOui-ctP"
# 在包含多個物件的名稱之前加上 `*` 關鍵字，可以一次將多個物件給依序傳入函式中：

# + id="9pGPvNAjaY_s" executionInfo={"status": "ok", "timestamp": 1607675943775, "user_tz": -480, "elapsed": 1454, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def print_them(x, y, z):  # 初始化一個可以接收 x, y, z 三個參數的函式
    print("x =", x)
    print("y =", y)
    print("z =", z)


# + colab={"base_uri": "https://localhost:8080/"} id="8l7saQFOal20" executionInfo={"status": "ok", "timestamp": 1607676484703, "user_tz": -480, "elapsed": 958, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="fd7b3dd1-db87-460b-fca7-310de42b21ea"
numbers = [1, 2, 3]
print_them(*numbers)         # 一次將 numbers[0], numbers[1], numbers[2] 給依序傳入函式內
# print_them(x=1, y=2, z=3)  # 上一行的用法與此行等價

# + [markdown] id="Wly-oQKlaT1n"
# #### `**kwargs`：可變長度關鍵字參數

# + [markdown] id="fzr-G7NF_HoM"
# 若在字典物件之前加上 `**` 關鍵字，可以將字典的鍵值對當作關鍵字參數給傳入函式：

# + id="56_ONxO_aYB1" executionInfo={"status": "ok", "timestamp": 1607676530554, "user_tz": -480, "elapsed": 902, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
def print_them(x, y, z):  # 初始化一個可以接收 x, y, z 三個參數的函式
    print("x =", x)
    print("y =", y)
    print("z =", z)


# + colab={"base_uri": "https://localhost:8080/"} id="hMS-lNisa2Si" executionInfo={"status": "ok", "timestamp": 1607676737399, "user_tz": -480, "elapsed": 1016, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="e24c295f-86a8-41b7-c595-62d2b8ee7e93"
numbers_dict = {
    "x": 1,
    "y": 2,
    "z": 3,
}
print_them(**numbers_dict)  # 將 1 代入參數 x、2 代入參數 y、3 代入參數 z
# print_them(x=1, y=2, z=3) # 上一行的用法與此行等價

# + [markdown] id="nbUpIXWGbDhO"
# ## 全域

# + [markdown] id="vFg7kv7KAYHr"
# 在 Python 中，呼叫一個物件名稱時會參照到哪個物件，必須要參考這個物件的作用域 (Scope)，有以下的區別：
#
# * Python 原生內建的物件，稱作內建域 (Built-in)
# * 在沒有建立函式時，建立的物件是生效在全域 (Global)
# * 若在函式裡建立巢狀（Nested，意指多層次）函式，最底層函式的作用域叫做本地域 (Local)
# * 巢狀函式中，本地域與全域之間的作用域，稱作封閉域 (Enclosing)
#
# 所以調用物件時，查詢的順序為：
#
# 1. 內建域 (Built-in)
# 2. 本地域 (Local)
# 3. 封閉域 (Enclosing)
# 4. 全域 (Global)
#
#
# 若要在函式裡呼叫物件，需考慮到物件會調用到哪個區域的物件，才不會出現意料之外的錯誤。
#
# 如果要強制調用不同作用域的物件，有幾個關鍵字可以使用：
#
# 1. `global`：在此本地域 (Local) 調用全域 (Global) 物件
# 2. `nonlocal`：在此本地域 (Local) 調用本地域 (Local) 以及全域 (Glocal) 以外的所有物件
#
# References:
#
# * [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
#
# > 備註：對初學者來說，這真的稍嫌複雜，而且連筆者都沒辦法好好地寫好一個更淺顯的範例⋯⋯於是拿了 Python 官方文件的內容來嘗試跟大家講解。
# > 
# > 為了讓各位方便理解，筆者將程式碼的執行順序以 [1], [2], ... 標示，等一下請依照標示來閱讀程式內容：

# + id="L4bvdokaceQ6" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607680395985, "user_tz": -480, "elapsed": 1096, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1f5b6ab2-8519-4d42-ce3c-ea7ceb6cd090"
spam = "spam"                                       # [1]
print("[2] Global assignment:", spam)               # [2]

def scope_test():
    def do_local():
        spam = "local spam"                         # [6]
        print("[7] Local assignment:", spam)        # [7]

    def do_nonlocal():
        nonlocal spam                               # [10]
        spam = "nonlocal spam"                      # [11]

    def do_global():
        global spam                                 # [14]
        spam = "global spam"                        # [15]

    spam = "test spam"                              # [4]

    do_local()                                      # [5]
    print("[8] After local assignment:", spam)      # [8]
    
    do_nonlocal()                                   # [9]
    print("[12] After nonlocal assignment:", spam)  # [12]
    
    do_global()                                     # [13]
    print("[16] After global assignment:", spam)    # [16]

scope_test()                                        # [3]
print("[17] In global scope:", spam)                # [17]

# + [markdown] id="uYcatCs-F3s7"
# 1. 指定 `"spam"` 字串內容給全域 (Global) 的 `spam` 物件
# 2. 顯示 `spam` 物件，內容為全域 (Global) 的 `"spam"`
# 3. 呼叫 `scope_test()` 函式
# 4. 建立 `spam` 物件並指定 `"test spam"` 字串內容
# 5. 呼叫 `do_local()` 函式
# 6. 指定 `"local spam"` 字串內容給本地域 (Local) 的 `spam` 物件
# 7. 顯示 `spam` 物件，內容為本地域 (Local) 的 `"local spam"`
# 8. 顯示 `spam` 物件，內容為封閉域 (Enclosing) 的 `"test spam"`
# 9. 呼叫 `do_nonlocal()` 函式
# 10. 用 `nonlocal` 關鍵字，改變物件的作用域為封閉域 (Enclosing)
# 11. 指定 "nonlocal spam"` 字串內容給封閉域 (Enclosing) 的 `spam` 物件
# 12. 顯示 `spam` 物件，內容為 `nonlocal` 關鍵字宣告後，最接近的 `"nonlocal spam"`
# 13. 呼叫 `do_global()` 函式
# 14. 用 `global` 關鍵字，改變物件的作用域為全域 (Global)
# 15. 指定 "global spam"` 字串內容給全域 (Global) 的 `spam` 物件
# 16. 顯示 `spam` 物件，內容為 `nonlocal` 關鍵字宣告後，最接近的 `"nonlocal spam"`
# 17. 顯示 `spam` 物件，內容為 `global` 關鍵字宣告後，最接近的 `"global spam"`

# + id="Q8CnDEabQLF3"

