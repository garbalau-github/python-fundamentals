"""
Process: A process is an instance of a program (e.g. Jupyter Notebook).

+ Takes advantage of multiple CPUs and cores.
+ Separate memory space -> Memory is not shared between processes.
+ Great for CPU-bound processing.
+ New process is started independently from other processes.
+ Processes are interruptable / killable.
+ One GIL (Global interpreter lock) for each process, so it's safer.

- Heavyweight.
- Starting a process is slower than starting a thread.
- More memory.
- IPC (inter-process communication) is more complicated.

"""

"""
Thread: A thread is an entity within a process that can be scheduled (also known as "lightweight process").

+ All threads within a process share the same memory.
+ Lightweight.
+ Starting a thread is faster than starting a process.
+ Great for I/O-bound tasks.

- Threading is limited by GIL: Only one thread at a time.
- No effect for CPU-bound tasks.
- Not interruptable / killable.
- Careful with race conditions: Locking is required.

"""

"""
GIL: Global interpreter lock

A lock that allows only one thread at a time to execute in Python.
Needed in CPython because memory management is not thread-safe.

Avoid:
- Use multiprocessing.
- Use a different, free-threaded Python implementation (Jython, IronPython).
- Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy.

"""
