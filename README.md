# python-games
![GitHub](https://img.shields.io/pypi/v/python-games.svg?label=version&style=flat-square)
![Dowloads](https://img.shields.io/pypi/dm/python-games?color=blue)

## Installing

```
# Linux/macOS
python3 -m pip install -U python-games

# Windows
py -3 -m pip install -U python-games

# Github
pip install git+https://github.com/kevys/python-games.git@main
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
```