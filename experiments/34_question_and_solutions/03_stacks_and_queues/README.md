** Stacks and Queues**


stack.py

    LIFO(last-in first-out) ordering


list_as_stacks.py

    Describe how you could use a single array to implement three stacks.


list_as_stacks_flexible.py

    Describe how you could use a single array to implement three stacks.

    This approach allow the stack blocks to be flexible in size.
    When one stack exceeds its initial capacity, we grow the allowable capacity and shift elements as necessary.
    Also design array to be circular, such that the final stack may start at the end of the array and wrap to the beginning.


stack_with_min.py

    Design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
    Push, pop and min should all operate in O(1) time.


set_of_stacks.py

    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would like to start a new stack when the previous stack exceeds some threshold.
    Implement a data structure SetOfStacks that mimics this.
    SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single to a single stack
     (that is, pop() should return the same value as it would if there were just a single stack).

    FOLLOW UP

    Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
