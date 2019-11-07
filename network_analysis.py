"""
This program gives finds the most central character in a social network
defined by a file specified by the user.

Authors: Camden Bertucci, Oğuzhan Çölkesen
Time Spent: 2 hours 
"""

def get_dataset(file):
    """
    This function opens the file given by the user and places
    every line in the file as an element to the list, which
    is then returned.
    
    Parameters:
        file - a string, which is the name of the file that defines the
               social network, whose central character is going to be found.
    
    Returns:
        If there is a file in the same directory as the program, the
        function is going to return a list, which includes all the
        lines in the file as elements of the list.
        
        If the file specified by the user is not in the same directory,
        the function returns the boolean variable False.
    """
    try:
        with open(file, 'r') as in_file:
            lines = []
            for line in in_file:
                line_list = line.split(",")
                lines.append(line_list)
                
        return lines
    
    except IOError:
        print("File not found.")
        return False
    
    
def transpose_data(data_list):
    """
    This function gets a nested list, which is interpreted as a matrix,
    and transposes the matrix into a different list, which is then
    returned.
    
    Parameters:
        data_list - a nested list, which includes the data that will be
                    interpreted as a matrix to be transposed. Due to the
                    transposing task, the parameter must be nested list,
                    which is comprised of 2 lists.
    
    Returns:
        A nested list, which includes 2 lists that constitute the
        transposed version of the data_list parameter.
    """
    data_list.pop(0)
    
    for i in range(len(data_list)):
        data_list[i].pop(0)
    
    for i in range(len(data_list)):
        for j in range(len(data_list[0])):
            data_list[i][j] = int(data_list[i][j])
    
    transposed_data_list = []
    
    for i in range(len(data_list[0])):
        transposed_data_list.append([])
        for j in range(len(data_list)):
            transposed_data_list[i].append(data_list[j][i])
            
    return transposed_data_list
        
        
def do_matrix_calculations(data_list, transposed_data_list):
    """
    This function multiplies a nested data list with its tranposed
    version by interpreting them as matrices. The product is then
    stored in a seperate list, which is then used to find the most
    central character by taking the sum of each row in the list.
    At last, the index of the row with the maximum sum is returned.
    
    Parameters:
        data_list - original list of data, which includes a nested list,
                    which will be used to calculate the product
        transposed_data_list - a list, which is the transposed version
                               of data_list that will be used to calculate
                               the product
    
    Returns:
        An integer, which is the index of the row with the maximum sum that
        can also be interpreted as the index of the most central character
        in the social network. If there is tie, the smallest index value
        will be returned.
    """
    sum_list = []

    for i in range(len(data_list)):
        sum_list.append([])
        for j in range(len(transposed_data_list[0])):
            sum = 0
            for k in range(len(transposed_data_list)):
                sum += data_list[i][k] * transposed_data_list[k][j]
            sum_list[i].append(sum)
            
    max_row = 0
    index_max_row = 0
    
    for i in range(len(sum_list)):
        row_sum = 0
        for j in range(len(sum_list[0])):
            row_sum += sum_list[i][j]
            if row_sum != max_row:
                #if there is a tie, we want the first value since the dataset
                #is already in alphabetical order.
                max_row = max(row_sum, max_row)
                if max_row == row_sum:
                    index_max_row = i
            
    return index_max_row
        
        
def find_most_central(file):
    """
    This function is the main function that should be called in the program.
    It accepts a string as the name of the file, which includes the
    social network data. By using helper functions, get_dataset(),
    transpose_data(), and do_matrix_calculations(), the function gets social
    network information in terms of a nested list, which is interpreted as a
    matrix, and finds the index of row with the maximum sum from the product
    of this matrix and its transposed version. At the end, the function
    returns the name of the most central character based on this index.
    
    Parameters:
        file - a string, which is the name of the file that defines the
               social network, whose central character is going to be found.

    Returns:
        If the file is not in the same directory with the program, the function
        returns an empty string.
        
        If the file and the program are in the same directory, the fucntion
        returns a string, which is the name of the most central character in the
        social network in the format it is written on the file.
    """
    dataset = get_dataset(file)
    
    if not dataset:
        return ""
    
    transposed_data_list = transpose_data(dataset)
    index_number = do_matrix_calculations(dataset, transposed_data_list)
    
    dataset = get_dataset(file) #The function is recalled to get names in the dataset.
    
    return dataset[index_number+1][0] #+1 is because of the addition of a categories row.