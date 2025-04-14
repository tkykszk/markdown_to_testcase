#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parser module for extracting test cases from markdown files.
"""

import re
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import yaml
from loguru import logger
from markdown_it import MarkdownIt


class TestCaseParser:
    """Parser for extracting test cases from markdown files."""

    def __init__(self, verbose: bool = False, check_yaml_lint: bool = False):
        """
        Initialize the parser.

        Args:
            verbose: Whether to output detailed error messages and suggestions.
            check_yaml_lint: Whether to run yamllint on YAML content before parsing.
        """
        self.md_parser = MarkdownIt()
        self.verbose = verbose
        self.check_yaml_lint = check_yaml_lint

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

    def run_yamllint(self, yaml_content: str, file_name: str, source_path: str) -> List[str]:
        """
        Run yamllint on the YAML content and return any errors.
        
        Args:
            yaml_content: YAML content as string.
            file_name: Name of the file for logging purposes.
            source_path: Source file path for logging purposes.
            
        Returns:
            List of yamllint error messages.
        """
        try:
            # Create a temporary file with the YAML content
            temp_file = Path(f"/tmp/yamllint_temp_{file_name.replace('/', '_')}.yaml")
            temp_file.write_text(yaml_content)
            
            # Run yamllint on the temporary file
            result = subprocess.run(
                ["yamllint", "-f", "parsable", str(temp_file)],
                capture_output=True,
                text=True,
                check=False
            )
            
            # Remove the temporary file
            temp_file.unlink()
            
            # Process the output
            if result.returncode == 0:
                return []
            else:
                # Format the error messages to be more readable
                error_lines = result.stdout.strip().split('\n')
                formatted_errors = []
                
                for line in error_lines:
                    if line:
                        # Extract line number and error message from yamllint output format
                        parts = line.split(':', 2)
                        if len(parts) >= 3:
                            line_num = parts[1]
                            error_msg = parts[2].strip()
                            formatted_errors.append(f"Line {line_num}: {error_msg}")
                        else:
                            formatted_errors.append(line)
                            
                return formatted_errors
                
        except Exception as e:
            logger.warning(f"Failed to run yamllint: {str(e)}")
            return []
    
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
            
            # Check YAML with yamllint if enabled
            if self.check_yaml_lint:
                lint_errors = self.run_yamllint(yaml_content, file_name, source_path)
                if lint_errors:
                    logger.error(f"YAML lint errors in section for {file_name} in {source_path}:")
                    for error in lint_errors:
                        logger.error(f"  {error}")
                    logger.info("Please fix the YAML formatting issues before processing.")
                    continue
            
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

        # Check YAML with yamllint if enabled
        if self.check_yaml_lint:
            with open(file_path, 'r', encoding='utf-8') as f:
                yaml_content = f.read()
                
            lint_errors = self.run_yamllint(yaml_content, Path(file_path).name, file_path)
            if lint_errors:
                logger.error(f"YAML lint errors in file {file_path}:")
                for error in lint_errors:
                    logger.error(f"  {error}")
                logger.info("Please fix the YAML formatting issues before processing.")
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
