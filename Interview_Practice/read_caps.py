FILE = "file.txt"

with open(FILE) as fh:
    count = 0
    
    #Try #1 - most verbose
    # for line in fh:
    #     for char in line:
    #         if char.isupper():
    #             count += 1

    # print("Count of uppercase letters is: ", count)

    #Try #2, a bit more condensed
    # for line in fh:
    #     for char in line:
    #         count += (1 if char.isupper() else 0)
    
    # print("Count of uppercase letters is: ", count)

    #Actual 'one-liner'
    count = sum(1 for line in fh for char in line if char.isupper())

    print("Count of uppercase letters is: ", count)