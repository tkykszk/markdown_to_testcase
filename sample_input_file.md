# Test Case Specification

This file contains multiple test case sections.

## Temperature Conversion Function Test

### TestCases (fahrenheit_to_celsius.md)
- ID: TC001
  Name: Convert normal Fahrenheit temperature (32°F) to Celsius
  Desc: Input freezing point 32°F and confirm that Celsius 0°C is returned
  Pre-conditions: Function must support decimal calculations
  Test Steps: 1. Pass the input value 32°F to the function \n2. Verify the result
  Expected Result: 0.0
  Test Data: 32
  Priority: High
  Severity: Medium
  Status: Not implemented
  Environment: Python 3.12, macOS
  Tested By: Developer
  Date: 2025-04-05
  Comments/Notes: Fahrenheit 32 degrees is equivalent to Celsius 0 degrees

- ID: TC002
  Name: Convert Fahrenheit 100°F
  Desc: Convert 100°F to Celsius and confirm it's close to 37.78°C
  Test Steps: 1. Pass the input value 100°F \n2. Confirm result is 37.78±0.01
  Expected Result: approximately 37.78
  Test Data: 100
  Priority: Medium
  Severity: Low
  Status: Not implemented
  Environment: Python 3.12
  Tested By: Test Engineer
  Comments/Notes: Results are floating point so be aware of rounding errors

- ID: TC003
  Name: Convert negative Fahrenheit value
  Desc: Input Fahrenheit -40°F and confirm that Celsius -40°C is returned
  Test Steps: 1. Pass the input value -40°F \n2. Check the result
  Expected Result: -40.0
  Test Data: -40
  Priority: High
  Severity: High
  Status: Not implemented
  Environment: Python 3.12, Linux
  Comments/Notes: -40°F and -40°C are the only temperature values that match

## API Function Test

### TestCases (api_temperature_conversion.md)
- ID: TC101
  Name: Send 32°F to API and retrieve Celsius 0°C
  Desc: Send freezing point Fahrenheit 32 degrees via API and verify Celsius 0.0 is returned
  Pre-conditions: "API must be running, endpoint: /convert"
  Test Steps: |
    1. POST send the following JSON:
       {
         "fahrenheit": 32
       }
    2. HTTP 200 should be returned
    3. Verify that the "celsius" field in the response JSON is 0.0
  Expected Result: '{"celsius": 0.0}'
  Test Data: '{"fahrenheit": 32}'
  Priority: High
  Severity: Medium
  Status: Not implemented
  Environment: API server localhost:5000, Python FastAPI
  Tested By: Developer
  Comments/Notes: Values are expected to be returned as floating point

- ID: TC102
  Name: Send 100°F to API for Celsius conversion
  Desc: 100°F -> approximately 37.78°C conversion verification
  Test Steps: |
    1. Send JSON {"fahrenheit": 100} to the API
    2. Verify HTTP 200 response
    3. Check that "celsius" value is within 37.78±0.01 range
  Expected Result: '{"celsius": approximately 37.78}'
  Test Data: '{"fahrenheit": 100}'
  Priority: Medium
  Severity: Low
  Status: Not implemented
  Environment: Postman or curl
  Comments/Notes: Be aware of floating point rounding errors

## String Formatting Function Test

### TestCases (format_number_with_commas.md)
- ID: TC201
  Name: Insert commas as thousands separators in integers
  Desc: Test the function that converts int or float values to strings with commas inserted every 3 digits in the integer part
  Pre-conditions: |
    - Input is int or float type
    - Output is str type
    - Decimal part remains unchanged (example: 1234567.89 → "1,234,567.89")
    - Minus sign position doesn't change for negative values (example: -1234 → "-1,234")
  Test Steps: |
    1. Input the following values to the target function:
        - 1
        - 123
        - 1234
        - 123456789
        - 123456789012
        - 1234567.89
        - -987654321
        - 0
    2. Verify that the returned output strings have commas inserted at the correct positions (every 3 digits)
    3. For float values, confirm that the decimal part is maintained
    4. Verify that the output is a string
  Expected Result: |
    - Input 1 → Output "1"
    - Input 123 → Output "123"
    - Input 1234 → Output "1,234"
    - Input 123456789 → Output "123,456,789"
    - Input 123456789012 → Output "123,456,789,012"
    - Input 1234567.89 → Output "1,234,567.89"
    - Input -987654321 → Output "-987,654,321"
    - Input 0 → Output "0"
  Test Data: [1, 123, 1234, 123456789, 123456789012, 1234567.89, -987654321, 0]
  Priority: High
  Severity: Medium
  Status: Not implemented
  Environment: Python 3.12, Windows/macOS/Linux
  Tested By: Developer A
  Date: 2025-04-05
  Comments/Notes: Per specification, only the integer part is subject to comma separation, and the decimal part remains unchanged
