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

# + [markdown] id="vh24NWimaXtR"
# # Chapter 3 - Methods and Functions：方法與函式

# + [markdown] id="JEdL9FX4AmLt"
# ## 指定變數 Variable（= 物件 Object）表達式

# + [markdown] id="34eVaBh-cju2"
# 如同代數一樣，在撰寫程式時，我們也可以像代數一樣，用某個代號來稱呼某些內容。
#
# 一般的程式都稱這種代換的內容為變數 (Variable）。在 Python 中，所有可以操作的內容都是繼承「物件 (`object`)」類別而衍生的，所以變數也等同於物件。
#
# 指定物件時，會將等號右側的內容指定給左側的物件，例如 `n = 10`，即是將整數 `10` 指定給物件 `n`。
#
# > 備註：跟一般的數學式子不一樣，在程式語言中，一個等號 `=` 是代表「指定」，兩個等號 `==` 才是比較左右兩側的內容是否一致。
#
# References:
#
# * [Simple statements - Python Documentation](https://docs.python.org/3/reference/simple_stmts.html)

# + colab={"base_uri": "https://localhost:8080/"} id="idvh2H1mAxPC" executionInfo={"status": "ok", "timestamp": 1606899231685, "user_tz": -480, "elapsed": 956, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="2c8a9669-c709-4620-85b6-f3bbc3fadfa5"
# 範例：建立一個字串物件
s = "Hello world!"
print(s)
print(type(s))  # 驗證此物件是否為 str 型態

# + [markdown] id="OkdTUuECN_9i"
# 而物件的名稱需要參照命名規則。一般來說，要注意的事項如下：
#
# * 名稱不以數字開頭
# * 名稱中不包含 `-`（會與減法運算子混淆）
# * 名稱需避開 Python Keywords（參見[官方文件中的內容](https://docs.python.org/3/reference/lexical_analysis.html#keywords)）
#
# 另外，Google Python Style Guide 另有列出一串建議的命名方式：
#
# ```
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
# ```
#
# References:
#
# * [Keywords - Python Documentation](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
# * [Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
# * [Namings - Gogole Python Stule Guide](https://google.github.io/styleguide/pyguide.html#s3.16-naming)

# + colab={"base_uri": "https://localhost:8080/"} id="TTiCXpHRA2WI" executionInfo={"status": "ok", "timestamp": 1606900790857, "user_tz": -480, "elapsed": 4287, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a9215883-6c14-4d72-ea4c-751db3ed22ed"
# 搭配內建函式 input()，可以在執行時出現一個輸入窗格，讓使用者輸入內容並記錄起來
input_str = input("Hi, what's your name? ")
print("So you are", input_str + ".", "Welcome!")

# + [markdown] id="E0vIO2gLT8Jy"
# ### Augmented assignment statements：增強賦值陳述式

# + [markdown] id="nTgjsrBJhhfc"
# 增強賦值陳樹是的用途，就是將運算子與指定變數的語句合而為一。例如 `+=` 會將等號右側的內容與左側相加之後，再指定給等號左側的物件。
#
# References:
#
# * [Augmented assignment statements](https://docs.python.org/3/reference/simple_stmts.html?highlight=additional%20assignment#augmented-assignment-statements)

# + colab={"base_uri": "https://localhost:8080/"} id="IMm8KTpiUAxv" executionInfo={"status": "ok", "timestamp": 1607417236264, "user_tz": -480, "elapsed": 2042, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="c4a90cd3-7f8d-435b-fe43-6796ee48a6d0"
number = 1
number += 2
# number = number + 2  # 此表達式與上式等價
print(number)

# + [markdown] id="OWmkOr8Ynwp3"
# ## 複習: 使用物件的方法 (methods)

# + [markdown] id="fB_RCKeNikGU"
# 物件本身不只是可以用來儲存內容，很多物件都會內建一些好用的方法讓我們調用。在上一個章節，我們嘗試調用了字串物件的方法，這裡先回顧一下呼叫方法的方式：執行 `object.method()`

# + [markdown] id="eoihpvKJn4tv"
# ### 字串方法

# + colab={"base_uri": "https://localhost:8080/"} id="iaPIPogAn7_0" executionInfo={"status": "ok", "timestamp": 1606899252001, "user_tz": -480, "elapsed": 1042, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0a4db039-8bde-46a6-ab7c-ad59921ef876"
s = "Hello world!"
print(s.upper())  # 將字串轉換為大寫
print(s.lower())  # 將字串轉換為小寫
print(s.title())  # 將字串中的每個字詞的首字元轉換為大寫

