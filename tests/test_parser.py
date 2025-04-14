#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the TestCaseParser class.
"""

import os
import pytest
from pathlib import Path
import tempfile

from markdown_to_testcase.parser import TestCaseParser


@pytest.fixture
def parser():
    """Create a TestCaseParser instance."""
    return TestCaseParser(verbose=True)


@pytest.fixture
def sample_markdown():
    """Sample markdown content for testing."""
    return """# Test Document

This is a sample document with test cases.

### TestCases (sample_file.md)
- ID: TC001
  Name: Sample Test Case
  Desc: This is a sample test case
  Test Steps: |
    1. Step one
    2. Step two
  Expected Result: Expected output
  Priority: High

- ID: TC002
  Name: Another Test Case
  Desc: This is another test case
  Test Steps: Do something
  Expected Result: Another expected output
  Priority: Medium

### TestCases (another_file.md)
- ID: TC101
  Name: Test for another file
  Desc: Testing another file
  Test Steps: Steps for another file
  Expected Result: Output for another file
"""


@pytest.fixture
def sample_yaml():
    """Sample YAML content for testing."""
    return """sample_file.md:
  - ID: TC001
    Name: Sample Test Case
    Desc: This is a sample test case
    Test Steps: |
      1. Step one
      2. Step two
    Expected Result: Expected output
    Priority: High
  - ID: TC002
    Name: Another Test Case
    Desc: This is another test case
    Test Steps: Do something
    Expected Result: Another expected output
    Priority: Medium

another_file.md:
  - ID: TC101
    Name: Test for another file
    Desc: Testing another file
    Test Steps: Steps for another file
    Expected Result: Output for another file
"""


def test_parse_content(parser, sample_markdown):
    """Test parsing markdown content."""
    result = parser.parse_content(sample_markdown, "test_source.md")
    
    assert len(result) == 2
    assert "sample_file.md" in result
    assert "another_file.md" in result
    
    assert len(result["sample_file.md"]) == 2
    assert len(result["another_file.md"]) == 1
    
    assert result["sample_file.md"][0]["ID"] == "TC001"
    assert result["sample_file.md"][1]["ID"] == "TC002"
    assert result["another_file.md"][0]["ID"] == "TC101"


def test_parse_file(parser, sample_markdown):
    """Test parsing a markdown file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as temp_file:
        temp_file.write(sample_markdown)
        temp_path = temp_file.name
    
    try:
        result = parser.parse_file(temp_path)
        
        assert len(result) == 2
        assert "sample_file.md" in result
        assert "another_file.md" in result
        
        assert len(result["sample_file.md"]) == 2
        assert len(result["another_file.md"]) == 1
    finally:
        os.unlink(temp_path)


def test_parse_yaml_file(parser, sample_yaml):
    """Test parsing a YAML file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as temp_file:
        temp_file.write(sample_yaml)
        temp_path = temp_file.name
    
    try:
        result = parser.parse_yaml_file(temp_path)
        
        assert len(result) == 2
        assert "sample_file.md" in result
        assert "another_file.md" in result
        
        assert len(result["sample_file.md"]) == 2
        assert len(result["another_file.md"]) == 1
        
        assert result["sample_file.md"][0]["ID"] == "TC001"
        assert result["sample_file.md"][1]["ID"] == "TC002"
        assert result["another_file.md"][0]["ID"] == "TC101"
    finally:
        os.unlink(temp_path)


def test_parse_invalid_yaml(parser):
    """Test parsing invalid YAML content."""
    invalid_markdown = """### TestCases (invalid.md)
- ID: TC001
  Name: Invalid YAML
  Desc: This contains invalid YAML
  Test Steps: 
  - This is incorrect indentation
    Expected Result: This won't parse correctly
"""
    
    result = parser.parse_content(invalid_markdown, "invalid_source.md")
    assert len(result) == 0  # Should fail to parse


def test_parse_empty_section(parser):
    """Test parsing an empty test case section."""
    empty_section = """### TestCases (empty.md)
"""
    
    result = parser.parse_content(empty_section, "empty_source.md")
    assert len(result) == 0  # No test cases to parse


def test_parse_non_existent_file(parser):
    """Test parsing a non-existent file."""
    result = parser.parse_file("non_existent_file.md")
    assert result == {}
