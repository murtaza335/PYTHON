# PYTHON
Welcome to the Python Projects Repository! This repository serves as a collection of all my Python-based projects. From simple scripts to complex applications, you'll find a variety of projects showcasing different aspects of Python programming.
here's the code description.
# Number System Converter

This Python program allows you to convert numbers between different number systems: binary, decimal, octal, and hexadecimal. 

## Features

- Convert from any base (2, 8, 10, 16) to any other base.
- Handles both integer and alphanumeric hexadecimal input.
- User-friendly interface with prompts for input and output bases.

## Requirements

- Python 3.x

## Usage

### Running the Program

To run the program, simply execute the Python script. You will be prompted to enter the base of the number you want to convert from, followed by the base of the number you want to convert to.

```sh
python number_system_converter.py
```

### Input and Output

The program will prompt you to enter the base of the number you want to convert from and the base you want to convert to. It will then prompt you to enter the number in the specified base. Finally, it will output the converted number.

### Example

1. **Convert from Decimal to Binary:**
    ```
    select the base of the input number to convert from(2/8/10/16): 10
    select the base of the number to convert to(2/8/10/16): 2
    Enter a decimal number: 45
    Output: 101101
    ```

2. **Convert from Hexadecimal to Decimal:**
    ```
    select the base of the input number to convert from(2/8/10/16): 16
    select the base of the number to convert to(2/8/10/16): 10
    Enter a hexadecimal number: 1A3
    Output: 419
    ```

## Functions

### `input_number(choice_from)`

Prompts the user to input a number in the specified base.

- **Parameters:**
  - `choice_from`: The base of the input number (2, 8, 10, 16).
- **Returns:** The input number, either as an integer or a string for hexadecimal.

### `hexa_10_11_12(remainder)`

Converts decimal remainders to their corresponding hexadecimal characters.

- **Parameters:**
  - `remainder`: The remainder to convert (10-15).
- **Returns:** The corresponding hexadecimal character ('A'-'F').

### `hexa_ABC(a)`

Converts hexadecimal characters to their corresponding decimal values.

- **Parameters:**
  - `a`: The hexadecimal character ('A'-'F').
- **Returns:** The corresponding decimal value (10-15).

### `from_decimal(choice_from, choice_to, ans)`

Converts a decimal number to the specified base.

- **Parameters:**
  - `choice_from`: The base of the input number (should be 10 for this function).
  - `choice_to`: The base to convert to (2, 8, 16).
  - `ans`: The input number if already in decimal.
- **Returns:** None. Prints the converted number.

### `to_decimal(choice_from, choice_to)`

Converts a number from the specified base to decimal.

- **Parameters:**
  - `choice_from`: The base of the input number (2, 8, 16).
  - `choice_to`: The base to convert to (should be 10 for this function).
- **Returns:** The converted decimal number.

### `start()`

The main function that drives the program. Prompts the user for input and output bases, then performs the conversion.

## Program Flow

1. The `start()` function is called.
2. The user is prompted to select the input and output bases.
3. Depending on the input and output bases, the appropriate conversion functions (`from_decimal` or `to_decimal`) are called.
4. The converted number is printed to the console.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
