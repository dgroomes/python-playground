# python-playground

📚 Learning and exploring the Python programming language.

> Python is a programming language that lets you work quickly and integrate systems more effectively.
>
> --<cite> https://www.python.org/ </cite>


## Overview

This repository is for me to learn and explore Python at my own pace and through subjects that interest me. This
repository will contain executable code that will help me in the future when I want to review and quickly re-learn
subjects I've already covered.

**NOTE**: This project was developed on macOS. It is for my own personal use.


## Instructions

Follow these instructions to run the demo programs.

1. Use Python 3.11
   * Alternatively, develop this project in a [*Dev Container*](https://containers.dev/) defined in
   `.devcontainer/devcontainer.json`. The dev container is pre-installed with the required Python version.
2. Run the "Hello World" program
   * ```shell
     python3 hello.py
     ```  
   * I'm using the `python3` name here instead of `python` because it's such a common convention. While you can get away
   with using the straight name `python` on some systems because that points to a Python 3 installation, that's not a safe
   assumption on other systems where `python` may point to a Python 2 installation.
   * Altogether, it should something like this:
     ```shell
     $ python3 hello.py
     Hi there, from a Python program!
     ``` 
3. Run the "read a JSON file" program
   * ```shell
     python3 read_json.py
     ```


## Wish List

General TODOs and things I wish to implement in this project.

* [x] DONE Dev Container
* [ ] Figure out the right package manager. And wire in some basic utility library (although Pyhton is very cool that it
  has the basics like JSON and CSV support in the standard library already).
* [ ] REPL example and instructions
* [ ] Showcase type hints
* [ ] What does modularization look like in Python? Is there a module system, or conventions?
* [x] DONE Read from a JSON file.


## Reference

* [python.org: *What’s New In Python 3.11*](https://docs.python.org/3/whatsnew/3.11.html)
