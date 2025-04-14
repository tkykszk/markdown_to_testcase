# Usage Guide

## Basic Usage

The most basic usage is to convert a Markdown file containing test cases:

```bash
markdown_to_testcase convert -i input_file.md
```

This will:
1. Parse all test cases from the input file
2. Validate YAML syntax using yamllint
3. Create CSV files for each test case section
4. Create a single Excel file with all test cases

## Command-line Options

### Required Options

- `-i, --input`: Input markdown or YAML file path (required)

### Optional Options

- `-o, --output-dir`: Directory to store output files (default: `output`)
- `-F, --force`: Overwrite output files without asking
- `-d, --debug`: Enable debug mode (outputs DEBUG level logs)
- `--verbose`: Show verbose error messages and suggestions for YAML parsing issues
- `--no-yaml-lint`: Skip running yamllint on YAML content (validation is enabled by default)
- `-v, --version`: Display version information

## Working with YAML Input

You can also directly provide a YAML file:

```bash
markdown_to_testcase convert -i testcases.yaml
```

The YAML file should follow this structure:

```yaml
filename1.md:
  - ID: TC001
    Name: Test Case Name
    # ... other fields
  - ID: TC002
    Name: Another Test Case
    # ... other fields

filename2.md:
  - ID: TC101
    Name: Test Case for Another File
    # ... other fields
```

## Output Files

The tool produces the following output:

1. **CSV files**: One CSV file per test case section, named after the filename in the section header.
2. **Excel file**: A single `test_cases.xlsx` file containing all test cases, with each section as a separate sheet.

By default, all output files are stored in the `output` directory. You can change this using the `-o` option.

## Debug and Verbose Mode

For troubleshooting, you can use the debug and verbose options:

```bash
markdown_to_testcase convert -i input_file.md -d --verbose
```

This will show more detailed logs and provide suggestions when YAML parsing fails.
