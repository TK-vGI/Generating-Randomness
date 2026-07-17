# Stage 3/4: Predicting future input
## Description
We will make the simplest version of AI (yes, AI is not only about neural networks) to predict the next character of the  
user input. You will be surprised how often people repeat the same patterns!

Imagine the following: after the second stage for a string `0101010100101001010101000111101010010101010010101010101` we have  
calculated the amount of a certain character (`0` or `1`) that follows a specific triad of numbers:  
`'000': [0, 1]`, `'001': [4, 1]`, `'010': [5, 16]`, `'011': [0, 1]`, `'100': [1, 4]`, `'101': [16, 0]`, `'110': [0, 1]`, `'111': [1, 1]`.  
Now, the user enters the sequence 001110. How can we foresee the next numbers?

Starting with the 4th character, we can predict the input based on the triads obtained in the previous stage. We've  
learned that the combination 001 (the first three characters from the example above) was followed by a 0 in four cases  
out of five. So, the estimated probability that the user will enter 0 as the fourth character is 4/5 = 80%. For the  
probability of 1 is 1/5 = 20%. We can predict 0 as the fourth character. Unfortunately, we didn't guess correctly, but  
let's continue. In the same way, the 5th character is more likely to be 1 based on statistics for the triad preceding it (011).  
This time, we are right.

Of course, in this case, there is no need to convert quantity to probability, since we consider that the most likely  
symbol is the most frequently occurring symbol after a certain triad. But it is better to think in probabilities and  
practice calculating it. Though in the solution, we won't check the way, you've defined the character.

Now, you're invited to write a program, which will sequentially scan three characters of the user's sequence at a time  
and make a prediction of what goes next.

## Objectives
In this stage, your program should:
1. Take and preprocess user input as described in stage 1;
2. Calculate user statistics using triads as described in stage 2. Don't output the statistics this time;
3. Ask the user to enter another test string of `0` and `1`. We'll predict and preprocess the new input in the same way as in  
   the first step, but the minimal length of a string is four: 3 characters for prediction, 1 for accuracy estimation.  
   If this is not the case — ask to enter a whole new string again. Use this text: `Please enter a test string containing 0 or 1:`;
4. Going through the string entered by the user, estimate the frequency of occurrence of `0` or `1` obtained in step 2 for each  
   triad except the last one, and generate predictions. For example, if the count of `0` for the current triad is higher,  
   the program should predict `0`, otherwise, predict `1`. If the counts are equal, pick the prediction at random. Save the  
   predictions in a new variable and print them on a new line after a line with the following text — `predictions:`;
5. Test the accuracy of the predictor by comparing the real input (without first three characters) and the predictions.  
   As the final output, print the line `Computer guessed right N out of M symbols (ACC %)`, where `N` is the number of correctly  
   guessed symbols, `M` is the total length of the test input, and `ACC` is the accuracy value with 0.01% precision — round to  
   two decimal places. Remember to exclude the first three symbols from the user's test string from the calculation!

## Example Output
```
Print a random string containing 0 or 1:

> 0101001010010101011111100010010110000101010101010100101
> The current data length is 55, 45 symbols left
> Print a random string containing 0 or 1:

> 01010101001010010101010001111001010010101010010101010101

Final data string:
010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101

Please enter a test string containing 0 or 1:

> 0110001010100101
> predictions:
> 1011010101101

Computer guessed 10 out of 13 symbols right (76.92 %)
```