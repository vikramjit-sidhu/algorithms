"""
Hacker Rank - Gem Stones
https://www.hackerrank.com/challenges/service-lane
"""

def main():
    n = int(input().strip())
    char_count = {} #hash containing the letters and the count of the number of strings they appear in
    for i in range(n):
        word = input().strip()
        word_char_cnt = {}
        for char in word:
            if char not in word_char_cnt:
                word_char_cnt[char] = True
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    count_tot = 0
    for key, val in char_count.items():
        if val == n:
            count_tot += 1
    print(count_tot)

if __name__ == '__main__':
	main()