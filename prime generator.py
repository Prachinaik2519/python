t = int(input("Enter number of test cases(<=10)"))
for test in range(0,t):
    if t<=10:
        m = int(input("\nEnter lower range: "))
        n = int(input("Enter upper range: "))
        if m >= 1 and n <= 1000000000 and n - m <= 100000:
            for num in range(m,n+ 1):
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            break
                    else:
                        print(num,end=" ")
        else:
            print("Invalid input")
© 2020 GitHub, Inc.
