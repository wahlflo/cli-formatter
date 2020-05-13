# cli-formatter

cli-formatter is a python3 utility for formatting console output for cli scripts.

## Current Features

* Colored output
* Ability to control the verbosity level
* Two table factories for ASCII tables

## Installation

Install the package with pip

    pip3 install cli-formatter


## Examples

### Example 1

```python
from cli_formatter.output_formatting import info, warning, set_verbosity_level

set_verbosity_level(level=3)

info(message='This is a Info message')
info(message='This is a Info message with very low verbosity level', verbosity_level=1)
warning(message='This is a warning')
```

```
[+] This is a Info message
[!] This is a warning
```


### Example 2

```python
from cli_formatter.table_builder import TableBuilderClassic, TableBuilderAlternative

header=['Column 1', 'Column 2', 'Column 3']
data=[
    ['This is a test', '123', 'abc'],
    ['cli-formatter', 'is', 'awesome']
]

print('classic design:')
classic_builder = TableBuilderClassic()
classic_builder.build_table(header=header, data=data)

print('\nalterative design:')
alternative_builder = TableBuilderAlternative()
alternative_builder.build_table(header=header, data=data)
```

```
classic design:
+----------------+----------+----------+
| Column 1       | Column 2 | Column 3 |
+----------------+----------+----------+
| This is a test | 123      | abc      |
| cli-formatter  | is       | awesome  |
+----------------+----------+----------+

alterative design:
 Column 1       | Column 2 | Column 3
--------------------------------------
 This is a test | 123      | abc
 cli-formatter  | is       | awesome
```