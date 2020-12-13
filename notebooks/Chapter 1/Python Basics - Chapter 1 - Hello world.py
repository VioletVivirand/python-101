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

# + [markdown] id="OIKHAVkDYzwU"
# # Chapter 1 - Hello world!

# + [markdown] id="kyBjg1jRm_u0"
# 這是 Python 課程的起跑點。在筆者的經驗裡，幾乎學習所有程式語言的第一堂，老師都會先讓學生可以在螢幕上顯示出 "Hello world!" 的字樣。沒錯，就是這麼簡單，經過簡單的步驟，我們開始可以讓電腦幫我們做事情了！

# + [markdown] id="EygpPERTjxzz"
# ## 基本操作

# + [markdown] id="5ML6BoC_1R2I"
# 在資料科學領域的專案裡，通常會選用互動式編輯器，以快速執行程式碼及實驗。以下將列出本次教學課程建議使用的編輯器：
#
# * [Jupyter Notebook, Jupyter Lab](https://jupyter.org)：最盛行的互動式編輯器，可以透過 Python 套件管理器安裝，或透過[安裝 Anaconda indivisual edition](https://www.anaconda.com/products/individual) 以取得
# * [Google Colab](https://colab.research.google.com/)：由 Google 提供之免費的線上 Jupyter 運算環境，有時間限制，可選用 GPU 及 TPU
#
# 請各位先熟悉以下的常用操作。在此列出較常使用的部分鍵盤操作說明： 

# + [markdown] id="rcr1BbRJOvZ3"
# ### Jupyter Notebook, Jupyter Lab

# + [markdown] id="Jm7QuOy9OyoJ"
# * 在 Cell 上輸入 <button>Enter</button> (Windows) / <button>Return</button>：進入編輯模式 (Edit mode)
# * 在編輯模式內輸入 <button>Esc</button>：返回命令模式 (Command mode)
# * 在命令模式中：
#    * 輸入 <button>a</button>：在此 Cell 上方新增一個 Cell
#    * 輸入 <button>b</button>：在此 Cell 下方新增一個 Cell
#    * 輸入 <button>dd</button>：刪除此 Cell
#    * 輸入 <button>z</button>：將被刪除的 Cell 給復原
#    * 輸入 <button>m</button>：將此 Cell 轉換為 Markdown 格式之文件
#    * 輸入 <button>y</button>：將此 Cell 轉換為程式碼

# + [markdown] id="aYOCUb5HP4EW"
# ### Google Colab

# + [markdown] id="dWKoSrbhQAbX"
# * 在 Cell 上輸入 <button>Enter</button> (Windows) / <button>Return</button>：進入編輯模式 (Edit mode)
# * 在編輯模式內輸入 <button>Esc</button>：返回命令模式 (Command mode)
# * 在命令模式中：
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>a</button>：在此 Cell 上方新增一個 Cell
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>b</button>：在此 Cell 下方新增一個 Cell
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>d</button>：刪除此 Cell
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>z</button>：將被刪除的 Cell 給復原
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>m</button>：將此 Cell 轉換為 Markdown 格式之文件
#    * 輸入 <button>Ctrl + m</button> (Windows) / <button>Command ⌘ + m</button> (MacOS) + <button>y</button>：將此 Cell 轉換為程式碼

# + [markdown] id="NqueSBrN-HaW"
# ## 程式碼專案儲存庫位址
#

# + [markdown] id="QPT0Lj0z-Qxk"
# 本次的教學內容並無機密性，將於 GitHub 向全世界公開，歡迎各位在授權條款的規範下自由使用。

# + [markdown] id="sEMZX9rGm5Or"
# > [TODO] Add resources, repos, and links

# + [markdown] id="5IQI-OCPThFw"
# ## Console I/O - Hello world!

# + [markdown] id="LczgYatKAUmA"
# 透過呼叫 `print()` 函式，可以讓指定的內容作為執行的結果顯示於畫面上。

# + [markdown] id="_kUO5Y21CtJO"
# > 備註：或許有些讀者會發現，某些內容即使不呼叫 `print()` 函式，也可以正常顯示出來，這是因為我們使用互動式的編輯器來檢視結果。未來各位的程式可能不一定是使用 Jupyter Notebook 來執行，如果需要顯示訊息於畫面，務必呼叫 `print()` 函式。

# + id="2aogtz_hUPJn" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1604645435399, "user_tz": -480, "elapsed": 1074, "user": {"displayName": "\u9ec3\u7a2e\u5e73", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjCoYcYDAMAK-J-MvClxwWJY0fvKYsny6BL962ZNA=s64", "userId": "12486487678081777487"}} outputId="5db79497-961e-4c21-f943-d6ab2c06efb6"
print('Hello world!')

# + [markdown] id="ViORNJguuYg7"
# ## Comment：註解

# + id="ukRg1Icpud5T"
# 這就是註解，經過註解後的內容將不會被執行
# 註解以 "#"（井字號）作為開頭，後方的所有文字皆會被視為註解

# + [markdown] id="LH_wtT2HBHMS"
# > 備註：很多編輯器的「註解」動作都有相似的快捷鍵，在 Windows 上可能是 <button>Ctrl</button> + <button>/</button>，MacOS 上則是 <button>Command ⌘</button> + <button>/</button>。
# >
# > 由於操作頻繁，很常會使用，而且透過快捷鍵不只比較快速，更可以一次性的將多行文字轉換為註解。不妨試試看？

# + [markdown] id="3YgbYtkkjzhb"
# ## 展望未來

# + [markdown] id="03Shi7AVDKWQ"
# 雖然本課程只會介紹 Python 的基礎內容，但是不管多大的專案，都是從無到有、一行一行程式碼堆砌起來的心血結晶。在底下提供一些相當好用的專案，給各位一個夢想，期待未來大家可以應用 Python 到自己的日常生活中！

# + [markdown] id="Rez9gEe1j5R-"
# * [youtube-dl](https://github.com/ytdl-org/youtube-dl/)：線上媒體串流服務的命令列 (Command line interface, CLI) 下載工具
# * [thef*ck](https://github.com/nvbn/thefuck)：自動修正錯誤終端機的指令
# * [python - GitHub topics](https://github.com/topics/python)：GitHub 中受矚目的 Python 相關專案集合

# + id="p3OSHPgqEREC"

