# xavier
Python bytecode can be alot of fun

Xavier is a fun application showcasing the power of bytecode. 
It is consisted of 2 python files, the xavier.py and the xmlBuilder.py
The xmlBuilder.py creates an xml file containing a stringified bytecode object of a single function.
The xavier.py reads this file and executes the code.
Suppose you run the xmlBuilder on a server and xavier on a client. The client will download the code and execute it without it ever touching the hard disk drive of the client.

Features i would like to implement:
Encrypt/Decrypt the code object
Successfuly load multiple functions at once, or nested functions.
Research if we can explicitly delete the code object from memory after running 

Good luck and have fun. Don't hesitate to contact me for any questions.
