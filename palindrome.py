def expand(string, low, high, s):
    # run till `string[low.high]` is not a palindrome
    while low >= 0 and high < len(string) and string[low] == string[high]:
        # push all palindromes into a set
        s.add(string[low: high + 1])

        # Expand in both directions
        low = low - 1
        high = high + 1


def palindrome_more_than_one(my_set: set):
    my_list = []
    for i in my_set:
        if len(i) > 1:
            my_list.append(i)
    return my_list


# Function to find all unique palindromic substrings of a given string
def all_palindromic_substrings(string):
    # create an empty set to store all unique palindromic substrings
    s = set()

    for i in range(len(string)):
        # find all odd length palindrome with `string[i]` as a midpoint
        expand(string, i, i, s)

        # find all even length palindrome with `string[i]` and `string[i+1]`
        # as its midpoints
        expand(string, i, i + 1, s)
    s = palindrome_more_than_one(s)
    return s


def check_if_palindrome(string: str):
    dictionary = {}
    for i in range(len(string)):
        if string[i] in dictionary:
            dictionary[string[i]] += 1
        else:
            dictionary[string[i]] = 1

    tmp_list = []
    for i in dictionary:
        if dictionary[i] % 2 != 0:
            tmp_list.append(i)

    if len(tmp_list) > 1:
        return False
    else:
        return True
