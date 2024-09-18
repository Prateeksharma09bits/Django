# Django
Question 1: Are Django signals executed synchronously or asynchronously by default?

By default, Django signals are executed synchronously. This means that when a signal is sent, the connected signal handler functions are called immediately and the code that sent the signal waits for the signal handlers to finish before continuing.

There snippet code will be in file1

