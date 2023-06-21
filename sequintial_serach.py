import random 

def sequintial_search(number_list, target_value):
    for index in range(len(number_list)):
        #determin if the number at current index is = to target 
        #if return the index and end the loop
        if target_value == number_list[index]:
            return index 
    
    return -1

def main():
    #crreate a list of 100 numbers from 1 to 100
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()
   
    found_index = sequintial_search(number_list, 105)

    print(found_index)

main()