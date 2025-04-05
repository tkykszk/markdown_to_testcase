#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Command-line interface for the markdown_to_testcase tool.
"""

import os
import sys
import typer
from typing import Optional
from pathlib import Path
from loguru import logger

from parser import TestCaseParser
from converter import TestCaseConverter

app = typer.Typer(help="Tool to convert markdown test cases to CSV and Excel formats")


def configure_logger(debug: bool):
    """Configure the logger based on debug flag."""
    logger.remove()  # Remove default handler
    log_level = "DEBUG" if debug else "INFO"
    logger.add(sys.stderr, level=log_level, colorize=True)


@app.command()
def convert(
    input_file: str = typer.Option(
        ..., "--input", "-i", help="Input markdown or YAML file path"
    ),
    force: bool = typer.Option(
        False, "--force", "-F", help="Overwrite output files without asking"
    ),
    output_dir: str = typer.Option(
        "output", "--output-dir", "-o", help="Directory to store output files"
    ),
    debug: bool = typer.Option(
        False, "--debug", "-d", help="Enable debug mode"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", help="Show verbose error messages and suggestions"
    ),
):
    """Convert test cases from markdown/YAML to CSV and Excel formats."""
    configure_logger(debug)
    
    logger.info(f"Processing file: {input_file}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        raise typer.Exit(code=1)
    
    # Initialize parser and converter
    parser = TestCaseParser(verbose=verbose)
    converter = TestCaseConverter(output_dir=output_dir)
    
    # Parse test cases
    file_extension = Path(input_file).suffix.lower()
    if file_extension in ['.md', '.markdown']:
        test_cases = parser.parse_file(input_file)
    elif file_extension in ['.yaml', '.yml']:
        test_cases = parser.parse_yaml_file(input_file)
    else:
        logger.error(f"Unsupported file extension: {file_extension}. Use .md, .markdown, .yaml, or .yml")
        raise typer.Exit(code=1)
    
    if not test_cases:
        logger.error("No valid test cases found")
        raise typer.Exit(code=1)
    
    # Convert to CSV files
    csv_files = converter.convert_to_csv(test_cases, force=force)
    if not csv_files:
        logger.warning("No CSV files created")
    
    # Convert to Excel file
    excel_file = converter.convert_to_excel(test_cases, force=force)
    
    logger.info("Conversion completed")


@app.command()
def version():
    """Display the version information."""
    print("markdown_to_testcase v0.1.0")


if __name__ == "__main__":
    app()
