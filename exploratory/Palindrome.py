def isPalindrome(input_value):
    input_array = list(input_value)
    i = 0
    j = len(input_array) - 1
    while i != j and j > i:
        if input_array[i] != input_array[j]:
            return False
        i = i + 1
        j = j - 1
    return True


test = 'ZuiuZ'
print(isPalindrome(test))
