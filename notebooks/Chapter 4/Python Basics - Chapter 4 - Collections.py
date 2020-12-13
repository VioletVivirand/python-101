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

# + [markdown] id="8ovgVMJ2Aaql"
# # Chapter 4 - Collections：集合物件

# + [markdown] id="LsU4q5p3BmZP"
# ## Lists：串列

# + [markdown] id="uR7r0OFED3L6"
# 串列 (Lists) 是種序列 (Sequence) 物件，用中括號 (`[]`, Square brackets) 收集許多物件，並在物件之間以逗號 (`,`) 分隔。
#
# 串列裡並不限於裝載相同資料型態的物件。
#
# Reference:
#
# * [List - Python Documentation](https://docs.python.org/3/library/stdtypes.html#lists)
#
# > 備註：可能有讀者在其他的程式語言中學過陣列 (Array) 的概念與用法，雖然類似，但 Python 的串列與其他程式語言的陣列畢竟本質上仍稍有不同，不能混為一談。

# + [markdown] id="poRkpZY-1MDM"
# ### 串列的基本用法

# + colab={"base_uri": "https://localhost:8080/"} id="lv3xyQX2FV4P" executionInfo={"status": "ok", "timestamp": 1607481696653, "user_tz": -480, "elapsed": 1095, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="be947e70-21d5-4ec0-fd95-e6887d5c98c6"
# 創建一個空的串列
empty = []
print(empty)

# + [markdown] id="bMfVwRpejWG1"
# > 備註：或許有些讀者會有從其他程式語言帶來的習慣，也可能曾經看過用 `list()` 建立一個新的、空的串列的用法，在此我表示不建議。在 Python 的設計中，用中括號 `[]` 就是建立一個全新的串列的標準方法，透過 `list()` constructor 的操作的意義並不一樣，連帶的會影響效率。詳情可以查看 `help(list)`。
# >
# > 所以，除非有將物件轉換為串列的用途，其餘建立串列的用途，建議都用中括號 `[]` 的寫法代替就好。而且，寫 Python 就是要寫得優雅、簡潔，何苦又將它複雜化呢？

# + id="x2iBjU12Fabd"
letters = ["a", "b", "c"]     # 放入字串
numbers = [6, 5, 4, 3, 2, 1]  # 放入數字

# + id="Ir6l-4KcJCMC"
mixed = ["one", 2, "3", [4, 5, "F"]]  # 混合不同資料型態物件的串列

# + [markdown] id="yVxibQhZYrA2"
# 在先前的內容中，我們理解字串物件是由很多的單一字元所組成，其實與串列的概念是相仿的。所以在字串中用來索引的方法，在串列也同樣適用：

# + colab={"base_uri": "https://localhost:8080/"} id="sZW8MuK-JRY2" executionInfo={"status": "ok", "timestamp": 1606959812860, "user_tz": -480, "elapsed": 895, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="7b29a33a-7077-4beb-be7f-cd518bf0784d"
# 索引
print(letters[1])  # 在充滿字串的串列中索引
print(numbers[4])  # 在充滿數字的串列中索引

# + colab={"base_uri": "https://localhost:8080/"} id="bJ1BXwJPJgxr" executionInfo={"status": "ok", "timestamp": 1606890755318, "user_tz": -480, "elapsed": 924, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="6395d8f3-2335-42db-ada2-25b0750b7722"
print(mixed[2])     # 在混合不同資料型態物件的串列中索引
print(mixed[3][1])  # 索引串列中的串列物件

# + colab={"base_uri": "https://localhost:8080/"} id="j1mTGYmgJxEM" executionInfo={"status": "ok", "timestamp": 1606890837167, "user_tz": -480, "elapsed": 897, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="979c79f9-e5f7-45f9-9554-1230ca774a10"
print(mixed[1::2])  # 索引的格式一樣是 list[start:stop:step]

# + [markdown] id="pH6eR4zoZhsq"
# 字串中的字元是無法單獨被置換的，但串列可以，只要直接用等號 `=` 將新的物件指定到特定的索引值位置即可：

