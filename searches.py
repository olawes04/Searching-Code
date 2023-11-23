from random import randint

def linear_search(search_list, search_item):
 for i in range (len(search_list)): 
    if list[i]==search_item:
        return True 
    elif i==len(search_list):
        return False
    else: 
        continue 
    
  
    #Iterate through the list
        #compare each item with the search item
            #return true if the items are equal
    #if the loop has completed, return False
    pass

def linear_search_for_position_iterative(search_list, search_item):
    for i in range (len(search_list)): 
        if list[i]==search_item:
            return i 
        elif i>len(search_list):
            return (-1)
        else: 
            pass 
    
    pass

def binary_search_recursive(search_list, search_item, start_index, end_index):
    if start_index > end_index:
        return -1
    if start_index>=end_index :
        return ("Index is too small")
    middle_index = (start_index + end_index)
    current_item = search_list[middle_index]
    if current_item==search_item:
        return True
    if current_item < search_item:
        return binary_search_recursive(search_list, middle_index+1, end_index, search_item)
    else:
        return binary_search_recursive(search_list, middle_index-1, end_index, search_item)

def binary_search(search_list, search_item):
    found=False
    first=0
    final=len(search_list)-1
    while first<=final and found==False:
        middle_index=(first+final)//2
        if search_item==search_list[middle_index]:
            found=True
            return True
        else:
            if search_item> search_list:
                first=middle_index+1
            else:
                last=middle_index-1
    if found==False:
        return False
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

def binary_search_recursive_position(search_list, search_item, start_index, end_index):
    if start_index > end_index:
        return -1
    if start_index>=end_index :
        return ("Index is too small")
    middle_index = (start_index + end_index)
    current_item = search_list[middle_index]
    if current_item==search_item:
        return middle_index
    if current_item < search_item:
        return binary_search_recursive_position(search_list, middle_index+1, end_index, search_item)
    else:
        return binary_search_recursive_position(search_list, middle_index-1, end_index, search_item)

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

search_list = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,10]
start_index = 0
end_index = len(search_list) - 1
search_item = randint(1,18)
print("Searching for: ", search_item)
print("Linear search: ", linear_search(search_list, search_item))
print("Binary search: ", binary_search_recursive(search_list, search_item, start_index, end_index))
