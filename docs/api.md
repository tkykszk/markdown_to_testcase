# API Reference

This document provides details about the API of the markdown_to_testcase package.

## TestCaseParser

The `TestCaseParser` class is responsible for parsing markdown files and extracting test cases.

```python
from markdown_to_testcase.parser import TestCaseParser

parser = TestCaseParser(verbose=True)
test_cases = parser.parse_file("path/to/markdown_file.md")
```

::: markdown_to_testcase.parser.TestCaseParser
    options:
      show_root_heading: true
      show_source: true

## TestCaseConverter

The `TestCaseConverter` class converts test cases to CSV and Excel formats.

```python
from markdown_to_testcase.converter import TestCaseConverter

converter = TestCaseConverter(output_dir="output")
csv_files = converter.convert_to_csv(test_cases)
excel_file = converter.convert_to_excel(test_cases)
```

::: markdown_to_testcase.converter.TestCaseConverter
    options:
      show_root_heading: true
      show_source: true
