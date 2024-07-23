def binary_search(sequence,item):
    start_index = 0
    end_index = len(sequence) - 1
    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) //2
        midpoint_value = sequence[midpoint]
        if item < midpoint_value:
            end_index = midpoint - 1
        elif item > midpoint:
            start_index = midpoint + 1
        else:
            return none
    return midpoint
sequence_a = [9,11,13,17,21,31,37]
item_a = 37
print(binary_search(sequence_a,item_a))