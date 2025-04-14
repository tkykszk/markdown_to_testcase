#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pytest configuration file.
"""

import os
import sys
import pytest
from pathlib import Path

# Add the project root to the path so we can import the package
sys.path.insert(0, str(Path(__file__).parent.parent))
