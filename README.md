# Blackened Pygments Style
A black-and-white pygments style based originally on the `emacs` and `bw` styles and intended for use with the LaTeX package `minted`.
It is improved in comparison to the built-in `bw` style in that some further keywords are now bold, as well as some other changes that seem reasonable.

Wherever I have not yet seen part of the style used, the default colouring has been kept.
When you find code that results in coloured parts – especially when using `minted` –, please open an issue and I'll have a look at it.

## Installation
On Linux, execute:
```
sudo python setup.py install
```
On Windows, this should work similarly (without `sudo`) when executed in a command line with administratorial rights.

## Acknowledgments
* This style had originally been based on the default `emacs` style, though it currently bears little resemblance to it.
* Some elements have been taken from the `bw` style.
* https://github.com/huesersohn/pygments-mastersthesis has been used as a basis for the build files.
