# Time Addition Challenge

This project is part of the freeCodeCamp challenge to create a Python program that adds a specified duration to a given start time, considering both 12-hour clock format and an optional starting day of the week.

## Challenge Description

The challenge involves implementing a function named `add_time` with the following features:

- Takes a start time in the 12-hour clock format (ending in AM or PM).
- Accepts a duration time that indicates the number of hours and minutes.
- Has an optional starting day of the week parameter (case-insensitive).
- Adds the duration time to the start time and returns the result.

The function should handle various cases, such as indicating the next day or multiple days later in the output. Additionally, if the starting day is provided, the output should display the day of the week.

## Code Implementation

The code is implemented in Python and follows the specified requirements. It ensures valid input for both start time and duration, considering correct formats and ranges. The code is structured for readability and modularity.

## Usage

1. **Input Start Time:**
   - Enter the start time in the format `HH:MM AM/PM`. Ensure the time is valid, and AM/PM is correctly specified.

2. **Input Duration:**
   - Enter the duration of the meeting in the format `HH:MM`.

3. **Optional: Input Starting Day of the Week:**
   - Optionally, you can enter the starting day of the week (case-insensitive). Only valid days (Monday to Sunday) are accepted.

4. **Output:**
   - The program will calculate the new time, considering the duration, and display the result.
   - If the result is on the next day or later, it will indicate that in the output.
   - If a starting day is provided, it will also display the day of the week.

## Examples

```python
# Example 1
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# Example 2
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
