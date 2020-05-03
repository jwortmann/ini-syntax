# INI Syntax

[![License](https://img.shields.io/github/license/jwortmann/ini-syntax)](https://github.com/jwortmann/ini-syntax/blob/master/LICENSE)
[![Version](https://img.shields.io/github/v/tag/jwortmann/ini-syntax?label=version)](https://github.com/jwortmann/ini-syntax/tags)
[![GitHub Actions](https://github.com/jwortmann/ini-syntax/workflows/syntax%20tests/badge.svg)](https://github.com/jwortmann/ini-syntax/actions)

A package for [Sublime Text 3](https://www.sublimetext.com/) that provides syntax highlighting for INI files and Windows Registry (.reg) files.

## Installation

1. Run `Package Control: Add Repository` from the command palette and paste `https://raw.githubusercontent.com/jwortmann/ini-syntax/master/packages.json`
2. Run `Package Control: Install Package` and search for `INI Syntax`

## Features

You can navigate between sections in opened INI files via Sublime's `Goto Symbol...` feature from the menu or with the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>R</kbd>.

## Color Schemes

Following the naming conventions for key-value pairs, the scope `meta.mapping.key.ini string.unquoted.ini` is applied for key names in INI files.
If you prefer different highlighting colors for key names and values, ensure to use a color scheme which utilizes a rule for `meta.mapping.key string` or `meta.mapping.value string`, to differentiate between them.