# + [markdown] id="xi8Xz4_7jMfm"
# ## 常用的內建函式 (functions)

# + [markdown] id="tDAmAmhSeHZ8"
# 與方法相似的物件為函式 (functions）。與方法不同的是，呼叫函式時，不需要建立物件，直接呼叫函式即可：執行 `function()`
#
# 接下來我們會以一些常用的內建函式作為範例。
#
# References:
#
# * [Built-in Functions - Python Documentation](https://docs.python.org/3/library/functions.html)
# * [Glossary - Python Documentation](https://docs.python.org/3/glossary.html)

# + [markdown] id="oOqnPexol2lv"
# ### `help()`: 取得某物件的使用說明

# + id="DZvkAsSDaRia" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607417931451, "user_tz": -480, "elapsed": 1288, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d278b295-0047-481c-8078-610f84926cf3"
help(print())  # 取得 print() 函式的使用說明

# + [markdown] id="lHyd2NoIl8Ze"
# ### `type()`: 取得指定物件的物件型態

# + id="VeTQSiIElqNy"
print(type("Hello world!"))  # 取得 "Hello world!" 物件的物件型態

# + [markdown] id="Tm6eciGpl6Dq"
# ### `dir()`: 取得指定物件的屬性 (attributes) 及方法 (methods)

# + [markdown] id="-8kexjculCED"
# > 備註：至於什麼是「屬性」？我們會在類別的章節再次講解。

# + colab={"base_uri": "https://localhost:8080/"} id="qIoIFASjlSjC" executionInfo={"status": "ok", "timestamp": 1606898341677, "user_tz": -480, "elapsed": 1033, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="8d0307e6-3bf3-48e0-98ee-8aa66aea9301"
dir("Hello world!")

# + [markdown] id="Y_zjaNKMl_MM"
# ### `len()`: 取得指定容器 (containers) 物件內含的元素個數

# + [markdown] id="ZS-f9F4apl69"
# 所謂的容器物件，指的是部分物件可以包含其他物件的資料型態。目前我們所認識的只有字串 (`str`)，可以在一個物件包含多個單一字元。這種情況就可以呼叫 `len()` 函式來計算此物件內含的物件個數：

# + id="GO_NYVwFlx4c" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607419346573, "user_tz": -480, "elapsed": 1148, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="86351b81-5a78-484d-fa80-36af32086ee9"
print(len("Hello world!"))  # 計算字串內含有多少個單一字元

# + [markdown] id="o3JvueE6NjGA"
# ## 物件型態轉換函式

# + [markdown] id="SHmuPVEKwJS0"
# 數字物件與字串物件在特定的情況下，是可以互相轉換的。

# + [markdown] id="JFF3dbEieiVL"
# ### `int()`：轉換為整數

# + [markdown] id="H-0-qmAmgCl8"
# #### 由字串轉換為整數

# + id="El84DRXuNk-s" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1606963327375, "user_tz": -480, "elapsed": 860, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="b3ebb86c-4f03-4139-e047-69ea2a8609ba"
s = "10"
print(s)
print(type(s))

# + colab={"base_uri": "https://localhost:8080/"} id="uzwQed5FedHK" executionInfo={"status": "ok", "timestamp": 1606963341419, "user_tz": -480, "elapsed": 869, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="ea28fcc0-d71a-4df2-ef4f-40742e8f4f27"
i = int(s)
print(i)
print(type(i))

# + [markdown] id="KK5ck1wogLmC"
# #### 由浮點數轉換為整數

# + colab={"base_uri": "https://localhost:8080/"} id="XSAOeOOSffX6" executionInfo={"status": "ok", "timestamp": 1606963680774, "user_tz": -480, "elapsed": 738, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d1dc8fd9-58bf-4463-e2da-a5adbe793c7b"
f = 3.14159
print(f)
print(type(f))

# + colab={"base_uri": "https://localhost:8080/"} id="Qi3STILRf8am" executionInfo={"status": "ok", "timestamp": 1606963683499, "user_tz": -480, "elapsed": 770, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="25cc2cfc-df0e-4619-a6ff-073d8d313f38"
i_f = int(f)
print(i_f)
print(type(i_f))

# + [markdown] id="Omapv0DoevKv"
# ### `str()`：轉換為字串

# + [markdown] id="iCCcx6nggjLz"
# #### 由整數轉換為字串