# + colab={"base_uri": "https://localhost:8080/"} id="J96BD2l2RN9R" executionInfo={"status": "ok", "timestamp": 1607482190583, "user_tz": -480, "elapsed": 1072, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="41815a1c-ce15-474a-c698-2afb6eff8e45"
letters[1] = "B"  # 置換串列內的物件
print(letters)

# + [markdown] id="i_8lAn81bA6r"
# 與字串當的還有可以使用 `in`: 包含測試運算子，可以驗證某物件是否包含在串列內

# + colab={"base_uri": "https://localhost:8080/"} id="ApMrrgQ4JKxE" executionInfo={"status": "ok", "timestamp": 1607482563028, "user_tz": -480, "elapsed": 980, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0fbe1356-8e72-4539-fab5-d63dbef70185"
print("3" in mixed)  # 驗證字串是否存在於串列內
print(3 in mixed)    # 驗證數字是否存在於串列內

# + colab={"base_uri": "https://localhost:8080/"} id="yGT3gaPfJPMX" executionInfo={"status": "ok", "timestamp": 1607482670029, "user_tz": -480, "elapsed": 1440, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="dbaccd47-1758-4d5e-8cfd-e1a67d1787dd"
print("F" in mixed)  # "F" 實際是包含在 mixed 串列中、index = 3 的串列內
                     # 那麼驗證的結果是如何呢？

# + [markdown] id="3dVzkL1DXryd"
# ### 搭配內建函式使用

# + [markdown] id="Nm1rRdNXYqsO"
# #### `len()`：計算串列內有多少物件

# + [markdown] id="bjvC5zHJm_ho"
# References:
#
# * [len() - Python Documentation](https://docs.python.org/3/library/functions.html#len)

# + colab={"base_uri": "https://localhost:8080/"} id="MNnmalUJVWlu" executionInfo={"status": "ok", "timestamp": 1607482949595, "user_tz": -480, "elapsed": 1194, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f13dfb14-aa62-44e1-e725-5b1ad86f8657"
numbers = [6, 5, 4, 3, 2, 1]
print(len(numbers))

# + colab={"base_uri": "https://localhost:8080/"} id="1HCKhE3Mc_JA" executionInfo={"status": "ok", "timestamp": 1607483095297, "user_tz": -480, "elapsed": 1028, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a9aa2605-d6c7-4e06-a7cc-097e9801d276"
mixed = ["one", 2, "3", [4, 5, "F"]]  # 思考一下：如果串列中還有串列，這樣到底有幾個物件呢？
print(len(mixed))

# + [markdown] id="6LG7bAJhYvkI"
# #### `sorted()`：對串列內的內容排序

# + [markdown] id="Pp_WB9rFepI7"
# 要注意的是：`sorted()` 函式僅會回傳排序後的結果，串列本身並不會被修改：
#
# References:
#
# * [sorted() - Python Documentation](https://docs.python.org/3/library/functions.html#sorted)

# + colab={"base_uri": "https://localhost:8080/"} id="FiAjo-upXwS_" executionInfo={"status": "ok", "timestamp": 1607483555730, "user_tz": -480, "elapsed": 899, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="88546f2c-baa9-496c-dba7-d36c7b4ca0e9"
numbers = [6, 5, 4, 3, 2, 1]
print(sorted(numbers))  # 觀察經過 sorted() 函式處理後的內容
print(numbers)          # 觀察 numbers 串列本身：並不會被更動

# + [markdown] id="xVQuT1yjfbHI"
# `sorted()` 預設是使用遞增排序，也可以使用遞減排序，方法是加上設定 `reverse` 參數 (Parameter) 為 `True`：

# + colab={"base_uri": "https://localhost:8080/"} id="sk-LsWNdfW3J" executionInfo={"status": "ok", "timestamp": 1607483747872, "user_tz": -480, "elapsed": 867, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1da65f67-e993-49de-b873-078fab31c9bb"
numbers = [1, 2, 3, 4, 5, 6]
print(sorted(numbers, reverse=True))  # 遞減排序

# + [markdown] id="vvhwtSv1f4Zt"
# > 備註：參數 (Parameters) 是什麼？我們將會在自訂函式的章節中提及。

