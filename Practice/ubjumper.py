

while(True):
    x = input()
    if x == "STOP":
        break
    nums = list(map(int, x.split()))

    abs_value = []
    for i in range(len(nums)-1):
        abs_value.append(abs(nums[i]-nums[i+1]))

    is_ub_jumper = True
    for i in range(1, len(nums)):
        if i not in abs_value:
            is_ub_jumper = False
            break
    if is_ub_jumper:
        print("UB Jumper")
    else:
        print("Not UB Jumper")
    
        
    