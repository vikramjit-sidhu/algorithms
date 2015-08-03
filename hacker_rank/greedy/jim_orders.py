"""
Jim and the Orders
https://www.hackerrank.com/challenges/jim-and-the-orders
"""

def put_in_dict(time_dict, person_num, time_order_finished):
    """ 
    Put in values to dictionary, key is time_order_finished
    The value person_num is put as a list, to append further values if needed
    """
    if time_order_finished in time_dict:
        time_dict[time_order_finished].append(person_num)
    else:
        time_dict[time_order_finished] = [person_num]
    return time_dict

def print_asc_order(time_dict):
    """
    Print values of dictionary in ascending order of keys
    Each value in (key, value) pair is a list
    """
    for key in sorted(time_dict.keys()):
        for person in time_dict[key]:
            print(person, end=' ')
    
def main():
    num_orders = int(input().strip())
    # this dictionary is in format; time: person(s) who will get orders
    # the value could be a list as there could be multiple persons getting orders
    time_dict = {}
    for person_num in range(1, num_orders+1):
        order_time, order_process_time = (int(i) for i in input().strip().split(' '))
        time_order_finished = order_time + order_process_time
        time_dict = put_in_dict(time_dict, person_num, time_order_finished)
    # print the times in which the fans receive the order in ascending order by time
    print_asc_order(time_dict)
    

if __name__ == '__main__':
    main()