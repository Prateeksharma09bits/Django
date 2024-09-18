# Django
Question 1: Are Django signals executed synchronously or asynchronously by default?
-->By default, Django signals are executed synchronously. This means that when a signal is sent, the connected signal handler functions are called immediately and the code that sent the signal waits for the signal handlers to finish before continuing.
There snippet code will be in file1.py

Question 2: Do Django signals run in the same thread as the caller?
--> Yes, Django signals run in the same thread as the caller unless explicitly offloaded to a different thread or process.
There snippet code will be in file2.py

Question 3: Do Django signals run in the same database transaction as the caller?
-->By default, Django signals run in the same database transaction as the caller, assuming the signal is triggered by a database operation that is part of a transaction.
There snippet code will be in file3.py

# Topic2
Custom Classes in Python
Rectangle Class with Iteration Support
-->You can create a Rectangle class with custom iteration behavior using Python’s __iter__ method. In this case, when iterating over an instance of Rectangle, it first returns the length and then the width.
There snippet code will be in Topic2.py
