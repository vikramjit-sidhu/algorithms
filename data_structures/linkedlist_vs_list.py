"""
the below functions are used solely by the timeit module to measure
performance difference between double linked list and python list

Double linked list code written in python (double_linked_list.py)

elements_in_ds variable contains the number of elements that the data structures hold

Operations checked: initialization, add, search and remove


CONCLUSION: 
Python list faster overall, but almost 20 times faster in search test.
"""
from timeit import timeit as time
from random import randint
from double_linked_list import LinkedList

LINK_LIST = None
PYTHON_LIST = None
elements_in_ds = 1000000
# range_of_numbers = elements_in_ds*2
el_search1 = -2
el_search2 = -3


def initializing_linkedlist():
    global LINK_LIST
    LINK_LIST = LinkedList()
    
def initializing_pythonlist():
    global PYTHON_LIST
    PYTHON_LIST = []

    
def insert_into_linkedlist():
    """
    Cost of initializing double linked list and appending elements to it
    """
    global LINK_LIST, elements_in_ds
    for i in range(elements_in_ds):
        LINK_LIST.add(i)
        
def insert_into_list():
    """
    Same for python default list
    """
    global PYTHON_LIST, elements_in_ds
    for i in range(elements_in_ds):
        PYTHON_LIST.append(i)


def search_in_linkedlist():
    """
    Searching for 2 elements in end and 2 elements randomly
    """
    global LINK_LIST, el_search1, el_search2, elements_in_ds
    el_search1 in LINK_LIST
    el_search2 in LINK_LIST
    randint(1, elements_in_ds) in LINK_LIST
    randint(1, elements_in_ds) in LINK_LIST
    -99 in LINK_LIST
    
def search_in_list():
    """
    Searching for 2 elements in end and 2 elements randomly, 1 not in list
    """
    global PYTHON_LIST, el_search1, el_search2, elements_in_ds
    el_search1 in PYTHON_LIST
    el_search2 in PYTHON_LIST
    randint(1, elements_in_ds) in PYTHON_LIST
    randint(1, elements_in_ds) in PYTHON_LIST
    -99 in PYTHON_LIST
     

def removing_from_linkedlist():
    """
    removing elements from beginning, end, and 2 random elements
    """
    global LINK_LIST, el_search2, elements_in_ds
    LINK_LIST.remove(0)
    LINK_LIST.remove(el_search2)
    LINK_LIST.remove(randint(1, int(elements_in_ds/2)))
    LINK_LIST.remove(randint(int(elements_in_ds/2)+1, elements_in_ds))
    
def removing_from_pythonlist():
    """
    removing elements from beginning, end, and 2 random elements
    """
    global PYTHON_LIST, el_search2, elements_in_ds
    PYTHON_LIST.remove(0)
    PYTHON_LIST.remove(el_search2)
    PYTHON_LIST.remove(randint(1, int(elements_in_ds/2)))
    PYTHON_LIST.remove(randint(int(elements_in_ds/2)+1, elements_in_ds))
     
     
     

def main():
    #initializing lists
    print("Time to initialize linked list: {0}".format( + \
                time(stmt='__main__.initializing_linkedlist()', setup='import __main__', number=1000000)))
                
    print("Time to initialize python list: {0}".format( + \
                time(stmt='__main__.initializing_pythonlist()', setup='import __main__', number=1000000)))

    #adding elements to list
    print("Time to add {0} elements to linked list: {1}".format( + \
                elements_in_ds, + \
                time(stmt='__main__.insert_into_linkedlist()', setup='import __main__', number=1)))
                
    print("Time to add {0} elements to python list: {1}".format( + \
                elements_in_ds, + \
                time(stmt='__main__.insert_into_list()', setup='import __main__', number=1)))
                
    #for searching, searching for 2 elements in end of list and 2 randomly between list
    LINK_LIST.add(el_search1)
    LINK_LIST.add(el_search2)
    PYTHON_LIST.append(el_search1)
    PYTHON_LIST.append(el_search2)
    
    print("Searching for 2 elements in end of linked list, 2 random elements in between and one element not in list. Time: {0}".format( + \
                time(stmt='__main__.search_in_linkedlist()', setup='import __main__', number=10)))
                
    print("Searching for 2 elements in end of python list, 2 random elements in between and one element not in list. Time: {0}".format( + \
                time(stmt='__main__.insert_into_list()', setup='import __main__', number=10)))
    
    #removing elements
    print("removing 4 elements. From beginning, end and 2 randomly. Time: {0}".format( + \
                time(stmt='__main__.removing_from_linkedlist()', setup='import __main__', number=1)))
                
    print("removing 4 elements. From beginning, end and 2 randomly. Time: {0}".format( + \
                time(stmt='__main__.removing_from_pythonlist()', setup='import __main__', number=1)))
    
	
if __name__ == '__main__':
    main()
    