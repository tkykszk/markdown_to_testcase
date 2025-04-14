# Tutorials

This page contains tutorials for using the Markdown to Testcase tool to create and convert test cases.

## Quick Start: Creating Test Cases for Different Languages

This quick start guide demonstrates how to create test cases for simple functions in different programming languages and convert them to CSV and Excel formats.

Before diving into the complete typing game example, let's start with a simple example of testing an `add` function in different programming languages.

Create a file named `function_tests.md` with the following content:

```markdown
# Function Tests

Test cases for add functions across different programming languages.

### TestCases (csharp_tests.csv)
- ID: CS001
  Name: C# Add Function - Positive Numbers
  Desc: Test add function with positive integers
  Pre-conditions: C# environment is set up, function is implemented
  Test Steps: |
    1. Call Add(5, 3)
    2. Verify result
  Expected Result: |
    - Function returns 8
  Actual Result: 
  Test Data: a=5, b=3
  Priority: High
  Severity: High
  Status: Not executed
  Environment: .NET 7.0
  Tested By: 
  Date: 
  Comments/Notes: Basic test case for integer addition

- ID: CS002
  Name: C# Add Function - Negative Numbers
  Desc: Test add function with negative integers
  Pre-conditions: C# environment is set up, function is implemented
  Test Steps: |
    1. Call Add(-5, -7)
    2. Verify result
  Expected Result: |
    - Function returns -12
  Actual Result: 
  Test Data: a=-5, b=-7
  Priority: High
  Severity: High
  Status: Not executed
  Environment: .NET 7.0
  Tested By: 
  Date: 
  Comments/Notes: Verify handling of negative numbers

### TestCases (nodejs_tests.csv)
- ID: JS001
  Name: Node.js Add Function - Integer Addition
  Desc: Test add function with integers
  Pre-conditions: Node.js environment is set up, function is implemented
  Test Steps: |
    1. Call add(10, 20)
    2. Verify result
  Expected Result: |
    - Function returns 30
  Actual Result: 
  Test Data: a=10, b=20
  Priority: High
  Severity: High
  Status: Not executed
  Environment: Node.js 20.0
  Tested By: 
  Date: 
  Comments/Notes: Basic JavaScript integer addition

- ID: JS002
  Name: Node.js Add Function - Floating Point
  Desc: Test add function with floating point numbers
  Pre-conditions: Node.js environment is set up, function is implemented
  Test Steps: |
    1. Call add(2.5, 3.5)
    2. Verify result
  Expected Result: |
    - Function returns 6.0
  Actual Result: 
  Test Data: a=2.5, b=3.5
  Priority: Medium
  Severity: Medium
  Status: Not executed
  Environment: Node.js 20.0
  Tested By: 
  Date: 
  Comments/Notes: Verify floating point addition

### TestCases (python_tests.csv)
- ID: PY001
  Name: Python Add Function - Basic Addition
  Desc: Test add function with simple integers
  Pre-conditions: Python environment is set up, function is implemented
  Test Steps: |
    1. Call add(42, 58)
    2. Verify result
  Expected Result: |
    - Function returns 100
  Actual Result: 
  Test Data: a=42, b=58
  Priority: High
  Severity: High
  Status: Not executed
  Environment: Python 3.12
  Tested By: 
  Date: 
  Comments/Notes: Basic Python addition

- ID: PY002
  Name: Python Add Function - String Concatenation
  Desc: Test add function with string inputs
  Pre-conditions: Python environment is set up, function handles strings
  Test Steps: |
    1. Call add("Hello, ", "World")
    2. Verify result
  Expected Result: |
    - Function returns "Hello, World"
  Actual Result: 
  Test Data: a="Hello, ", b="World"
  Priority: Medium
  Severity: Medium
  Status: Not executed
  Environment: Python 3.12
  Tested By: 
  Date: 
  Comments/Notes: Testing string concatenation if function is overloaded

### TestCases (cpp_tests.csv)
- ID: CPP001
  Name: C++ Add Function - Integer Addition
  Desc: Test add function with integers
  Pre-conditions: C++ environment is set up, function is implemented
  Test Steps: |
    1. Call add(100, 200)
    2. Verify result
  Expected Result: |
    - Function returns 300
  Actual Result: 
  Test Data: a=100, b=200
  Priority: High
  Severity: High
  Status: Not executed
  Environment: GCC 13.1
  Tested By: 
  Date: 
  Comments/Notes: Basic C++ addition

- ID: CPP002
  Name: C++ Add Function - Large Numbers
  Desc: Test add function with large integers to check for overflow
  Pre-conditions: C++ environment is set up, function is implemented
  Test Steps: |
    1. Call add(2147483647, 1)
    2. Verify result behavior
  Expected Result: |
    - Function handles overflow according to specifications
    - If int type, may overflow to -2147483648
    - If using long or overflow detection, appropriate result or error
  Actual Result: 
  Test Data: a=2147483647 (INT_MAX), b=1
  Priority: Medium
  Severity: High
  Status: Not executed
  Environment: GCC 13.1
  Tested By: 
  Date: 
  Comments/Notes: Testing integer overflow handling
```

