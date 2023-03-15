def vaild(text):
    while True:
        x = input(text)
        try:
            nums = int(x)
            if nums < 0  or nums > 2: # check the day is in between 0 to 2 
                x
            elif nums == float: # check for float number
                print("Input in number")
            else:
               break        
        except ValueError: # check for other input like string symbol
            print("Input Invalid")
    return nums