# + [markdown] id="WvfnQwPlgIFM"
# > 順帶一提：如果要永久將串列的內容變更為排序後的結果，我們可以調用串列本身的 `list.sort()` 方法，這會在底下：串列方法的小節中介紹。

# + [markdown] id="j20qLOGhKUoN"
# #### `del()`：移除串列中的物件

# + [markdown] id="ZMh_tzAKpyrs"
# References:
#
# * [The del statement - Python Documentation](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-del-stmt)

# + colab={"base_uri": "https://localhost:8080/"} id="NXLLdCkOKFDh" executionInfo={"status": "ok", "timestamp": 1607484151234, "user_tz": -480, "elapsed": 835, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="6afdf8b3-52be-402a-a47a-e38637b9eaf3"
letters = ["a", "b", "c", "d", "e", "f", "g"]
del(letters[1])  # 直接在 del() 函式指定串列物件的索引值，即可移除該物件
print(letters)

# + colab={"base_uri": "https://localhost:8080/"} id="ZchiDz8KKfq3" executionInfo={"status": "ok", "timestamp": 1607485028865, "user_tz": -480, "elapsed": 817, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="2763ef0c-1e1d-4d7d-ec4c-09d4b4a75f63"
letters = ["a", "b", "c", "d", "e", "f", "g"]
del(letters[3:6])  # 也可以一次刪除多個物件
print(letters)

# + [markdown] id="AHPpHpvtpoAt"
# > 備註：眼尖的各位可能有機會發現，其實 `del` 關鍵字在 Python 的官方文件裡是個陳述式 (statements)，其實在執行時不用寫成函式 `del()` 的型態也可以執行。
# >
# > 有什麼差異呢？執行上的感覺是沒有差異的，但礙於篇幅，暫時不多作解釋。有興趣的各位可以自行搜尋看看！

# + colab={"base_uri": "https://localhost:8080/"} id="Y_1506N0n2UY" executionInfo={"status": "ok", "timestamp": 1607486513954, "user_tz": -480, "elapsed": 870, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1fec483d-36a7-49ad-d265-2536fdb7ab1c"
letters = ["a", "b", "c", "d", "e", "f", "g"]
del letters[0]  # 用陳述式的方式來操作刪除功能
letters

# + [markdown] id="84hRx96cLAgy"
# ### 串列方法

# + [markdown] id="2As2qjN4LD2R"
# #### `list.append()`：新增物件至串列內

# + [markdown] id="sQ5i-ifkk_X9"
# 使用 `list.append()` 方法將**一個**物件加入至現有串列內：

# + colab={"base_uri": "https://localhost:8080/"} id="qFsMrXktKr-i" executionInfo={"status": "ok", "timestamp": 1606891454191, "user_tz": -480, "elapsed": 976, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="6f30803a-4bfe-4ea5-a81c-c1cba59cc1a3"
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters.append("h")
print(letters)

# + [markdown] id="SLVcM-yblyOX"
# 但 `list.append()` 方法無法一次新增多個物件：

# + colab={"base_uri": "https://localhost:8080/"} id="6jQ5XBAkK3Jk" executionInfo={"status": "ok", "timestamp": 1606891526868, "user_tz": -480, "elapsed": 870, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="72f5325d-a385-4cc4-8915-8494970b0c43"
letters = ["a", "b", "c", "d", "e", "f", "g"]

# letters.append("h", "i")  # 無法一次新增多個物件，執行此段會出現錯誤

letters.append(["h", "i"])  # 雖然可以將另一個串列加入
                            # 但這個串列依然是以「一個物件」的身份被加入到串列內的
print(letters)

# + [markdown] id="TVl5VV7Hl4gQ"
# 若要將另一個串列的物件**一個個**的加入現有串列中，有兩個方法：
#
# 1. 透過 `list.extend()` 方法
# 2. 透過 `+` 運算子來連接兩個串列

# + colab={"base_uri": "https://localhost:8080/"} id="gGZRBDmHMtb0" executionInfo={"status": "ok", "timestamp": 1607485413305, "user_tz": -480, "elapsed": 884, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="7dcfdbb8-e6f3-44e1-f0b1-0bcf4be596c6"
# 透過 list.extend() 方法
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters.extend(["h", "i"])
print(letters)

