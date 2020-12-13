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

# + [markdown] id="k91y6QPYeq_z"
# # Chapter 7 - Classes - 類別

# + [markdown] id="sqOS3crNmHH-"
# 在前面的章節中，我們使用了相當多內建的物件，並調用物件的方法做出許多應用。
#
# 接下來開始可以製作我們需要的物件類別 (Classes)。類別可以想像為物件的範本，裡面可以定義類別的建構子 (Constructor)、屬性 (Attributes) 及方法 (Methods)，最後用這個範本去產生物件實例 (Instances)。
#
# 物件類別之間還可以繼承 (Inherit)，讓物件之間可以保留部分相同的成分，並對不同的成分做出微調。
#
# 這些都是物件導向 (Object-oriented) 程式設計中相當重要的概念。筆者喜歡以貓科動物的類別來當例子，用以講解物件類別設定及繼承的概念，希望可以讓各位讀者更容易理解。

# + [markdown] id="t1ulxeALkYwh"
# References:
#
# * [Classes - Python Documentation](https://docs.python.org/3/tutorial/classes.html)

# + [markdown] id="2115_vnDkqee"
# ## 建立物件類別 (Classes) 及物件實例 (Instances)

# + [markdown] id="7odfOYWurZwf"
# 用關鍵字 `class` 來定義一個新的物件類別。物件類別名稱的首字並定要為大寫英文字：

# + id="9OdWSSWKoEY6" executionInfo={"status": "ok", "timestamp": 1607840017461, "user_tz": -480, "elapsed": 782, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Cat:  # 建立新的物件類別 Cat（貓類別）
    pass    # 暫時不撰寫內容


# + [markdown] id="rizcihWVr92b"
# 接著將物件類別指定到一個新的物件上，來初始化 (Initialize) 這個類別的一個物件。

# + colab={"base_uri": "https://localhost:8080/"} id="Ur7KmCBkoHS7" executionInfo={"status": "ok", "timestamp": 1607839503199, "user_tz": -480, "elapsed": 785, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="2dd0a905-be9e-4349-9a9a-1ebe0d8eb72a"
cat = Cat()       # 建立一個新的物件 cat（一隻貓），而 cat 物件是由類別 Cat 初始化而來
                  # 括號內可傳入參數至建構子內，會在下一個小節講解
print(type(cat))  # 驗證此物件的類別


# + [markdown] id="POzmqeALpLO9"
# ## 建構子 (Constructor)

# + [markdown] id="IUqiAx_8tQzr"
# 一般在建立一個類別時，會一併製作建構子，用途是在初始化類別實例時，設定可以一併執行的操作，或透過傳入參數來設定新的物件中的組成。
#
# > 備註：其實 Python 並沒有建構子 (Constructor) 的定義，但類別中的 `__init__()` 方法與其他的程式語言中的建構子的功能是一致的，所以在這裡借用其他程式語言的稱呼。

# + id="cDwledWVpNX_" executionInfo={"status": "ok", "timestamp": 1607840122523, "user_tz": -480, "elapsed": 1015, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Cat:
    def __init__(self):              # Cat 貓類別的建構子
        print("A new cat is born!")  # 當實例被建立時，提示有一隻新的貓出生了！


# + colab={"base_uri": "https://localhost:8080/"} id="Ikxx-gOCpS2Y" executionInfo={"status": "ok", "timestamp": 1607840122859, "user_tz": -480, "elapsed": 1133, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f6d4da8a-456e-4838-b85b-0e9c4aa6e685"
cat = Cat()  # 初始化一隻貓


# + [markdown] id="omiVVeC_oNYR"
# ## 屬性 (Attributes)

# + [markdown] id="y95mXsClvlbw"
# 上一個小節有提到：建構子通常也用來在初始化物件時，用傳入參數的方式來定義一個物件的組成。我們用貓類別當做例子，每隻貓會有不同的花色、身長、重量，透過建構子即可輕易的在初始化時將一隻貓的屬性給定義好。

# + id="Rm8JBABWoQEN" executionInfo={"status": "ok", "timestamp": 1607840960586, "user_tz": -480, "elapsed": 698, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Cat:
    def __init__(self, color, height, weight):  # 在建構子中定義三個要傳入的屬性：花色、身長、重量
        self.color = color                      # color 為傳入的屬性值，將其指定給此物件的屬性值 self.color
        self.height = height                    # height 為傳入的屬性值，將其指定給此物件的屬性值 self.height
        self.weight = weight                    # weight 為傳入的屬性值，將其指定給此物件的屬性值 self.weight


