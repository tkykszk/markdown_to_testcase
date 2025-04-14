# Markdown to Testcase

![image](https://raw.githubusercontent.com/tkykszk/markdown_to_testcase/alpharel/docs/images/markdown2testcase.png)

A Python tool to extract test cases from Markdown files and convert them to CSV and Excel formats.

## Features

- Parse test cases from Markdown headings in the format `### TestCases (filename)`
- Support for direct YAML input files
- Generate CSV output files (one per test case section)
- Compile all test cases into a single Excel file with multiple sheets
- Detailed error reporting and suggestions for YAML parsing issues
- Colorized console output using loguru

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/tkykszk/markdown_to_testcase.git
cd markdown_to_testcase

# Install dependencies
pip install -r requirements.txt
```

### Binary Installations

#### Windows

Download the latest `.exe` file from the [Releases](https://github.com/tkykszk/markdown_to_testcase/releases) page and run it directly.

```powershell
# From the command line
markdown_to_testcase.exe convert -i input_file.md
```

#### macOS (Homebrew)

```bash
# Install using Homebrew
brew tap tkykszk/markdown_to_testcase
brew install markdown_to_testcase

# Run the command
markdown_to_testcase convert -i input_file.md
```

#### Ubuntu/Debian (apt)

```bash
# Add the repository
curl -s https://tkykszk.github.io/markdown_to_testcase/apt/KEY.gpg | sudo apt-key add -
echo "deb https://tkykszk.github.io/markdown_to_testcase/apt ./" | sudo tee /etc/apt/sources.list.d/markdown_to_testcase.list

# Update package list and install
sudo apt update
sudo apt install markdown-to-testcase

# Run the command
markdown_to_testcase convert -i input_file.md
```

## Usage

Basic usage:

```bash
python main.py convert -i input_file.md
```

All available options:

```bash
python main.py convert -i input_file.md -o output_dir -F --verbose
```

### Command-line Options

- `-i, --input`: Input markdown or YAML file path (required)
- `-o, --output-dir`: Directory to store output files (default: `output`)
- `-F, --force`: Overwrite output files without asking
- `-d, --debug`: Enable debug mode (outputs DEBUG level logs)
- `--verbose`: Show verbose error messages and suggestions for YAML parsing issues
- `--no-yaml-lint`: Skip running yamllint on YAML content (validation is enabled by default)
- `-v, --version`: Display version information

## Input Format

### Markdown Format

The tool looks for sections in Markdown files that match the following format:

```markdown
### TestCases (filename)
- ID: TC001
  Name: Test Case Name
  Desc: Test case description
  Pre-conditions: Required preconditions
  Test Steps: Steps to execute the test
  Expected Result: Expected outcome
  Actual Result: Actual outcome (recorded after testing)
  Test Data: Test data to use
  Priority: High/Medium/Low
  Severity: High/Medium/Low
  Status: Not executed/Passed/Failed
  Environment: Test environment information
  Tested By: Tester name
  Date: Test date
  Comments/Notes: Additional notes
```

Multiple test cases can be included in a single section, and multiple sections can be included in a single file.

### YAML Format

The tool also supports direct YAML input files with the following format:

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

## Output

- CSV files will be created in the specified output directory (default: `output`), one per test case section.
- An Excel file named `test_cases.xlsx` will be created in the output directory, with one sheet per test case section.

## Development

### Requirements

- Python 3.12+
- yamllint (required for YAML validation)
- Dependencies listed in `requirements.txt`

### Testing

```bash
pytest
```

### Code Formatting

```bash
black .
flake8
```

## Building from Source

### Building Windows Executable

```bash
# Install PyInstaller if not already installed
pip install pyinstaller

# Build the executable
pyinstaller --onefile --name markdown_to_testcase main.py

# The executable will be in the dist/ directory
```

### Packaging for macOS (Homebrew)

1. Create a Homebrew formula in a new repository named `homebrew-markdown_to_testcase`:

```ruby
# markdown_to_testcase.rb
class MarkdownToTestcase < Formula
  desc "A tool to extract test cases from Markdown files"
  homepage "https://github.com/tkykszk/markdown_to_testcase"
  url "https://github.com/tkykszk/markdown_to_testcase/archive/refs/tags/v[VERSION].tar.gz"
  sha256 "[SHA256]"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/markdown_to_testcase", "--version"
  end
end
```

1. Users can then install with `brew tap` and `brew install` as shown in the Installation section.

### Packaging for Ubuntu/Debian (apt)

1. Create a `debian` directory with the necessary files:

```bash
mkdir -p debian/source
```

1. Create the required configuration files (control, rules, changelog, etc)

1. Build the Debian package:

```bash
dpkg-buildpackage -us -uc
```

1. Host the package in a repository accessible via apt (e.g., GitHub Pages)

## License

MIT
