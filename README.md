# INI Syntax

[![License](https://img.shields.io/github/license/jwortmann/ini-syntax)](https://github.com/jwortmann/ini-syntax/blob/master/LICENSE)
[![Version](https://img.shields.io/github/v/tag/jwortmann/ini-syntax?label=version)](https://github.com/jwortmann/ini-syntax/tags)
[![GitHub Actions](https://github.com/jwortmann/ini-syntax/workflows/syntax%20test/badge.svg)](https://github.com/jwortmann/ini-syntax/actions)

A package for [Sublime Text](https://www.sublimetext.com/) that provides syntax highlighting for INI and related file types like Windows Registry (.reg) files.

## Installation

The package can be installed via Sublime Text's package manager [Package Control](https://packagecontrol.io/installation).
From the command palette choose *Package Control: Install Package* and search for *INI*.

## Customization

### Comment toggling

The default character for the "toggle comment" functionality (<kbd>Ctrl</kbd>+<kbd>/</kbd> on Windows/Linux or <kbd>⌘</kbd>+<kbd>/</kbd> on macOS) in INI files is a semicolon.
It can be changed to `#` by adding a custom key binding with a `"variant": 2` argument for the `toggle_comment` command (this requires Sublime Text build 4130 or later):
```jsonc
{
    "keys": ["ctrl+/"],  // or ["super+forward_slash"] on macOS
    "command": "toggle_comment",
    "args": {"block": false, "variant": 2},
    "context": [{"key": "selector", "operand": "source.ini"}]
},
```
