def main():
    height = get_height()

# loop for the rows
    for i in range(1,height + 1):
            # loop for the spaces to move hashes to oppposite side
            # subtracts from the height backwards
            #  prints the hashes
            for k in range(height , i , -1):
                print(" ", end="")  

            for j in range(1, i + 1):
             print("#", end="")   

            #  for k in range(height , i , 1):
            print(" ", end="")

            for j in range(1, i + 1):
                print("#", end="")     
            print()
                   
                                                     
def get_height():
    # while so that if user enters a value less than 1 or more than 8 the user will be prompted again
    while True:
        # Added a try for error handling if user enters a value other than an integer
        try:
            size = int(input("Enter a height: "))
            if  1 <= size <= 8 : 
                                return size
        except ValueError:
             print("Not an Integer") 

if __name__ == "__main__": 
           
 main()
    