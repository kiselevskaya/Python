

def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0
    else:
        def interesting(num):
            lst = list(str(num))
            half_len = len(lst)//2

            if len(str(num)) >= 3:
                # The digits match one of the values in the awesome_phrases array
                if str(num) in awesome_phrases:
                    return True

                # Any digit followed by all zeros: 100, 90000
                if int(lst[0]) in range(1, 10) and num % 10**(len(lst)-1) == 0:
                    return True

                # Every digit is the same number: 1111
                # set(str(number)[1:]) == set('0')
                if len(set(str(num))) == 1 and len(lst) > 2:
                    return True

                # The digits are a palindrome: 1221 or 73837
                # str(number) == str(number)[::-1]
                if lst[:half_len] == lst[-half_len:][::-1]:
                    return True

                # # The digits are sequential, incrementing: 1234
                # For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
                # For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
                if str(num) in '1234567890' or str(num) in '9876543210':
                    return True
            else:
                return False

        def almost_interesting(num):
            if interesting(num+1) or interesting(num+2):
                return True

        if interesting(number):
            return 2
        elif almost_interesting(number):
            return 1
        else:
            return 0
