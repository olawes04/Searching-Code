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

def binary_search_recursive(items, start_index, end_index, search_item):
    if start_index > end_index:
        return -1
  # TODO use start_index and end_index to find out if the sublist is of size 0 or less and return appropriate int
    if start_index>=end_index :
        return ("Index is too small")

  # TODO work out middle index of the sublist
    middle_index = (start_index + end_index)
  # TODO from that, set current item
    current_item = items[middle_index]
  # TODO base case 2: find out if current item is the search item and return the appropriate index
    if current_item==search_item:
        return middle_index
  # recursive cases: do a BS on a subset of the list by tweaking appropriate start or end index
    if current_item < search_item:
        return binary_search_recursive(items, middle_index+1, end_index, search_item)
    else:
        return binary_search_recursive(items, middle_index-1, end_index, search_item)

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