# + colab={"base_uri": "https://localhost:8080/"} id="iHOHHJJbNA9P" executionInfo={"status": "ok", "timestamp": 1606892446590, "user_tz": -480, "elapsed": 694, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="ad389fb4-df13-4e72-b82f-4612f7f82999"
# 透過 + 運算子來連接兩個串列
letters = ["a", "b", "c", "d", "e", "f", "g"]
more_letters = letters + ["h", "i", "j"]
print(more_letters)

# + [markdown] id="uvOxgYHDQLoC"
# #### `list.remove()`：移除串列內的物件

# + [markdown] id="Px5GOqXB4Zog"
# 透過 `list.remove()` 的方式，並直接指定要刪除的物件內容。不同於使用 `del()` 或 `del` 陳述式需要指定索引值去刪除。
#
# 但若有多個相符的物件，只會將**第一個**相符的物件移除：

# + colab={"base_uri": "https://localhost:8080/"} id="JAfDsyA2U-BJ" executionInfo={"status": "ok", "timestamp": 1607490405053, "user_tz": -480, "elapsed": 966, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="66bbea57-e8f1-475f-8f4c-6abe7bb86980"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.remove(3)  # 移除串列內的數字物件 3
print(numbers)
print(len(numbers))

# + colab={"base_uri": "https://localhost:8080/"} id="4bi2MYGI5TNq" executionInfo={"status": "ok", "timestamp": 1607490460674, "user_tz": -480, "elapsed": 811, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="663bc40d-5fb1-4ae4-8838-3a744d9960c2"
numbers = [1, 1, 2, 3, 4, 5]
numbers.remove(1)  # 移除串列內的數字物件 1，但因有多個相符的物件，只會刪除第一個
print(numbers)

# + colab={"base_uri": "https://localhost:8080/"} id="Ephn25b55eCq" executionInfo={"status": "ok", "timestamp": 1607490527131, "user_tz": -480, "elapsed": 1083, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="644b2502-fca8-4ed0-a26c-54f0656f5a43"
mixed_numbers = [[1, 2, 3], [4, 5], 6]
mixed_numbers.remove([4, 5])  # 也可以移除串列裡的串列，只要物件相符都沒有問題
print(mixed_numbers)

# + [markdown] id="Ckr2uB027vsE"
# #### `list.pop()`：依照後進先出規則移除物件並回傳結果

# + [markdown] id="L_rfb2MC5vR1"
# 而另一個移除物件的方法是呼叫 `list.pop()`。
#
# 若在執行時不代入需要移除的物件，預設會以「後進先出」的方式，將索引值最大的物件給移除，並在執行的時候回傳該物件。

# + colab={"base_uri": "https://localhost:8080/"} id="gQOJsz-wVIjI" executionInfo={"status": "ok", "timestamp": 1606894298675, "user_tz": -480, "elapsed": 992, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="df7c7429-6b16-48d2-b178-5a23f98c14c4"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dropped_number = numbers.pop()  # 不代入需要移除的物件，則物件將會移除並回傳
                                # 所以我們可以將回傳的內容存放於一個物件中
print(numbers)
print(dropped_number)
print(len(numbers))

# + [markdown] id="-u6m2FSw8Ef2"
# 也可以代入欲移除的索引值，一樣會移除並回傳物件內容：

# + colab={"base_uri": "https://localhost:8080/"} id="AuHgyXTi763y" executionInfo={"status": "ok", "timestamp": 1607491181445, "user_tz": -480, "elapsed": 989, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f4a24ec4-3144-44cb-d7cd-40902fcae8c0"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dropped_number = numbers.pop(7)  # 指定要移除的物件索引值
print(numbers)
print(dropped_number)
print(len(numbers))

# + [markdown] id="42wNFOCg6mYe"
# #### `list.sort()`：排序串列內的物件

# + [markdown] id="F_M69Q576pFO"
# 與使用 `sorted()` 函式不同的地方是：調用 `list.sort()` 方法將永久改變串列的內容，且執行的當下不會回傳任何結果。