Now run the Markdown to Testcase tool to convert these test cases:

```bash
markdown_to_testcase convert -i function_tests.md
```

This will generate the following output files:

- `csharp_tests.csv`
- `nodejs_tests.csv`
- `python_tests.csv`
- `cpp_tests.csv`
- `test_cases.xlsx` containing all test cases in separate sheets

This quick example demonstrates how to create test cases for simple functions across different programming languages.

## Tutorial: Testing a Typing Game

This tutorial demonstrates how to create test cases for a more complex typing game application using markdown format and convert them to CSV and Excel formats.

## Sample Application: Speed Typer

For this tutorial, let's imagine we are testing a typing game called "Speed Typer" with the following features:

- Users type phrases that appear on the screen
- Timing and accuracy are measured
- Different difficulty levels
- Leaderboard functionality
- User accounts and profiles

## Step 1: Create Markdown Test Cases

First, let's create a markdown file with our test cases. Create a file named `typing_game_tests.md` with the following content:

```markdown
# Speed Typer Typing Game Tests

This document contains test cases for the Speed Typer typing game application.

## Introduction

Speed Typer is a typing game that measures typing speed and accuracy.

### TestCases (core_functionality.csv)
- ID: TC001
  Name: Basic Typing Test
  Desc: Verify that the basic typing functionality works correctly
  Pre-conditions: Application is launched and on the main screen
  Test Steps: |
    1. Click on "Start New Game" button
    2. Select "Easy" difficulty
    3. Type the phrase exactly as shown
    4. Complete the typing challenge
  Expected Result: |
    - Typing input is registered correctly
    - Accuracy and WPM (Words Per Minute) are calculated
    - Results screen is shown with correct stats
  Actual Result: 
  Test Data: Sample phrase "The quick brown fox jumps over the lazy dog"
  Priority: High
  Severity: High
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: This is a core functionality test

- ID: TC002
  Name: Error Handling - Wrong Key Press
  Desc: Verify that wrong keystrokes are correctly identified
  Pre-conditions: Game has started, phrase is displayed
  Test Steps: |
    1. Start typing the displayed phrase
    2. Intentionally press wrong keys for some characters
  Expected Result: |
    - Wrong keystrokes are highlighted in red
    - Error count is increased
    - Accuracy percentage is decreased accordingly
  Actual Result: 
  Test Data: Any available phrase
  Priority: High
  Severity: Medium
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: Error detection is critical for accuracy calculation

### TestCases (user_management.csv)
- ID: TC101
  Name: User Registration
  Desc: Verify that new users can register
  Pre-conditions: Application is launched and on the login screen
  Test Steps: |
    1. Click "Register" button
    2. Enter username "testuser123"
    3. Enter email "test@example.com"
    4. Enter password "Password123!"
    5. Confirm password "Password123!"
    6. Click "Submit" button
  Expected Result: |
    - Registration successful message appears
    - User is redirected to login page
    - User can login with the new credentials
  Actual Result: 
  Test Data: Username: testuser123, Email: test@example.com, Password: Password123!
  Priority: High
  Severity: High
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

- ID: TC102
  Name: User Login
  Desc: Verify that existing users can login
  Pre-conditions: User has registered
  Test Steps: |
    1. Navigate to login screen
    2. Enter username "testuser123"
    3. Enter password "Password123!"
    4. Click "Login" button
  Expected Result: |
    - Login successful
    - User redirected to main menu
    - User's profile information is displayed correctly
  Actual Result: 
  Test Data: Username: testuser123, Password: Password123!
  Priority: High
  Severity: High
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

### TestCases (leaderboard_functionality.csv)
- ID: TC201
  Name: Leaderboard Display
  Desc: Verify that leaderboard shows correct scores
  Pre-conditions: Multiple users have completed typing tests
  Test Steps: |
    1. Login as testuser123
    2. Navigate to "Leaderboard" section
  Expected Result: |
    - Leaderboard is displayed
    - Scores are sorted from highest to lowest
    - User rankings are displayed correctly
    - Current user's position is highlighted
  Actual Result: 
  Test Data: 
  Priority: Medium
  Severity: Low
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

- ID: TC202
  Name: Personal Best Score
  Desc: Verify that personal best scores are tracked
  Pre-conditions: User has completed multiple typing tests
  Test Steps: |
    1. Login as testuser123
    2. Complete a typing test with score better than previous attempts
    3. Navigate to "Profile" page
  Expected Result: |
    - New personal best is displayed on profile
    - Previous scores are available in history
    - New score is reflected in leaderboard
  Actual Result: 
  Test Data: 
  Priority: Medium
  Severity: Medium
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 
```

