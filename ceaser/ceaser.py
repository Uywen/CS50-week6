# above for loop
while True:
    try:
        # gets input from user to enter a number
        # this number determines how many letters it will be shifted
        key = int(input("Enter a number: "))

        # User cannot enter a value less than zero
        if key > 0 :
            break

    except ValueError:
        print("usage ./Ceaser Key")

# input for user to enter text
text = input("plaintext: ")


for value in text:
    
    # checks if character is an alphabetical character
        if value.isalpha():

        #  checks the range of the lowercase letters
         if value.islower():
                shifting = 97 + (ord(value) - 97 + key) % 26 
                print(chr(shifting), end="")

            # checks the range for uppercase letters
         if value.isupper():
                shifting = 65 + (ord(value) - 65 + key) % 26
                
                encrypted_text = chr(shifting)
                
                print(encrypted_text , end="")

                # Adds non-alphabetical characters to the string.
        else:
            encrypted_text = value

            print(encrypted_text, end="")