# + colab={"base_uri": "https://localhost:8080/"} id="qvxOzfvVWvRd" executionInfo={"status": "ok", "timestamp": 1606901539539, "user_tz": -480, "elapsed": 741, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="9fb4fc6b-588e-4144-9a12-e1b5ec50a970"
numbers = [6, 5, 4, 3, 2, 1]
print(numbers)

# 使用 list.sort() 方法排序
numbers.sort()  # 串列的 list.sort() 方法並不會回傳結果，所以可以單獨執行
print(numbers)  # 串列內容已被變更為排序後的結果

# + [markdown] id="wsfCU8d7zVd6"
# ## Dicts: Dictionaries 字典

# + [markdown] id="fDnqmxwzzqxM"
# 就如其名「字典」一樣的形式，`dict` 物件需要由 Key（鍵）去對應到相對的 Value（值），所以有時候會稱這種物件為 Mapping type：對應的資料型態，或稱為 Key : Value pair：鍵值對（每一筆資料都是由成對的鍵與值組成）。
#
# 字典的建立是用大括號 `{}` (Curly brackets) 將一個一個鍵值對以冒號 `:` 隔開後，置於大括號之內。每一個鍵必須是獨一無二的內容，不可重複。
#
# Reference:
#
# * [Dict - Python Documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

# + [markdown] id="KTKpxUYp1Plv"
# ### 字典的基本用法

# + id="X86cc1yF0bpv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607502891161, "user_tz": -480, "elapsed": 1205, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3b26362b-1966-4d86-c6ff-ac4421e6d48a"
# 創建一個空的字典
d = {}
print(d)

# + [markdown] id="lkDCqOFho4a6"
# > 備註：如同前面串列提到的相似，在此還是建議：建立一個新的字典物件一律使用大括號 `{}` 建立，`dict()` constructor 還是建議在需要做型態轉換時使用。
# >
# > 保持程式的簡潔及可讀性，是 Python 開發者留給這個世界的最佳禮物！

# + colab={"base_uri": "https://localhost:8080/"} id="LUOj438QqWRq" executionInfo={"status": "ok", "timestamp": 1607503344056, "user_tz": -480, "elapsed": 938, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f2081461-6060-425d-8ded-5aa39f252b94"
# 拿個人的基本資料，做一個簡單的範例
profile = {
    "name": "Vivi",  # 名字
    "age": 18        # 年齡
}
print(profile)

# + [markdown] id="4w0fhaNUKGVt"
# > 補充：現在起，各位應該會寫一些較複雜、多行的表達式。在 Python 中，要表示物件的階層關係，是在底下多一層時，加入用**四個空白鍵**空白組成的縮排。
# > 或許有讀者在其他語言的習慣是兩個空白鍵，或是用 <button>Tab ↹</button> 按鈕來縮排，不過不建議這樣做。詳情請參考 [PEP 8](https://www.python.org/dev/peps/pep-0008/#indentation) 及 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#s3.4-indentation) 文件中關於 Indentation 的章節。
# >
# > 
# > 以下舉例說明：

# + id="AMOej1mYK59j"
obj = {
    "Level-1": {
        "Level-2": {
            "Level-3": {
                # ......依此類推
            }
        }
    }
}

# + [markdown] id="0VPkJcLMrzNA"
# > 備註：因為字典物件的內容通常比較複雜，為了讓各位比較好閱讀，這裡用個內建的模組 `pprint` 來輔助顯示：

# + id="pt4o_AQRrl5f"
from pprint import pprint

# + [markdown] id="Q18phfnm0y1d"
# 備註：`import` 跟 `from` 都是在載入模組 (Module) 時會用到的陳述句，在本次的課程中會比較少見，請大家先記著就好。

# + colab={"base_uri": "https://localhost:8080/"} id="IKu0tyxy0fuy" executionInfo={"status": "ok", "timestamp": 1607561592028, "user_tz": -480, "elapsed": 856, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="fec72715-090d-4e37-ac4a-49ccda4f1050"
# 再做得稍微複雜一點
profile = {
    "name": "Vivi",
    "age": 18,
    "skills": [
        "eating",
        "sleeping",
        "doing nothing",
        "being lazy",
    ],
    "memo": "I wanna go home",
}
pprint(profile)

