from lc import *

# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse both numbers.
        first_number = num1[::-1]
        second_number = num2[::-1]

        # For each digit in second_number, multipy the digit by first_number and then
        # store the multiplication result (reversed) in the results array.
        results = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        # Add all of the results together to get our final answer (in reverse order)
        answer = self.sum_results(results)

        # Reverse answer and join the digits to get the final answer.
        return "".join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(
        self, digit2: str, num_zeros: int, first_number: List[str]
    ) -> List[int]:
        """Multiplies first_number by a digit from second_number (digit2)."""
        # Insert zeros at the beginning of the current result based on the current digit's place.
        current_result = [0] * num_zeros
        carry = 0

        # Multiply each digit in first_number with the current digit of the second_number.
        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append last digit to the current result.
            current_result.append(multiplication % 10)

        if carry != 0:
            current_result.append(carry)
        return current_result

    def sum_results(self, results: List[List[int]]) -> List[int]:
        # Initialize answer as a number from results.
        answer = results.pop()

        # Add each result to answer one at a time.
        for result in results:
            new_answer = []
            carry = 0

            # Sum each digit from answer and result. Note: zip_longest is the
            # same as zip, except that it pads the shorter list with fillvalue.
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                # Add current digit from both numbers.
                curr_sum = digit1 + digit2 + carry
                # Set carry equal to the tens place digit of curr_sum.
                carry = curr_sum // 10
                # Append the ones place digit of curr_sum to the new answer.
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            # Update answer to new_answer which equals answer + result
            answer = new_answer

        return answer


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize answer as a string of zeros of length N.
        N = len(num1) + len(num2)
        answer = [0] * N

        # Reverse num1 and num2
        first_number = num1[::-1]
        second_number = num2[::-1]

        for place2, digit2 in enumerate(second_number):
            # For each digit in second_number multiply the digit by all digits in first_number.
            for place1, digit1 in enumerate(first_number):
                # The number of zeros from multiplying to digits depends on the place
                # of digit2 in second_number and the place of the digit1 in first_number.
                num_zeros = place1 + place2

                # The digit currently at position numZeros in the answer string
                # is carried over and summed with the current result.
                carry = answer[num_zeros]
                multiplication = int(digit1) * int(digit2) + carry

                # Set the ones place of the multiplication result.
                answer[num_zeros] = multiplication % 10

                # Carry the tens place of the multiplication result by
                # adding it to the next position in the answer array.
                answer[num_zeros + 1] += multiplication // 10

        # Pop the excess 0 from the end of answer.
        if answer[-1] == 0:
            answer.pop()

        return "".join(str(digit) for digit in reversed(answer))


def multiply(self, num1, num2):
    dicT = {"0":0,"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    aval = 0
    bval = 0
    iA = len(num1)-1
    aTok = True
    bTok = True
    iB = len(num2)-1
    while aTok or bTok:
        if iA < 0:
            aTok = False
        if iB < 0:
            bTok = False
        if aTok:
            aval += dicT[num1[iA]] * 10**(len(num1)-iA-1)
            iA -= 1
        if bTok:    
            bval += dicT[num2[iB]] * 10**(len(num2)-iB-1)
            iB -= 1
            
    return str(aval * bval)

# https://leetcode.com/problems/multiply-strings/solutions/17615/simple-python-solution-18-lines/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def multiply(self, a: str, b: str) -> str:
        d = [0] * (len(a) + len(b))
        p = len(d)-1
        for i in reversed(a):
            k = p
            for j in reversed(b):
                d[k] += int(i) * int(j)
                d[k-1] += d[k]//10
                d[k] %= 10
                k -= 1
            p -= 1
        pt = 0
        while pt < len(d)-1 and d[pt] == 0:
            pt += 1
        return ''.join(map(str, d[pt:]))

class Solution:
    def multiply(self, a: str, b: str) -> str:
        return str(int(a)*int(b))

test('''
43. Multiply Strings
Medium

7115

3380

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
Accepted
844,820
Submissions
2,065,171
''')
