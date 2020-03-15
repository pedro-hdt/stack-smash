# CS3235 - Assignment 2

## Exercise 2 - Format String Attack

The script build_exploit.py automatically generates the file (exploit) 
such that running `./format_string < exploit` causes a shell to be spawned.

To run the attack just use the sequence of commands:
```
make
python3 build_exploit.py
./format_string < exploit
```
