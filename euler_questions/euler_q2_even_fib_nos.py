# project euler finding sum of even numbers in fibonacci
# https://projecteuler.net/problem=2


def main():
    prev = 1; curr = 1; sum = 0

    while curr < 4000000:
        if curr%2 == 0:
            sum += curr
        temp = curr
        curr += prev
        prev = temp

    print(sum)



if __name__ == '__main__':
    main()