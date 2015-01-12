# project euler questions
# https://projecteuler.net/problem=1

def main():
    sum = 0

    for i in range(0, 1000, 3):
        sum += i

    for i in range(0, 1000, 5):
        sum += i

    subtract_sum = 0

    for i in range(0, 1000, 15):
        subtract_sum += i

    sum -= subtract_sum

    print ("the sum is: {}".format(sum))



if __name__ == '__main__':
    main()
