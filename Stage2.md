# Stage 2/4: Analyzing user input
## Description
Now it's time to reveal the secret of our magical predictive system. We will create a "profile" of the user that will  
contain information about patterns found in their "random" clicks. To do this, we will count how many times a certain  
character (`0` or `1`) follows a specific triad of numbers. Examples of triads: `000` or `011`.  
For example, in the string `00010000`, the triad `000` is followed by a `1` and once by `0`. Visually, it looks like this — `00010000`.

In the next stage, we will create a prediction algorithm based on this information.

## Objectives
In this stage, your program should:
1. Read the user input the same way as in the previous stage;
2. Get all possible triads from the string. For each of them, count the number of `0` and `1` that follow them;
3. Output the result in the following format: `triad: {counts_of_0}, {counts_of_1}`, for example, `000: 57,12`. Print the result  
   for each triad on a new line. The triads must be ordered in ascending order of their decimal representation —  
   for example, `110` in binary equals `1*4 +1*2 + 0*1 = 61* 4 + 1*2 + 0*1 = 6` in decimal.

You may wonder, how many triads are there? There are three vacant seats: _ _ _. Two options (`0` or `1`) for the first seat,  
then two options for the second seat, and so on. In the case of the same number of options at each seat, the number of  
unique sequences can be calculated as follows:  

`number of options^number of seats`

You can use `bin()` and `zfill()` functions to convert number to triad representation, for example — `2` -> `010`.

## Example
The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.
```
Print a random string containing 0 or 1:

> 01010010010001010100100101001001
The current data length is 32, 68 symbols left
Print a random string containing 0 or 1:

> 10100011001010101010111101001001011010
The current data length is 70, 30 symbols left
Print a random string containing 0 or 1:

> 0101101010100110101010101010001110011

Final data string:
01010010010001010100100101001001101000110010101010101111010010010110100101101010100110101010101010001110011

000: 0,3
001: 10,5
010: 13,18
011: 5,2
100: 3,12
101: 20,3
110: 2,5
111: 2,1
```