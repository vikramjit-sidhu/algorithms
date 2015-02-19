"""
Hacker Rank
maximising XOR
https://www.hackerrank.com/challenges/maximizing-xor
"""

def maximize_xor(smaller, bigger):
    xsmall, xlarge = '', ''    #contains the numbers whose xors are max
    current_power = int(pow(2, len(bigger)-1))   #the current power of 2, for which character is being iterated
    max_diff = int(bigger,2) - int(smaller,2)   #the max value that diff_nums can attain
    diff_nums = 0   #the difference in value between the numbers
    for smbit, lbit in zip(smaller, bigger):
        if (int(smbit)^int(lbit)) == 1:
            xsmall = xsmall + smbit
            xlarge = xlarge + lbit
            if smbit =='0':
                diff_nums += current_power
            else:
                diff_nums -= current_power
        else:
            if diff_nums > current_power:
                diff_nums -= current_power
                xsmall = xsmall + '1'
                xlarge = xlarge + '0'
            elif (diff_nums + current_power) < max_diff:
                diff_nums += current_power
                xsmall = xsmall + '0'
                xlarge = xlarge + '1'
            elif smbit == '0' and lbit == '0':
                xsmall = xsmall + '0'
                xlarge = xlarge + '0'
            else:
                xsmall = xsmall + '1'
                xlarge = xlarge + '1'
        current_power = current_power // 2
    return (xsmall, xlarge)

def main():
    #the 2 high and low numbers
    #NOTE: the numbers can only be +ve
    l = int(input().strip())
    r = int(input().strip())
    #bin() converts int to binary format in python, eg 10 = 0b1010
    #taking from 2nd character onwards, the b is removed, leaving only the imp bit.
    if l > r:
        l, r = r, l
    smaller = bin(l)[2:]
    bigger = bin(r)[2:]
    #in case 0's need to be padded to smaller int
    if len(smaller) < len(bigger):
        zeros_needed = len(bigger) - len(smaller)
        smaller = '0'*zeros_needed + smaller
    xs, xl = maximize_xor(smaller, bigger)
    #converting from binary string to int
    smallint, largeint = int(xs, 2), int(xl, 2)
    print(smallint^largeint)
    
if __name__ == '__main__':
    main()