# + colab={"base_uri": "https://localhost:8080/"} id="vbiICVCi06Gm" executionInfo={"status": "ok", "timestamp": 1607504842700, "user_tz": -480, "elapsed": 1269, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="7a218b41-29f1-468b-9b4b-5adb6489c00e"
# 索引
print(profile["name"])    # 調閱個人檔案內的名字
print(profile["skills"])  # 調閱個人檔案內的技能

# + id="H6JB_irEQca6" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607504842701, "user_tz": -480, "elapsed": 1112, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="62fa6ff3-6b91-4275-ced7-f027ef71428b"
# 置換已經存在的內容
profile["age"] = 32
print(profile["age"])

# + colab={"base_uri": "https://localhost:8080/"} id="zwKhT1hbrRg7" executionInfo={"status": "ok", "timestamp": 1607504844084, "user_tz": -480, "elapsed": 745, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3213009e-b5e1-46b6-fc9e-f05ec5f14683"
# 新增內容
profile["deposit"] = 100000  # 透過指定內容到不存在的鍵上以新增內容
pprint(profile)

# + colab={"base_uri": "https://localhost:8080/"} id="TgDHvgVu1HLi" executionInfo={"status": "ok", "timestamp": 1607504845593, "user_tz": -480, "elapsed": 926, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3ac16c1d-6e74-4179-e6a2-288b3664b147"
# 刪除內容
del(profile["memo"])  # 刪除指定的鍵
pprint(profile)

# + [markdown] id="xdWicJcCsYeq"
# 使用 `in`: 包含測試運算子，可以驗證某物件是否包含在字典的鍵之內：

# + colab={"base_uri": "https://localhost:8080/"} id="h-CD7d4Smo_K" executionInfo={"status": "ok", "timestamp": 1607504847188, "user_tz": -480, "elapsed": 770, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3d3ae133-1a05-46eb-b110-a6d48d87f5b0"
# 驗證 skills 是否存在於 profile 字典物件的鍵之內
print("skills" in profile)

# + colab={"base_uri": "https://localhost:8080/"} id="Lme0TiDOmyU8" executionInfo={"status": "ok", "timestamp": 1607504848992, "user_tz": -480, "elapsed": 790, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="3fe6fac3-d434-4bb5-94cb-d9c25b446420"
# 測試一下：是否可以用 in 來檢查物件是否存在於該字典的值之內？不行。
print("eating" in profile)

# + [markdown] id="YOiQD2yJtDuz"
# > 備註：那是否可以用別的方法，來檢查某物件是否存在於字典內的任何值之內？這邊先緩緩，等到後面的章節教完以後，就會有方法了。

# + [markdown] id="fABRLrHxMCwo"
# ### 字典方法

# + [markdown] id="PULwQuu4ta5A"
# #### `dict.get()`：獲得字典內特定鍵的值

# + colab={"base_uri": "https://localhost:8080/"} id="37rBnqkxME7i" executionInfo={"status": "ok", "timestamp": 1607504852354, "user_tz": -480, "elapsed": 1298, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="5ef75383-9b1f-43f6-c4ab-d9e58b169439"
print(profile.get("name"))
print(profile["name"])

# + [markdown] id="mUXOHdKGtjNH"
# 在上面的範例中，`profile.get("name"))` 與 `print(profile["name"]` 的表達式是等價的。那差別在哪裡呢？在於今天如果無法確定某鍵是否存在於字典內，用 `dict.get()` 方法可以在遇到鍵不存在的情況值回傳 `None` 物件，而用索引的方式則會直接出現錯誤。

# + colab={"base_uri": "https://localhost:8080/"} id="vRE6hhDlMV3n" executionInfo={"status": "ok", "timestamp": 1607504853409, "user_tz": -480, "elapsed": 863, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="94cf4265-d521-4491-9a20-15491d677925"
# 測試從不存在的鍵之內獲得值
print(profile.get("salary"))
# print(profile["salary"])  # 用索引的方式獲值，在該鍵不存在時會引發 Runime error

# + [markdown] id="Z-g0SWgIukRT"
# #### `dict.key()`：獲得字典內的所有鍵

