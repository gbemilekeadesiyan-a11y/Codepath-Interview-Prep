def doubled(lst):
    for item in lst:
        if not isinstance(item, (int, float)):
            print(f"Skipping '{item}' - not a number")
        elif item == 0:
            print("0 doubles to 0")
        else:
            print(item * 2)    