# Contributing

Thank you for considering contributing to markdown_to_testcase! This document provides guidelines for contributing to this project.

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/markdown_to_testcase.git`
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Testing

Tests are written using pytest. Run the test suite with:

```bash
pytest
```

## Code Style

This project follows PEP 8 style guidelines with a line length of 150 characters.

We use the following tools for code quality:
- black for code formatting
- flake8 for linting
- pytest for testing

Before submitting a pull request, please make sure your code passes all tests and style checks:

```bash
# Run black formatter
black --line-length 150 .

# Run linter
flake8 --max-line-length=150 .

# Run tests
pytest
```

## Pull Request Process

1. Create a branch with a descriptive name related to your changes
2. Make your changes and commit them with descriptive commit messages
3. Push your branch and create a pull request
4. Wait for review and make any requested changes

## Release Process

The maintainers will handle the release process, which includes:

1. Updating the version number in the appropriate files
2. Creating a new tag
3. Building and uploading to PyPI
4. Creating a GitHub release with binaries for different platforms
