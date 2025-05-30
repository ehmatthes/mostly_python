# Dice Battle

## Setup

- Download this mini-project by clicking [here](https://github.com/ehmatthes/mostly_python/releases/download/dice_battle_mp143/dice_battle_mp143.zip), or visit [this page](https://github.com/ehmatthes/mostly_python/releases/tag/dice_battle_mp143) and download the file `dice\_battle\_mp143.zip`.
- Copy the folder `dice_battle_mp143/` from your Downloads folder to wherever you like to store your Python programs.
- Run the following commands to set up an environment for this project:

```sh
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.in
(.venv)$ git init
(.venv)$ git add .
(.venv)$ git commit -m "Initial state."
```

## Running Dice Battle

```sh
(.venv)$ python dice_battle.py
Player A: 1
Player B: 4
Player B won!
...

Player A: 6
Player B: 1
Player A won!

Summary:
  Player A won 6 battles.
  Player B won 3 battles.
  There were 1 tied battles.

Clearly, player A is better at rolling dice.
```

## Running tests

```sh
(.venv)$ pytest
========== test session starts ==========
collected 1 item
tests/e2e_tests/test_basic_behavior.py .
========== 1 passed in 0.03s ==========
```

## Practicing debugging

To practice debugging a bug that results in an `AttributeError`, for example:

```sh
$ py-bugger -e AttributeError
Added bug.
All requested bugs inserted.
```

Now when you run `dice_battle.py`, you should see a traceback:

```sh
$ python dice_battle.py 
Traceback (most recent call last):
  File " dice_battle.py", line 7, in <module>
    import utils
  File "utils.py", line 3, in <module>
    from die import Die
  File "die.py", line 7, in <module>
    if seed := os.envidron.get("DICE_BATTLE_RANDOM_SEED"):
               ^^^^^^^^^^^
AttributeError: module 'os' has no attribute 'envidron'. Did you mean: 'environ'?
```
