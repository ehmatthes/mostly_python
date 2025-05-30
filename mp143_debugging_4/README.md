# Dice Battle

## Setup

- Download this mini-project by clicking [here](https://github.com/ehmatthes/mostly_python/releases/download/dice_battle_mp143/mp143_debugging_4.zip), or visit [this page](https://github.com/ehmatthes/mostly_python/releases/tag/dice_battle_mp143) and download the file *mp143_debugging_4.zip*.
- Copy the folder 
- `uv venv .venv`
- `uv source .venv/bin/activate`
- `uv pip install -r requirements.in`
- Make an initial commit:
    - `git init`
    - `git add .`
    - `git commit -m "Initial state."`

## Running tests

```sh
$ pytest
========== test session starts ==========
collected 1 item
tests/e2e_tests/test_basic_behavior.py .
========== 1 passed in 0.03s ==========
```

## Running Dice Battle

```sh
$ python dice_battle.py
```

## Practicing debugging

To practice debugging a bug that results in an `AttributeError`, for example:

```sh
$ py-bugger -e AttributeError
Added bug.
All requested bugs inserted.
```

Now when you run dice_battle.py, you should see a traceback:

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
