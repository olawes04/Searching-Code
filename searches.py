from random import randint

def linear_search(search_list, search_item):
    '''
        Does a search and returns True if the item is found
        Parameters: 
        search_list (list): Any list of items
        search_item (any): Object that you are looking for
    
        Returns: 
        boolean: True if item found, else False
    '''

    #Iterate through the list
        #compare each item with the search item
            #return true if the items are equal
    #if the loop has completed, return False
    pass

def linear_search_for_position_iterative(search_list, search_item):
    #TODO This is a more useful algorithm than the one that returns a boolean. Have a go. Write your own tests.
    pass

def recursive_binary_search(search_list, search_item):
    '''
        Does a binary search and returns True if the item is found
        Parameters: 
        search_list (list): A sorted list of items
        search_item (any): Object that you are looking for
    
        Returns: 
        boolean: True if item found, else False
    '''
    #middle_index = TODO, but make sure it's an integer division (i.e. not just one slash)

    #TODO if search_list[middle_index] is the same as search_item return True

    #TODO if the list has only 1 item return False

    #TODO in one situation call recursive_binary_search(search_list[0:middle_index], search_item) 

    #TODO otherwise recursive_binary_search(search_list[middle_index+1:], search_item)
    pass

def binary_search(search_list, search_item):
    '''
        Does a binary search and returns True if the item is found
        Parameters: 
        search_list (list): A sorted list of items
        search_item (any): Object that you are looking for
    
        Returns: 
        boolean: True if item found, else False
    '''
    #TODO have a go at this one without any help if you can! Write your own tests.
    
    pass

def binary_search_for_position_recursive(search_list, search_item, start_index, end_index):
    '''
        Does a binary search and returns True if the item is found
        Parameters: 
        search_list (list): A sorted list of items
        search_item (any): Object that you are looking for
    
        Returns: 
        int: Position of item, or -1 if not in list
    '''
    #TODO have a go at this one without any help if you can! Write your own tests


#---------------------------testing-----------------------------------------------#

test_list = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,10]
this_search_item = randint(1,18)
print("Searching for: ", this_search_item)
print("Linear search: ", linear_search(test_list, this_search_item))
print("Binary search: ", recursive_binary_search(test_list, this_search_item))
