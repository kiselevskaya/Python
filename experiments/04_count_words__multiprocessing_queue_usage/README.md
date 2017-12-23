Count words from list

Divide text into parts and put every part in a queue as a task. Initialize <n> processes. Every process gets the part of the text as a task and compares every word in this part with every word in the list. If there is a coincidence, the counter of this word increase. Put results of every process in a <answer> queue. Running by the <answer> queue get a final count.
