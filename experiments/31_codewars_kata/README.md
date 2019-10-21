01_human readable_time
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    # Test.assert_equals(make_readable(0), "00:00:00")
    # Test.assert_equals(make_readable(5), "00:00:05")
    # Test.assert_equals(make_readable(60), "00:01:00")
    # Test.assert_equals(make_readable(86399), "23:59:59")
    # Test.assert_equals(make_readable(359999), "99:59:59")


02_Josephus_Permutation
    This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.
    Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).
    Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.
    You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of items to be permuted as if they were in a circle and counted out every k places until none remained.
    Tips and notes: it helps to start counting from 1 up to n, instead of the usual range 0..n-1; k will always be >=1.
    For example, with n=7 and k=3 josephus(7,3) should act this way.
        [1,2,3,4,5,6,7] - initial sequence
        [1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
        [1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
        [1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
        [1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
        [1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
        [4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
        [] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]

    # Test.assert_equals(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
    # Test.assert_equals(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
    # Test.assert_equals(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
    # Test.assert_equals(josephus([],3),[])
    # Test.assert_equals(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])

03_catching_car_mileage_number
    We've hacked into car's computer, and we have a box hooked up that reads mileage numbers.
    We've got a box glued to dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).
    Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below),
        a 1 if an interesting number occurs within the next two miles,
        or a 0 if the number is not interesting.

    "Interesting" Numbers
    Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

    Any digit followed by all zeros: 100, 90000
    Every digit is the same number: 1111
    The digits are sequential, incrementing†: 1234
    The digits are sequential, decrementing‡: 4321
    The digits are a palindrome: 1221 or 73837
    The digits match one of the values in the awesome_phrases array
    † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
    ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
