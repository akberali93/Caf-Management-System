print("=======Number Triangle Pattern======")

rows = int(input("Enter number of rows: "))

num = 2  

for i in range(1, rows + 1):  
    count = 0
    while count < i:        
        is_prime = True

        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    is_prime = False
                    break
        else:
            is_prime = False

        if is_prime:
            print(num, end=" ")
            count += 1
        else:
            pass  

        num += 1

    print() 
