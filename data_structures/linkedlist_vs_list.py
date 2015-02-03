"""
the below functions are used solely by the timeit module to measure
performance between double linked list (code written in double_linked_list.py) and python list

To insert data into both data structures, randint(1, 1000) is used, it is assumed the cost
will be neutralised

elements_in_ds variable contains the number of elements that the data structures hold
range_of_numbers is the range of numbers used to generate random numbers
"""
from timeit import timeit as time
from random import randint 
from double_linked_list import LinkedList

link_list = None
python_list = []
elements_in_ds = 10000
range_of_numbers = elements_in_ds*2
el_search1 = -2, el_search2 = -3

def insert_into_linkedlist():
    """
    Cost of initializing double linked list and appending elements to it
    """
    link_list = LinkedList()
    for i in range(elements_in_ds):
        link_list.add(randint(1, range_of_numbers))
        
        
def insert_into_list():
    """
    Same for python default list
    """
    python_list = []
    for i in range(elements_in_ds):
        python_list.append(randint(1, range_of_numbers))


def search_in_linkedlist():
    """
    Searching for random elements in lists
    """
    
        

def main():
    print("time to add {0} elements to linked list: {1}".format( + \
                elements_in_ds, + \
                time(stmt='__main__.insert_into_linkedlist()', setup='import __main__', number=100)))
                
    print("time to add {0} elements to python list: {1}".format( + \
                elements_in_ds, + \
                time(stmt='__main__.insert_into_list()', setup='import __main__', number=100)))
                
    #for searching operation, appending elements to end of both lists
    link_list.add(el_search1)
    link_list.add(el_search2)
    python_list.append(el_search1)
    python_list.append(el_search2)
    
    
    
	
if __name__ == '__main__':
    main()
    