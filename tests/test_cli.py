#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the CLI module.
"""

import os
import pytest
import tempfile
import sys
from pathlib import Path
from typer.testing import CliRunner

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli import app


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


@pytest.fixture
def sample_markdown():
    """Sample markdown content for testing."""
    return """# Test Document

### TestCases (sample_file.md)
- ID: TC001
  Name: Sample Test Case
  Desc: This is a sample test case
  Test Steps: Steps for test case
  Expected Result: Expected output
  Priority: High

### TestCases (another_file.md)
- ID: TC101
  Name: Test for another file
  Desc: Testing another file
  Test Steps: Steps for another file
  Expected Result: Output for another file
"""


def test_version_command(runner):
    """Test the version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "markdown_to_testcase" in result.stdout


def test_convert_command(runner, sample_markdown):
    """Test the convert command with valid input."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sample markdown file
        md_path = os.path.join(temp_dir, "sample.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(sample_markdown)
        
        # Create output directory
        output_dir = os.path.join(temp_dir, "output")
        
        # Run the convert command
        result = runner.invoke(app, [
            "convert", 
            "-i", md_path, 
            "-o", output_dir, 
            "-F"  # Force overwrite
        ])
        
        assert result.exit_code == 0
        assert "Successfully parsed" in result.stdout
        
        # Check that output files were created
        assert os.path.exists(os.path.join(output_dir, "sample_file.csv"))
        assert os.path.exists(os.path.join(output_dir, "another_file.csv"))
        assert os.path.exists(os.path.join(output_dir, "test_cases.xlsx"))


def test_convert_invalid_file(runner):
    """Test the convert command with a non-existent input file."""
    result = runner.invoke(app, [
        "convert", 
        "-i", "non_existent_file.md",
    ])
    
    assert result.exit_code != 0
    assert "Input file not found" in result.stdout


def test_convert_unsupported_extension(runner):
    """Test the convert command with an unsupported file extension."""
    with tempfile.NamedTemporaryFile(suffix=".txt") as temp_file:
        result = runner.invoke(app, [
            "convert", 
            "-i", temp_file.name,
        ])
        
        assert result.exit_code != 0
        assert "Unsupported file extension" in result.stdout


def test_convert_debug_mode(runner, sample_markdown):
    """Test the convert command with debug mode enabled."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sample markdown file
        md_path = os.path.join(temp_dir, "sample.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(sample_markdown)
        
        # Run the convert command with debug mode
        result = runner.invoke(app, [
            "convert", 
            "-i", md_path, 
            "-d",  # Debug mode
            "-F"   # Force overwrite
        ])
        
        assert result.exit_code == 0
        # In debug mode, more verbose output should be present
        assert "Processing file" in result.stdout