## Step 2: Process the Test Cases

Once you have created the markdown file with the test cases, use the Markdown to Testcase tool to convert them:

```bash
markdown_to_testcase convert -i typing_game_tests.md
```

## Step 3: Review the Output

After running the tool, check the `output` directory for:

1. CSV files:
   - `core_functionality.csv`
   - `user_management.csv`
   - `leaderboard_functionality.csv`

2. Excel file:
   - `test_cases.xlsx` with three sheets (one for each test case section)

## Step 4: Using the Test Cases

These test cases can now be:

1. Distributed to your QA team
2. Imported into test management tools
3. Used for manual testing
4. Tracked for test execution status

## Advanced: Adding More Test Sections

You can extend the test cases by adding more sections to your markdown file:

```markdown
### TestCases (difficulty_levels.csv)
- ID: TC301
  Name: Difficulty Selection
  Desc: Verify that different difficulty levels can be selected
  Pre-conditions: User is logged in and on the main menu
  Test Steps: |
    1. Click on "New Game"
    2. View available difficulty options
  Expected Result: |
    - Easy, Medium, and Hard difficulty options are displayed
    - Each option shows a brief description
  Actual Result: 
  Test Data: 
  Priority: Medium
  Severity: Medium
  Status: Not executed
  Environment: Chrome 120.0.6099.130, Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 
```

Run the conversion again to include the new section in your output files.

## Tips for Effective Test Cases

1. **Be specific**: Include clear pre-conditions and test steps
2. **Include test data**: Provide sample data to use during testing
3. **Prioritize**: Assign appropriate priority and severity to focus testing efforts
4. **Group logically**: Use different sections for different feature areas
5. **Maintain traceability**: Link test cases to requirements or user stories

## Conclusion

Using the Markdown to Testcase tool makes it easy to maintain test cases in a readable format while still being able to export them to formats suitable for test execution and tracking. The flexible YAML format within markdown allows for structured data that can be easily extended for your specific testing needs.
