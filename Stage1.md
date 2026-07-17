# Generating Randomness
## Description
To train the machine to predict the next user input, we need to collect data about the user. We will ask them to  
press `0`'s and `1`'s on the keyboard in an unpredictable order. These data will be kept in a string of the format `011100101010…`  
Do not consider other characters. If a user makes a mistake and presses `2` instead of `1` or enters characters separated by commas,  
spaces or any other character — just exclude them from the input string.

## Objectives
In this stage, your program should:
1. Store the value of the minimum length of a string of zeros and ones that the user must enter as a constant. Specify the  
   minimum string length equal to `100` — this should allow you to collect enough statistics without taking too much of the user's time;
2. Ask a user to enter a random string of `0` and `1`. Use this statement: `Print a random string containing 0 or 1:`;
3. Read user input and filter out inappropriate symbols from each user input. Remove all characters except `1` and `0`. For example,  
   if a user entered `1.0,1 120`, then after filtering it should be `10110`;
4. Append the processed string to the general string containing all the data from the inputs;
5. Keep asking the user for new input strings and appending them to the general string until the length of the general string  
   is equal or exceeds `100`. If it exceeds `100`, don't remove extra `1` and `0`: `100` symbols are the minimum required length,  
   but the more data we have, the better;
6. Output the final data string.

Inform the user how many characters they have already entered, and how many are left, before asking to enter characters again.  
Use this pattern: `Current data length is X, Y symbols left`.

## Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

For simplicity, we will limit ourselves to a string of length 20 in this example.
```
Print a random string containing 0 or 1:

> 01000111001
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 2345
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 1010456
Current data length is 15, 5 symbols left
Print a random string containing 0 or 1:

> 0100010

Final data string:
0100011100110100100010
```