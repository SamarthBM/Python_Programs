"""
* @Author: Samarth BM.
* @Date: 2021-09-11 20:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-11 20:11 
* @Title: :To print 2D array.
"""

def Array2D():
    """
    Description:
        This function is to take elements as user input and print the 2D array.
        At first rows and columns are taken as input.
        Next, the elements are taken as input.
        Using nested for loop all the elements are printed.
     
    """    
    try:
        rows = int(input("Enter the number of rows: "))
        col = int(input("Enter the number of columns: "))

        matrix = []

        # To create a 2D array.
        for row in range(rows):
            array = []
            for column in range(col):
                array.append( (int(input("Enter the element:: "))) )
            matrix.append(array)

        # To print the elements.
        print("The 2D array for entered elemets is: ")
        for row in range(rows):
            for column in range(col):
                print(matrix[row][column], end=" ")
            print()

    except Exception as e:
        print("Exception occured is: ",e)

if __name__ == "__main__":
    Array2D()

    


