# Installation Guide

## Prerequisites

- Python 3.12 or higher
- yamllint (for YAML validation)

## Installation from PyPI

The recommended way to install Markdown to Testcase is via pip:

```bash
pip install markdown-to-testcase
```

## Installation from Source

If you want to install from source:

```bash
# Clone the repository
git clone https://github.com/tkykszk/markdown_to_testcase.git
cd markdown_to_testcase

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e .
```

## Binary Installations

### Windows

Download the latest `.exe` file from the [Releases](https://github.com/tkykszk/markdown_to_testcase/releases) page and run it directly.

```powershell
# From the command line
markdown_to_testcase.exe convert -i input_file.md
```

### macOS (Homebrew)

```bash
# Install using Homebrew
brew tap tkykszk/markdown_to_testcase
brew install markdown_to_testcase

# Run the command
markdown_to_testcase convert -i input_file.md
```

### Ubuntu/Debian (apt)

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

## Verifying Installation

To verify that the installation was successful, run:

```bash
markdown_to_testcase --version
```

This should display the version information of the installed package.
