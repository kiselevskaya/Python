Count files which has <substring> start with <path> and further, <path> as first task in queue

Create <n> threads.
Threads get tasks from the queue.
Every thread checks if the document is file or directory in the list of directory <path>.
If the document is file and has <substring>, count it.
If the document is directory, put <path/directory> as a new task in the queue.
