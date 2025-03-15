while True:
    try:
        x = int(input("What is X? "))
    except ValueError:
        print("X is not an integer")
    else:
        break

print(f"X is {x}")

# try 块中的变量作用域：变量在 try 块中赋值时，它只在该块内生效。如果发生异常，变量可能不会被定义。
# while 循环中的变量作用域：变量在循环外部定义后，其作用域覆盖整个循环，因此即使在循环内修改它，循环外部也能访问到它。