# + colab={"base_uri": "https://localhost:8080/"} id="kabiSTOhe4b1" executionInfo={"status": "ok", "timestamp": 1606963412259, "user_tz": -480, "elapsed": 902, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="7775b285-297d-41e0-efc6-0e0df99baf78"
i = 10
print(i)
print(type(i))

# + colab={"base_uri": "https://localhost:8080/"} id="YcWPBfTCe7fX" executionInfo={"status": "ok", "timestamp": 1606963424403, "user_tz": -480, "elapsed": 814, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="cd81e191-711c-4ee5-943a-db196e43c1be"
s = str(i)
print(s)
print(type(s))

# + [markdown] id="NNJkWli5glVQ"
# #### 由浮點數轉換為字串

# + colab={"base_uri": "https://localhost:8080/"} id="9pB-3xKXzhOK" executionInfo={"status": "ok", "timestamp": 1607421807413, "user_tz": -480, "elapsed": 1369, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="ae53b2ae-4ef8-4bb9-e73a-74c31d587cbf"
f = 3.14159
print(f)
print(type(f))

# + colab={"base_uri": "https://localhost:8080/"} id="0Et29npjzk2x" executionInfo={"status": "ok", "timestamp": 1607421824655, "user_tz": -480, "elapsed": 1002, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d19940fd-7cea-4dba-f66b-15651943a73e"
s = str(f)
print(s)
print(type(s))

# + [markdown] id="o-Y2_jpUe-h2"
# ### `float()`：轉換為浮點數

# + [markdown] id="Ei1JJwJXg22N"
# #### 由整數轉換為浮點數

# + colab={"base_uri": "https://localhost:8080/"} id="VcWzR9aFfHhO" executionInfo={"status": "ok", "timestamp": 1606963911954, "user_tz": -480, "elapsed": 777, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f3247262-2f3c-4adf-cde6-753230cec5a8"
i = 10
print(i)
print(type(i))

# + colab={"base_uri": "https://localhost:8080/"} id="PbbigO8SfNJh" executionInfo={"status": "ok", "timestamp": 1606963516559, "user_tz": -480, "elapsed": 744, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a1ec6179-e772-4ab4-a840-62dae4772065"
f_i = float(i)
print(f_i)
print(type(f_i))

# + [markdown] id="yfKNYbekg5kw"
# #### 由字串轉換為浮點數

# + colab={"base_uri": "https://localhost:8080/"} id="hf5aOb3pgwkC" executionInfo={"status": "ok", "timestamp": 1606963902461, "user_tz": -480, "elapsed": 784, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="384a842f-1b46-4a77-8a73-85b29f1ef7dc"
s = "10"
print(s)
print(type(s))

# + colab={"base_uri": "https://localhost:8080/"} id="-QiOK3L2fRYm" executionInfo={"status": "ok", "timestamp": 1606963558748, "user_tz": -480, "elapsed": 728, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="35a5ff3a-fa84-4200-eea0-59c8c0433b86"
f_s = float(s)
print(f_s)
print(type(f_s))

# + [markdown] id="u-PrZ5avh_RL"
# ### 隱式 (Inplicit) 地由整數轉換為浮點數

# + [markdown] id="3d6Vq0Zs0Tud"
# 多個物件在經由運算子運算過後，會合併成同一個物件，一般來說，不相同的資料型態並不能經由運算子來進行運算。底下僅列出某種特定的例外情形：整數與浮點數運算後，將會隱式 (Inplicit) 地被轉換為浮點數：

# + colab={"base_uri": "https://localhost:8080/"} id="RmJANjAFiKR2" executionInfo={"status": "ok", "timestamp": 1606964326660, "user_tz": -480, "elapsed": 532, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="65c76980-3892-4a5f-d35e-ee79d1a52e1d"
x = 10 + 3.14159
print(x)
print(type(x))

# + [markdown] id="rTYke2IijFmo"
# 為什麼被稱為隱式呢？因為這個表達式並沒有使用 `float()` 函式將整數型態轉換為整數，就直接將整數及浮點數相加。但結果是 Python 會自動將整數轉換為浮點數。
#
# > 備註：其實我們並不建議常常利用這種特性，畢竟這樣有時候會讓程式碼難以維護（可讀性下降）、或是因為轉換失敗而造成錯誤發生，應儘量避免這種狀況。提出這個特性僅是讓各位認識這個機制，且未來在程式出錯時，可以做為一個除錯的追蹤方向。

# + id="LI7qmhka3Hb7"

