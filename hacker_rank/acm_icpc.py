"""
Hacker Rank - Algorithms Warmup
ACM ICPC team
https://www.hackerrank.com/challenges/acm-icpc-team
"""

def find_max_skillset(n, person_skills):
    """ Using brute force method - O(n^2) """
    max_or = 0  #the number representing the max no of topics a pair can have in common, using bitwise or gate
    count_max_or = 0   #the number of pairs with max no of topics in common
    len_list = len(person_skills)
    for i in range(len_list):
        for j in range(i+1, len_list):
            or_op = person_skills[i] | person_skills[j]
            if or_op > max_or:
                count_max_or = 1
                max_or = or_op
            elif or_op == max_or:
                count_max_or += 1
    no_common_skills = bin(max_or).count('1')    #count the max no of topics a pair can know
    return (no_common_skills, count_max_or)
    
def main():
    n, m = (int(i) for i in input().strip().split(' '))
    person_skills = []
    for i in range(n):
        person_skills.append(int(input().strip(), 2))
    common_skills, count_skills = find_max_skillset(n, person_skills)
    print(common_skills)
    print(count_skills)
    

if __name__ == '__main__':
	main()