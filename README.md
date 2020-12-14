# Python 101 Tutorial

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/violetvivirand/python-101)

Python lectures for begineers

## Chapters

| Chapter # | Title                                       | Notebook                                                                                                                                                             |                                                                                                                           Google Colab                                                                                                                           |
|-----------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 1         | Hello world!                                | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%201/Python%20Basics%20-%20Chapter%201%20-%20Hello%20world.ipynb)                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%201/Python%20Basics%20-%20Chapter%201%20-%20Hello%20world.ipynb)                     |
| 2         | Datatypes and Operators：資料型態與運算子   | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%202/Python%20Basics%20-%20Chapter%202%20-%20Datatypes%20and%20Operators.ipynb)       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%202/Python%20Basics%20-%20Chapter%202%20-%20Datatypes%20and%20Operators.ipynb)       |
| 3         | Methods and Functions：方法與函式           | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%203/Python%20Basics%20-%20Chapter%203%20-%20Methods%20and%20Functions.ipynb)         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%203/Python%20Basics%20-%20Chapter%203%20-%20Methods%20and%20Functions.ipynb)         |
| 4         | Collections：集合物件                       | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%204/Python%20Basics%20-%20Chapter%204%20-%20Collections.ipynb)                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%204/Python%20Basics%20-%20Chapter%204%20-%20Collections.ipynb)                       |
| 5         | Control flows and Iterables：流程控制與疊代 | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%205/Python%20Basics%20-%20Chapter%205%20-%20Control%20flows%20and%20Iterables.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%205/Python%20Basics%20-%20Chapter%205%20-%20Control%20flows%20and%20Iterables.ipynb) |
| 6         | Functions：函式                             | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%206/Python%20Basics%20-%20Chapter%206%20-%20Functions.ipynb)                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%206/Python%20Basics%20-%20Chapter%206%20-%20Functions.ipynb)                         |
| 7         | Classes：類別                               | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%207/Python%20Basics%20-%20Chapter%207%20-%20Classes.ipynb)                           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%207/Python%20Basics%20-%20Chapter%207%20-%20Classes.ipynb)                           |
| 8         | Miscellaneous：其餘補充說明                 | [Link](https://github.com/VioletVivirand/python-101/blob/main/notebooks/Chapter%208/Python%20Basics%20-%20Chapter%208%20-%20Miscellaneous.ipynb)                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VioletVivirand/python-101/blob/main/notebooks/Chapter%208/Python%20Basics%20-%20Chapter%208%20-%20Miscellaneous.ipynb)                     |

## Contributing

Lock dependencies before submit changes:

```bash
# Freeze into requirements.txt with Poetry
poetry export -f requirements.txt --output requirements.txt

# Use dephell to convert between different formats
# Convert from Poetry (pyproject.toml) to Pipfile
dephell deps convert --from-format=poetry --from-path=pyproject.toml  --to-format=pipfile --to-path=Pipfile
# Convert from Poetry Lock (poetry.lock) to Pipfile.lock
dephell deps convert --from-format=poetrylock --from-path=poetry.lock  --to-format=pipfilelock --to-path=Pipfile.lock
```

## License

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text"><a rel="cc:attributionURL" property="dct:title" href="https://github.com/VioletVivirand/python-101">Python-101</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/VioletVivirand">Violet Vivirand</a> is licensed under <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a></p>
