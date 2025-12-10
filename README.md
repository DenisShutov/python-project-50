[![Actions Status](https://github.com/DenisShutov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisShutov/python-project-50/actions)
[![Python CI](https://github.com/DenisShutov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/DenisShutov/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DenisShutov_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DenisShutov_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DenisShutov_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DenisShutov_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DenisShutov_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DenisShutov_python-project-50)

# Gendiff
A program that finds differences between two files.

### Supported Formats:

Input: JSON, YAML/YML
Output: stylish, plain, JSON

### Options:

-f, --format FORMAT - output format (stylish, plain, json), default: stylish
-h, --help - show help message


### Setup
```bash
make install
```

### Demo:
#### Compare JSON Files
<a href="https://asciinema.org/a/gdQnnEjAbQ48BRasIrBXaEfRc" target="_blank"><img src="https://asciinema.org/a/gdQnnEjAbQ48BRasIrBXaEfRc.svg" width="600"/></a>

#### Compare YAML Files
<a href="https://asciinema.org/a/1EX2V5CH7G0RdiWuyRxSTGlsa?t=30" target="_blank"><img src="https://asciinema.org/a/1EX2V5CH7G0RdiWuyRxSTGlsa.svg" width="600"/></a>

#### Compare Files with Nested Structuresы
<a href="https://asciinema.org/a/e1QGGu3KEya5SjjzQIHx1bdBi?t=30" target="_blank"><img src="https://asciinema.org/a/e1QGGu3KEya5SjjzQIHx1bdBi.svg" width="600"/></a>

#### Using "plain" Formatter
<a href="https://asciinema.org/a/0wwgFTbgPZLvuEW0dPw0LKb1c?t=40" target="_blank"><img src="https://asciinema.org/a/0wwgFTbgPZLvuEW0dPw0LKb1c.svg" width="600" /></a>

#### Using "json" Formatter
<a href="https://asciinema.org/a/1oinMaixNDVsZ1fs8YwftIfZy?t=45" target="_blank"><img src="https://asciinema.org/a/1oinMaixNDVsZ1fs8YwftIfZy.svg" width="600"/></a>