# + [markdown] id="yzmvmbGlx4u9"
# > 備註：在類別定義中，所有方法都要傳入 `self` 物件，但在初始化時即可忽略。

# + id="SYN4QZ3yoSGS" executionInfo={"status": "ok", "timestamp": 1607840991505, "user_tz": -480, "elapsed": 819, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
cat = Cat('white', 20, 2)  # 初始化新的貓，並將花色、身長、重量屬性設定值傳入

# + colab={"base_uri": "https://localhost:8080/"} id="kxxCyTTzpzjV" executionInfo={"status": "ok", "timestamp": 1607841200577, "user_tz": -480, "elapsed": 827, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="da921e3a-63d8-4da5-9714-6cf359588f00"
print(cat.color)  # 調用貓物件的屬性值
                  # 注意：因為屬性不會接入傳入參數，所以屬性名稱之後不用加上括號 "()"

# + colab={"base_uri": "https://localhost:8080/"} id="-iSsJgEDoTmE" executionInfo={"status": "ok", "timestamp": 1607841124540, "user_tz": -480, "elapsed": 1356, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="c020fbcf-a6c7-441c-df3a-842a27d3c977"
# 嘗試調用所有貓物件的屬性值
print("The color of this cat is", cat.color)
print("The height of this cat is", str(cat.height), "cm")
print("The weight of this cat is", str(cat.weight), "kg")

# + colab={"base_uri": "https://localhost:8080/"} id="qdrMBeBPzBQk" executionInfo={"status": "ok", "timestamp": 1607841117568, "user_tz": -480, "elapsed": 776, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="a58df344-d594-4a0a-f667-9aebb9c1b7a7"
print(dir(cat))  # 查看貓物件的所有可執行操作


# + [markdown] id="W0dtfJjXpoj3"
# ## 方法 (Methods)

# + [markdown] id="M4WBe3CA2MpC"
# 方法 (Methods) 其實就是：附加在物件上的函式。也因為附加在物件上，所以方法內通常會搭配調用物件本身的屬性值，來執行各式各樣的操作。

# + id="6Ypwz0ypeh8l" executionInfo={"status": "ok", "timestamp": 1607842357958, "user_tz": -480, "elapsed": 879, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Cat:
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight
    
    def roar(self):     # 幫貓類別定義「吼叫」的方法
        print("Meow!")  # 發出叫聲
        return "Meow!"  # 回傳叫聲內容
    
    def describe(self):                                # 幫貓類別定義「描述」方法
        print("My color is", self.color)               # 描述這隻貓自己的花色
        print("My height is", str(self.height), "cm")  # 描述這隻貓自己的身長
        print("My weight is", str(self.weight), "kg")  # 描述這隻貓自己的重量


# + id="4KXwflx-mpfL" executionInfo={"status": "ok", "timestamp": 1607842358297, "user_tz": -480, "elapsed": 1203, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
cat = Cat('white', 20, 2)  # 初始化一隻貓

# + colab={"base_uri": "https://localhost:8080/"} id="4VvdOQ-3nLqd" executionInfo={"status": "ok", "timestamp": 1607842358298, "user_tz": -480, "elapsed": 1181, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="42e18c88-c1bd-4642-dc12-2c89105e993a"
cat_sound = cat.roar()  # 讓貓吼叫，並將叫聲記錄於物件內

# + colab={"base_uri": "https://localhost:8080/"} id="ehK5EFmYnee4" executionInfo={"status": "ok", "timestamp": 1606982477223, "user_tz": -480, "elapsed": 638, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="4eb7b5e4-fdce-432d-e4c9-511e2255fd04"
print(cat_sound)  # 顯示貓的叫聲

# + colab={"base_uri": "https://localhost:8080/"} id="s2svrV-1nf6L" executionInfo={"status": "ok", "timestamp": 1607842391429, "user_tz": -480, "elapsed": 678, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="f2fca84c-1e30-48de-95a6-aec122a495fa"
cat.describe()  # 讓貓描述自己的花色、身長、體重


# + [markdown] id="EVKCoQcEnhj5"
# ## 繼承 (Inheritance)

