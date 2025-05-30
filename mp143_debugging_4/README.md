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

You should also see a failure if you run the tests after running py-bugger:

```sh
(.venv) $ pytest
============ test session starts =============
...
tests/e2e_tests/test_basic_behavior.py F     [100%]

================== FAILURES ==================
__________________ test_basic_behavior __________________

>   ???
E   AssertionError: assert '' == '\nPlayer A: ...lling dice.\n'
E     
E     - 
E     - Player A: 5
E     ...Full output truncated (42 lines hidden), use '-vv' to show

tests/e2e_tests/test_basic_behavior.py:29: AssertionError
__________________ Captured stdout call __________________
Traceback (most recent call last):
  File "/.../dice_battle.py", line 7, in <module>
    import utils
  File "/.../utils.py", line 3, in <module>
    from die import Die
  File "/.../die.py", line 7, in <module>
    if seed := os.ienviron.get("DICE_BATTLE_RANDOM_SEED"):
               ^^^^^^^^^^^
AttributeError: module 'os' has no attribute 'ienviron'. Did you mean: 'environ'?

========== short test summary info ===========
FAILED tests/e2e_tests/test_basic_behavior.py::test_basic_behavior -
    AssertionError: assert '' == '\nPlayer A: ...lling dice.\n'
============= 1 failed in 0.04s ==========
```

Note the `AttributeError` just before the test summary, showing that the test failed because of the bug introduced by py-bugger.
