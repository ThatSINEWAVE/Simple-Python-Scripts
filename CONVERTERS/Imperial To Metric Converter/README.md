**Imperial Metric Converter**

This script is a simple Imperial-Metric converter implemented in Python. It provides functionality to convert between various units of distance, including miles to kilometers, kilometers to miles, feet to meters, and meters to feet.

### Usage

To use the converter, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the script `imperialmetricconverter.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script with the following command:

```
python imperialmetricconverter.py <conversion> <value>
```

Replace `<conversion>` with the desired conversion type and `<value>` with the value you want to convert.

### Available Conversions

- `mk`: Miles to Kilometers
- `km`: Kilometers to Miles
- `fm`: Feet to Meters
- `mf`: Meters to Feet

### Example

To convert 10 miles to kilometers, run the following command:

```
python imperialmetricconverter.py mk 10
```

This will print the result:

```
10 miles is equal to 16.0934 kilometers
```

Similarly, you can perform other conversions by specifying the appropriate conversion type and value.

### Note

Ensure that you provide the correct number of command-line arguments, otherwise, the script will display an error message indicating the correct usage. Additionally, invalid conversion types will also prompt an error message.