# + [markdown] id="Pd7XR3UK3_K9"
# 物件之間若有某些程度的相似性，可以用繼承的方式，在建立一個新的物件的同時，將同樣的成分直接保留，並加上或修改不同的成分。
#
# 在此用老虎類別來舉例：老虎也是貓科動物，所以貓有的屬性，老虎也都有，也可以描述自己的花色、身長、體重，但是吼叫聲可能不同。所以我們在建立老虎類別時，可以先從貓類別繼承，之後改寫老虎的吼叫聲就好。
#
# 這個貓類別與老虎類別的關係中：
#
# * Cat 貓類別為 Tiger 老虎類別的**父類別**或**親類別** (Parent class)
# * Tiger 老虎類別為 Cat 貓類別的**子類別** (Child class)

# + id="gqu_Zr9-qEvq" executionInfo={"status": "ok", "timestamp": 1607842532117, "user_tz": -480, "elapsed": 876, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Tiger(Cat):    # 老虎也是貓科動物，所以貓有的屬性老虎也會有，用繼承就不用改寫這些屬性
    def roar(self):  # 但老虎跟貓的叫聲有相當大的差異，所以我們只改寫這個部分
        print("Ahhhhhhh!")
        return "Ahhhhhhh!"


# + id="rDg4BuTGsp3-" executionInfo={"status": "ok", "timestamp": 1607842547995, "user_tz": -480, "elapsed": 894, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
tiger = Tiger(color="yellow", height=180, weight=100)  # 初始化一隻老虎

# + colab={"base_uri": "https://localhost:8080/"} id="hRoyJO17ssAc" executionInfo={"status": "ok", "timestamp": 1607842555674, "user_tz": -480, "elapsed": 806, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="9aa91938-b79a-421c-9a72-0a2090627ddd"
tiger.roar()  # 讓老虎吼叫

# + colab={"base_uri": "https://localhost:8080/"} id="SnLCQPPGtCqS" executionInfo={"status": "ok", "timestamp": 1607842572284, "user_tz": -480, "elapsed": 1020, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="d9b19fcb-40dd-4318-8534-b12b1a4acc61"
tiger.describe()  # 讓老虎跟貓一樣，描述自己的屬性值


# + [markdown] id="Xalywr-NtGVU"
# > 備註：或許在某些教學中，會看到建立親類別時，都會去繼承 `object` 物件：

# + id="ZaBd0wXD6dzo"
class Unknown(object):  # Unknown 繼承 object 類別
    pass


# + [markdown] id="7FKIGRAP7Xxt"
# > 這樣的寫法是基於「Python 裡的所有內容都是一種物件 (`object`)」，所以所有物件都是 `object` 類別的子物件。
# >
# > 但其實不需要特別去繼承 `object` 類別也沒有影響。

# + [markdown] id="z1WB1xyP79_f"
# ## `super()`：調用親類別的內容

# + [markdown] id="_6BFnU7K8HWj"
# 如果在子類別中需要調用親類別的屬性或方法，可以調用 `super()` 函式，來指向親類別物件。
#
# 我們用另一個獅子 Lion 類別來舉例：獅子也是貓科動物，但這次我們需要在建構子當中，額外定義一個 `king` 屬性，來標示這隻獅子是否為獅子王。所以建構子需要被部分改寫：

# + id="q-lXW81A8U0I" executionInfo={"status": "ok", "timestamp": 1607843972433, "user_tz": -480, "elapsed": 945, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
class Lion(Cat):
    def __init__(self, color, height, weight, king):  # 改寫建構子，多傳入一個 king 參數
        super().__init__(color, height, weight)                  # 將 king 以外的參數傳給親類別建構子處理
        self.king = king                              # 在 Lion 類別中自行處理 king 的屬性指定
    
    def roar(self):
        print("Rahhhhhhhhh!")
        return "Rahhhhhhhhh!"


# + id="NG2ISI-y9XfB" executionInfo={"status": "ok", "timestamp": 1607843972962, "user_tz": -480, "elapsed": 731, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}}
lion = Lion(  # 初始化一隻獅子
    color='brown',
    height=200,
    weight=120,
    king=True
)

# + colab={"base_uri": "https://localhost:8080/"} id="sle9CxOh9n-X" executionInfo={"status": "ok", "timestamp": 1607843997346, "user_tz": -480, "elapsed": 735, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="c036b747-7847-486d-ef88-172e2000cdee"
lion.king  # 檢查這隻獅子是不是獅子王

# + id="QWPg0ifs-GNp" executionInfo={"status": "ok", "timestamp": 1607844012363, "user_tz": -480, "elapsed": 702, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="1f4e0276-31d8-464a-ba71-9788f6b00fb2" colab={"base_uri": "https://localhost:8080/"}
lion.describe()  # 讓獅子描述自己的屬性

# + id="kzPi0hPm-J4H"

