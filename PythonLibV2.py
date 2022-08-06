'''Read multiple inputs separated by space from keyboard
   Ex: K,M = get_input_values(int)  case of two inputs
   Ex: K,L,M = get_input_values(float)  case of two inputs
   Ex: list1=[(3,4)]. list1 = list1.append(list(get_input_values(float))    '''
def get_input_values(input_type):
    return map(input_type,input().split())# raw_input if python 2
     #   K =  int(raw_input())    read one int variable

''' Remove outer brakets and string quotes from list 
    Ex: list1=['a','b','c']  ->  a,b,c    '''
def get_list_no_brackets_quotes(list1):
    return (','.join(list1))

''' Remove outer brakets from list 
    Ex: list1=['a','b','c']  ->  'a','b','c'    '''
def get_list_no_outer_brackets(list1):
    return (str(list1)[1:-1])

''' Remove characters between start and end position in string   '''
def get_string_chars_removed(string1,start,end):
    if len(string1) > end :
        return (string1[0: start:] + string1[end + 1::])
    else:            
        return (string1[0: start:])

''' Remove special characters from items in list 
    Ex: list1=['a#','@b','c')]  ->  ['a','b','c']    '''
def get_list_without_special_chars(list1,special_char):
    #special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
    return [''.join(filter(lambda i: i not in special_char, string)) for string in list1]
    
'''  square function items in list or list(tuples)
     [(1, 2), (1, 5)] ->  [1,4,1,25]
     [1,2,3]   ->  [1,4,9]            '''
def square_items_list(list1,with_tuples):
    if with_tuples:
        return list( j * j  for i in list1 for j in i)
    else:
        return list( i * i  for i in list1 )  

'''  Create list(tuples) of column values from rows -transpose/zip
    zip takes one item from each list at a time
    [('a',2),(3,4)]  ->  [('a',3),(2,4)] '''
def transpose_rows_list(list1):
    return list(zip(*list1))

'''  Merge(if string)/sum(if int) column values in lists or list(tuples)
    [1,2] & [3,4]  ->  [(4,6)]
    ['a','b'] & ['c','d']  ->  ['ac','bd']     
    [(1,'b')] & [('c','d')]  ->  [1,'b','c','d']    '''
def sum_merge_columns_list(list1,list2):
    return list(i+j for i,j in zip(list1,list2))

'''  Sum the squares of item columns in two lists
    [1,2] & [3,4]  ->  [(10,20)]  '''
def sum_square_columns_list(list1,list2):
    return list((i**2+j**2) for i,j in zip(list1,list2))

''' get all combinations  of two lists
    Ex: [1,2] & [3,4]  -> [(1,3),(1,4),(2,3),(2,4)]  '''
def get_list_combinations(list1,list2):
    from itertools import product
    return list(product(list1, list2))

'''  evaluate expression from saved in list  (or from input)
    Also, used to convert/concatenate string to list
    x = 1,  list1 = ['x**3','+','x**2','+','x','+','1'] -> 4     '''          
def evaluate_expression_in_list(list1):
    return eval(''.join(str(i) for i in list1))

'''  print items in list 
     Ex: list1 = [(3,4),(5,6)].   print_sum_tuples_in_list(list1)    -> 7 11
     Ex: tuples1 = (3,4). print_sum_tuples_in_list(list(tuples1)) ->7    ''' 
def print_sum_tuples_in_list(list1):
    for i in list1:
        print(sum(i))

'''  print items in list without brackets and comma 
     Ex: list1 = [(3,4) , (5,6)].   3 4   5 6   ''' 
def print_formatted_list(list1):
    for i in list1:
        print(re.sub('\[|,|\]|\(|\)','',str(i)))  # without [ or , or ] or ( or ) 
    
'''  Sort a two dim List based on column k and then on column 0(optinal) 
    Ex [(7, 5, 0), (10, 1, 5), (6, 4, 9)] -> [(10, 1, 5), (6, 4, 9), (7, 5, 0)] '''        
def sort_list_asc(list1,k):
    list1.sort(key=lambda row: (row[k],row[0]), reverse=False)
    return list1

''' Reverse a Number 
    assign  reverse_number=0 before calling get_reverse_number()'''
def get_reverse_number(num): 
    global reverse_number
    if (num > 0):  
        remainder = num % 10  
        reverse_number = (reverse_number * 10) + remainder  
        get_reverse_number(num // 10)  
    return reverse_number  

'''  use namedtuples to read, hold, manipulate datasets with column names '''
def get_average_grade_from_dataset():
    from collections import namedtuple 
    # read 2 lines from input,1st number of rows, 2nd column names
    (number_students, column_names) = (int(raw_input()), raw_input().split())
    # Define class Grade with column names
    Grade = namedtuple('Grade', column_names)
    # get GRADES values from input. using dot(.) to refer to GRADES data regardless of their column position 
    # _make function convert from iterable to namedtuple
    marks = [int(Grade._make(raw_input().split()).GRADES) for _ in range (number_students)]  
    # print Average of Marks with two decimals
    print("{:.2f}".format(sum(marks) / number_students))

'''  get even numbers  (for odd  repalce ==1)'''
def extract_even_numbers(list1):
    list2=re.sub('[^0-9]','',s)  # extract only numbers from list
    return list(a for a in list2 if int(a)%2==0)

''' Usefull functions'''
re = max(lista)	# returns maximum nbr in list
re = max( lista, key=lambda x:x*x )	# returns number in list whose square is maximum
re = any( [ (lambda x:x%2==1)(num) for num in lista] ) 	# True if any nbr in list is odd ( even x:x%2==0)
re = all( [ (lambda x:x%2==1)(num) for num in lista] )	# True if all nbrs in list are odd
print(f” result is {re} “)
sum_all = sum(range(1, n + 1))	# sum of arithmetic progression 1 to n
range_to_list = list(range(2, 10, 2)) # define a list with number of inputs and values 


list1 = [(7, 5, 0), (10, 1, 5), (6, 4, 9)]
print(print_formatted_list(sort_list_asc(list1,1)))
