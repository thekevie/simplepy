# python-games
![GitHub](https://img.shields.io/pypi/v/python-games.svg?label=version&style=flat-square)

A python package that can do math and have games. This was made as my school project.

## Installing

```
# Linux/macOS
python3 -m pip install -U python-easy

# Windows
py -3 -m pip install -U python-easy

# Github
pip install git+https://github.com/kevys/python-easy.git@main
```

## Quick Example

```
import games

c = input("Choose rock, paper or scissor > ")

output = games.rps(c)

if output[2] is False:
    print(f'Loser, You picked {output[0]}, AI picked {output[1]}')
elif output[2] is True:
    print(f'Winner, You picked {output[0]}, AI picked {output[1]}')
elif output[2] == None:
    print(f"{output[1]}, {output[0]}")
```
