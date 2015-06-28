"""
Dynamic Programming - Longest common subsequence
"""

def lcs(word1, word2):
    memo = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
    for idx_w1, char1 in enumerate(word1):
        for idx_w2, char2 in enumerate(word2):
            if char1 == char2:
                memo[idx_w1+1][idx_w2+1] = memo[idx_w1][idx_w2] + 1
            else:
                memo[idx_w1+1][idx_w2+1] = max(memo[idx_w1+1][idx_w2], memo[idx_w1][idx_w2+1])
    print(find_comm_subseq(memo, word1, word2))
    return memo[len(word1)][len(word2)]

def find_comm_subseq(memo, word1, word2):
    """ Finding subsequence using the word represented in the rows of the memoized matrix, i.e. word1 """
    row = len(word1)
    col = len(word2)
    word = ''
    while memo[row][col] != 0:
        if memo[row-1][col-1] != memo[row][col]:
            word = word1[row-1] + word
            row -= 1
            col -= 1
        else:
            row -= 1
    return word

def main():
    seq1 = input().strip()
    seq2 = input().strip()
    print(lcs(seq1, seq2))

if __name__ == '__main__':
    main()