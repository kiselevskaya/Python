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

                04_smallest_code_interpreter
                    Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions
                        (the machine memory or 'data' should behave like a potentially infinite array of bytes, initialized to 0):

                    > increment the data pointer (to point to the next cell to the right).
                    < decrement the data pointer (to point to the next cell to the left).
                    + increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
                    - decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
                    . output the byte at the data pointer.
                    , accept one byte of input, storing its value in the byte at the data pointer.
                    [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
                    ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
                    The function will take in input...

                    the program code, a string with the sequence of machine instructions,
                    the program input, a string, eventually empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
                    ... and will return ...

                    the output of the interpreted code (always as a string), produced by the . instruction.

05_decimal_to_factorial_and_back
    Coding decimal numbers with factorials is a way of writing out numbers in a base system that depends on factorials, rather than powers of numbers.
    In this system, the last digit is always 0 and is in base 0!.
    The digit before that is either 0 or 1 and is in base 1!. The digit before that is either 0, 1, or 2 and is in base 2!.
    More generally, the nth-to-last digit is always 0, 1, 2, ..., or n and is in base n!.
    Example :
        decimal number 463 is coded as "341010":
        463 (base 10) = 3×5! + 4×4! + 1×3! + 0×2! + 1×1! + 0×0!
    If we are limited to digits 0...9 the biggest number we can code is 10! - 1.
    So we extend 0..9 with letters A to Z. With these 36 digits we can code up to
        36! − 1 = 37199332678990121746799944815083519999999910 (base 10)
    We will code two functions. The first one will code a decimal number and return a string with the factorial representation : dec2FactString(nb)
    The second one will decode a string with a factorial representation and produce the decimal representation : factString2Dec(str).
    Given numbers will be positive.
    Note
        You have tests with Big Integers in Clojure, Julia, Python, Ruby, Haskell, Ocaml, Racket but not with Java and others where the number "nb" in "dec2FactString(nb)" is at most a long.

06_going_to_zero_or_to_infinity
    Consider the following numbers (where n! is factorial(n)):
        u1 = (1 / 1!) * (1!)
        u2 = (1 / 2!) * (1! + 2!)
        u3 = (1 / 3!) * (1! + 2! + 3!)
        un = (1 / n!) * (1! + 2! + 3! + ... + n!)
    Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?
    Are these numbers going to 0 because of 1/n! or to infinity due to the sum of factorials or to another number?
    Task
    Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n, where n is an integer greater or equal to 1.
    To avoid discussions about rounding, return the result truncated to 6 decimal places, for example:
        1.0000989217538616 will be truncated to 1.000098
        1.2125000000000001 will be truncated to 1.2125

07_connect_four
    https://en.wikipedia.org/wiki/Connect_Four

08_binary_multiple_of_3
    In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.
    Take into account that:
        An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
    The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
    There might be leading 0s.
    Examples (Javascript)
        multipleof3Regex.test('000') should be true
        multipleof3Regex.test('001') should be false
        multipleof3Regex.test('011') should be true
        multipleof3Regex.test('110') should be true
        multipleof3Regex.test(' abc ') should be false
    Note
        There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number.
    You might want to check an example of an automata for doing this same particular task here.
    (https://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three)
        If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.

09_the_greatest_warrior
    Create a class called Warrior which calculates and keeps track of their level and skills, and ranks them as the warrior they've proven to be.

    Business Rules:

    A warrior starts at level 1 and can progress all the way to 100.
    A warrior starts at rank "Pushover" and can progress all the way to "Greatest".
    The only acceptable range of rank values is "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest".
    Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
    With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
    The experience earned from the battle is relative to what the warrior's current level is compared to the level of the enemy.
    A warrior's experience starts from 100. Each time the warrior's experience increases by another 100, the warrior's level rises to the next level.
    A warrior's experience is cumulative, and does not reset with each rise of level. The only exception is when the warrior reaches level 100, with which the experience stops at 10000
    At every 10 levels, your warrior will reach a new rank tier. (ex. levels 1-9 falls within "Pushover" tier, levels 80-89 fall within "Champion" tier, etc.)
    A warrior cannot progress beyond level 100 and rank "Greatest".
    Battle Progress Rules & Calculations:

    If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return "Invalid level".
    Completing a battle against an enemy with the same level as your warrior will be worth 10 experience points.
    Completing a battle against an enemy who is one level lower than your warrior will be worth 5 experience points.
    Completing a battle against an enemy who is two levels lower or more than your warrior will give 0 experience points.
    Completing a battle against an enemy who is one level higher or more than your warrior will accelarate your experience gaining. The greater the difference between levels, the more experinece your warrior will gain. The formula is 20 * diff * diff where diff equals the difference in levels between the enemy and your warrior.
    However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot fight against an enemy that strong and must instead return "You've been defeated".
    Every successful battle will also return one of three responses: "Easy fight", "A good fight", "An intense fight". Return "Easy fight" if your warrior is 2 or more levels higher than your enemy's level. Return "A good fight" if your warrior is either 1 level higher or equal to your enemy's level. Return "An intense fight" if your warrior's level is lower than the enemy's level.
    Logic Examples:

    If a warrior level 1 fights an enemy level 1, they will receive 10 experience points.
    If a warrior level 1 fights an enemy level 3, they will receive 80 experience points.
    If a warrior level 5 fights an enemy level 4, they will receive 5 experience points.
    If a warrior level 3 fights an enemy level 9, they will receive 720 experience points, resulting in the warrior rising up by at least 7 levels.
    If a warrior level 8 fights an enemy level 13, they will receive 0 experience points and return "You've been defeated". (Remember, difference in rank & enemy level being 5 levels higher or more must be established for this.)
    If a warrior level 6 fights an enemy level 2, they will receive 0 experience points.
    Training Rules & Calculations:

    In addition to earning experience point from battles, warriors can also gain experience points from training.
    Training will accept an array of three elements (except in java where you'll get 3 separated arguments): the description, the experience points your warrior earns, and the minimum level requirement.
    If the warrior's level meets the minimum level requirement, the warrior will receive the experience points from it and store the description of the training. It should end up returning that description as well.
    If the warrior's level does not meet the minimum level requirement, the warrior doesn not receive the experience points and description and instead returns "Not strong enough", without any archiving of the result.

    Code Examples:
    
    bruce_lee = Warrior()
    bruce_lee.level         # => 1
    bruce_lee.experience    # => 100
    bruce_lee.rank          # => "Pushover"
    bruce_lee.achievements  # => []
    bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
    bruce_lee.experience    # => 9100
    bruce_lee.level         # => 91
    bruce_lee.rank          # => "Master"
    bruce_lee.battle(90)    # => "A good fight"
    bruce_lee.experience    # => 9105
    bruce_lee.achievements  # => ["Defeated Chuck Norris"]

10_shortest_knight_path
    Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.
    The knight is not allowed to move off the board. The board is 8x8.
    For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
    For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
    (Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)

11_sum_of_intervals
    Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
        Intervals
    Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
        Overlapping Intervals
    List containing overlapping intervals: [[1,4], [7, 10], [3, 5]]
    The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
    Examples:
        sumIntervals( [
           [1,2],
           [6, 10],
           [11, 15]
        ] ); // => 9

        sumIntervals( [
           [1,5],
           [10, 20],
           [1, 6],
           [16, 19],
           [5, 11]
        ] ); // => 19

12_the_learning_game - Machine Learning #1
    Growing up you would have learnt a lot of things like not to stand in fire, to drink food and eat water and not to jump off very tall things But Machines have it difficult they cannot learn for themselves we have to tell them what to do, why don't we give them a chance to learn it for themselves?
        Task
    Your task is to finish the Machine object. What the machine object must do is learn from its mistakes! The Machine will be given a command and a number you will return a random action. After the command has returned you will be given a response (true/false) if the response is true then you have done good, if the response is false then the action was a bad one. You must program the machine to learn to apply an action to a given command using the reponse given. Note: It must take no more than 20 times to teach an action to a command also different commands can have the same action.
        Info
    In the preloaded section there is a constant called ACTIONS it is a function that returns the 5 possible actions.
    In Java, this a constant Actions.FUNCTIONS of type List<Function<Integer, Integer>>.
    In C++, the actions can be accessed by get_action(i)(unsigned int num) where i chooses the function (and therefore can range from 0 to 4) and num is its argument.
    In python ACTIONS() returns a list of lambdas.
    In Golang Actions() retruns a function slice []func(int) int