# + colab={"base_uri": "https://localhost:8080/"} id="_OwHuKOZMy_I" executionInfo={"status": "ok", "timestamp": 1607504855046, "user_tz": -480, "elapsed": 634, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f2fe16e4-8553-4c26-e908-b9a089f88ba5"
print(profile.keys())

# + [markdown] id="KsayxE-uuusU"
# #### `dict.pop()`：移除字典內的物件並回傳結果

# + [markdown] id="CEKPAa6wv2fL"
# 與串列的用法相似，調用 `dict.pop()` 並代入欲從字典內移除的鍵，將可以將該鍵值對移除、並回傳該鍵的值。

# + colab={"base_uri": "https://localhost:8080/"} id="iB6rISaTM_qE" executionInfo={"status": "ok", "timestamp": 1607504861185, "user_tz": -480, "elapsed": 854, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="20832265-9429-4870-f0ca-6c0a9cd11e63"
# 將個人資料中的年齡移除，並存放於物件中
vivi_age = profile.pop("age")
print(vivi_age)
pprint(profile)

# + [markdown] id="dOvosknSyqUh"
# ## 複製可變型別物件

# + [markdown] id="CZ43RPOVxL7V"
# 在 Python 物件中，其實有著**可變** (Mutable) 型態與**不可變** (Immutable) 型態的區別。到目前為止，在我們學到的物件中：
#
# * 不可變 (Immutable) 型態：`int`, `float`, `str`
# * 可變型態 (Mutable) 型態：`list`, `dict`
#
# 而對於可變型態的物件，在想要複製此物件時，如果沒有透過呼叫該物件的 `copy()` 方法，存粹用等號 `=` 將可變型態物件指定到一個新的物件上，將導致兩個物件實際上依然指向同一個記憶體位置，而編輯一個物件時，另一個物件依然會被更動到。
#
# 以下我們分別針對串列及字典來處理這個問題。

# + [markdown] id="1erP_jCrOaEz"
# ### 複製串列

# + [markdown] id="35Rg6DxuzRln"
# 我們先測試用等號 `=` 將串列指定給一個新的物件，並嘗試對任意一個串列操作：

# + colab={"base_uri": "https://localhost:8080/"} id="fTwvoFHgNODA" executionInfo={"status": "ok", "timestamp": 1607505690436, "user_tz": -480, "elapsed": 834, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="9ea44434-19d2-4292-81be-7499946a1cd5"
list_1 = [1, 2, 3, 4, 5]  # 建立新串列物件
list_2 = list_1           # 將原串列指定給新的物件
print(list_1)
print(list_2)

# + colab={"base_uri": "https://localhost:8080/"} id="RKc4qjnMOrWu" executionInfo={"status": "ok", "timestamp": 1606959177597, "user_tz": -480, "elapsed": 714, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="00b24c33-8909-405b-9ad4-e980774dbd30"
list_1.pop()  # 移除串列中的物件
print(list_1)
print(list_2)

# + [markdown] id="EIXrBlbqzu1s"
# 原本我們只執行 `list_1` 串列的 `pop()` 方法，移除了 `list_1` 串列中的最後一個物件，實際發生的情況是：`list_2` 串列中的物件也一併被移除了。
#
# 所以我們可以調用 `list.copy()` 方法來複製串列物件：

# + colab={"base_uri": "https://localhost:8080/"} id="ytMJ4D8FOyoZ" executionInfo={"status": "ok", "timestamp": 1607505866203, "user_tz": -480, "elapsed": 923, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="39674aff-037e-403b-98cb-5a9476c8445f"
list_1 = [1, 2, 3, 4, 5]  # 建立新串列物件
list_2 = list_1.copy()    # 複製串列為新的物件
print(list_1)
print(list_2)

# + colab={"base_uri": "https://localhost:8080/"} id="tchQ7w7sO47r" executionInfo={"status": "ok", "timestamp": 1607505901180, "user_tz": -480, "elapsed": 1056, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="e92817d6-774b-4d73-d15c-9fc629b85e32"
list_1.pop()      # 將 list_1 串列中的最後一個物件移除
list_2.remove(2)  # 將 list_2 串列中的 2 物件移除
print(list_1)
print(list_2)

# + [markdown] id="eqd0SJE80XjL"
# 由此可見，兩個物件就有成功被獨立開來了。

