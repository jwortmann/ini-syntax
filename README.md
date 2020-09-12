# INI Syntax

[![License](https://img.shields.io/github/license/jwortmann/ini-syntax)](https://github.com/jwortmann/ini-syntax/blob/master/LICENSE)
[![Version](https://img.shields.io/github/v/tag/jwortmann/ini-syntax?label=version)](https://github.com/jwortmann/ini-syntax/tags)
[![GitHub Actions](https://github.com/jwortmann/ini-syntax/workflows/syntax%20test/badge.svg)](https://github.com/jwortmann/ini-syntax/actions)

A package for [Sublime Text](https://www.sublimetext.com/) that provides syntax highlighting for INI and related file types like Windows Registry (.reg) files.

## Installation

The package can be installed via Sublime Text's package manager [Package Control](https://packagecontrol.io/installation).
From the command palette choose `Package Control: Install Package` and search for `INI`.

## Features

You can navigate between sections in opened INI files via Sublime's `Goto Symbol...` feature from the menu or with the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>R</kbd>.

## Color Schemes

Following the naming conventions for key-value pairs, the scopes `meta.mapping.key.ini string` and `meta.mapping.value.ini string` are applied for keys and string values respectively.
If you prefer different highlighting colors for key names and values, ensure to use a color scheme which targets one of these scopes to distinguish between them.
You can easily add such a rule as a customization to your color scheme, as described in the [official documentation](https://www.sublimetext.com/docs/color_schemes.html#customization).
For example, if you want keys to be highlighted with the same color as keywords in *Mariana*, create a file `Mariana.sublime-color-scheme` in your Packages/User directory with the following content:
```json
{
    "rules": [
        {
            "scope": "meta.mapping.key.ini string",
            "foreground": "var(pink)"
        }
    ]
}
```
