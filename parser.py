#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parser module for extracting test cases from markdown files.
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import yaml
from loguru import logger
from markdown_it import MarkdownIt


class TestCaseParser:
    """Parser for extracting test cases from markdown files."""

    def __init__(self, verbose: bool = False):
        """
        Initialize the parser.

        Args:
            verbose: Whether to output detailed error messages and suggestions.
        """
        self.md_parser = MarkdownIt()
        self.verbose = verbose

    def parse_file(self, file_path: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Parse a markdown file and extract test cases.

        Args:
            file_path: Path to the markdown file.

        Returns:
            Dictionary with test case file names as keys and lists of test case dictionaries as values.
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return {}

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.parse_content(content, file_path)

    def parse_content(self, content: str, source_path: str = "") -> Dict[str, List[Dict[str, Any]]]:
        """
        Parse markdown content and extract test cases.

        Args:
            content: Markdown content as string.
            source_path: Source file path (for logging purposes).

        Returns:
            Dictionary with test case file names as keys and lists of test case dictionaries as values.
        """
        test_cases = {}
        
        # Find all "### TestCases ($file_name)" sections
        test_case_sections = re.finditer(
            r'### TestCases\s+\(([^)]+)\)(.*?)(?=###|\Z)', 
            content, 
            re.DOTALL
        )
        
        for match in test_case_sections:
            file_name = match.group(1).strip()
            yaml_content = match.group(2).strip()
            
            try:
                # Try to parse the YAML content
                parsed_test_cases = yaml.safe_load(yaml_content)
                
                if not parsed_test_cases:
                    logger.warning(f"No test cases found in section for {file_name} in {source_path}")
                    continue
                
                # Ensure the result is a list
                if not isinstance(parsed_test_cases, list):
                    if self.verbose:
                        logger.error(f"YAML content in section for {file_name} is not a list. Found type: {type(parsed_test_cases)}")
                        logger.error(f"Content should start with '- ' for each test case item")
                    else:
                        logger.error(f"YAML parse error: Expected list format in section for {file_name}")
                    continue
                
                test_cases[file_name] = parsed_test_cases
                logger.info(f"Successfully parsed {len(parsed_test_cases)} test cases from section for {file_name}")
                
            except yaml.YAMLError as e:
                if self.verbose:
                    logger.error(f"YAML parse error in section for {file_name} in {source_path}: {str(e)}")
                    logger.debug(f"Problematic YAML content:\n{yaml_content}")
                    logger.info("Suggestion: Check for proper indentation and YAML syntax.")
                else:
                    logger.error(f"YAML parse error in section for {file_name}. Use --verbose for details.")
        
        if not test_cases:
            logger.warning(f"No test case sections found in {source_path}")
            
        return test_cases

    def parse_yaml_file(self, file_path: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Parse a YAML file containing test cases directly.

        Args:
            file_path: Path to the YAML file.

        Returns:
            Dictionary with test case file names as keys and lists of test case dictionaries as values.
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return {}

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                
            if not isinstance(content, dict):
                logger.error(f"YAML file {file_path} should contain a dictionary mapping file names to test cases")
                return {}
                
            # Validate the structure
            for file_name, test_cases in content.items():
                if not isinstance(test_cases, list):
                    logger.error(f"Test cases for {file_name} should be a list")
                    continue
                    
            logger.info(f"Successfully parsed YAML file {file_path} with {len(content)} test case sections")
            return content
            
        except yaml.YAMLError as e:
            if self.verbose:
                logger.error(f"YAML parse error in file {file_path}: {str(e)}")
                logger.info("Suggestion: Check for proper indentation and YAML syntax.")
            else:
                logger.error(f"YAML parse error in file {file_path}. Use --verbose for details.")
            return {}
        except Exception as e:
            logger.error(f"Error parsing YAML file {file_path}: {str(e)}")
            return {}