# + [markdown] id="8wReUBgXP5Qu"
# ### 複製字典

# + [markdown] id="2uQr8bKFIZrm"
# 接著，我們一樣先測試用等號 `=` 將字典指定給另一個物件，並嘗試對任意一個字典進行操作：

# + colab={"base_uri": "https://localhost:8080/"} id="WXOdZKjeP7E-" executionInfo={"status": "ok", "timestamp": 1607561671133, "user_tz": -480, "elapsed": 788, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="64041d8f-e9ee-47e4-9c10-86059d231677"
dict_1 = {       # 建立新字典物件
    "one": 1,
    "two": 2,
    "more": {
        "three": 3,
        "four": 4
    }
}
dict_2 = dict_1  # 將原字典指定給新的物件
pprint(dict_1)
pprint(dict_2)

# + id="zemnr57XQSzu" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1607561785245, "user_tz": -480, "elapsed": 1338, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="183fd0ac-fcdd-4355-c9ec-3431f71b7253"
dict_1["one"] = "The first number"  # 新增一個鍵值對
pprint(dict_1)
pprint(dict_2)

# + [markdown] id="Np1lqf33Jmuh"
# 看起來我們在 `dict_1` 新增了一個鍵，但是 `dict_2` 也一樣受到影響了。
#
# 接著我們就來調用 `dict.copy()` 方法來複製字典：

# + colab={"base_uri": "https://localhost:8080/"} id="IEU-bJThSqQ3" executionInfo={"status": "ok", "timestamp": 1607562899118, "user_tz": -480, "elapsed": 948, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="fffd78bf-b3ef-47cf-e3a4-5a3951ea7400"
dict_1 = {                           # 建立新字典物件
    "one": 1,
    "two": 2,
    "more": {
        "three": 3,
        "four": 4
    }
}
dict_2 = dict_1.copy()               # 複製字典為新的物件
dict_1["two"] = "The second number"  # 新增一個鍵值對
pprint(dict_1)
pprint(dict_2)

# + [markdown] id="BvJelLwLMc63"
# 看似可以正確地將字典複製出來了！接著我們看一個更進階的範例：如果在字典物件裡面對裡面的字典操作呢？

# + colab={"base_uri": "https://localhost:8080/"} id="BRN2Ul2mTGhI" executionInfo={"status": "ok", "timestamp": 1607562900596, "user_tz": -480, "elapsed": 551, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="0b78344a-2221-46c4-deae-0ade8520c42c"
dict_1["more"]["three"] = "The third number"  # 對 dict_1["mode"] 字典新增一個鍵值對
pprint(dict_1)
pprint(dict_2)

# + [markdown] id="v8S6p5koM6B_"
# 看起來，`dict.copy()` 方法雖然可以成功地複製出字典，但針對「字典中的字典」卻沒有辦法好好複製出來、成為一個獨立的物件。於是我們要透過內建的 `copy` 模組中的 `deepcopy` 函式來解決這個問題：

# + id="rpmDhqpKTY-p"
from copy import deepcopy

# + colab={"base_uri": "https://localhost:8080/"} id="4Jgm9ab6TXXU" executionInfo={"status": "ok", "timestamp": 1607562906380, "user_tz": -480, "elapsed": 1105, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a8598cae-64e0-4e0e-f3cf-0cbb35fe49db"
dict_1 = {                 # 建立新字典物件
    "one": 1,
    "two": 2,
    "more": {
        "three": 3,
        "four": 4
    }
}
dict_2 = deepcopy(dict_1)  # 使用 deepcopy() 函式來複製字典
pprint(dict_1)
pprint(dict_2)

# + colab={"base_uri": "https://localhost:8080/"} id="W_9KtJuCNu3K" executionInfo={"status": "ok", "timestamp": 1607562914810, "user_tz": -480, "elapsed": 887, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="10620176-c2e5-4dd2-c4c4-b61186fc74a6"
dict_1["two"] = "The second number"           # 在字典中新增鍵值對
dict_1["more"]["three"] = "The third number"  # 在字典中的字典新增鍵值對
pprint(dict_1)
pprint(dict_2)

# + id="NIbp6ZLYN2f1"

