# CS3235 - Assignment 2

## Exercise 2 - Format String Attack

The script build_exploit.py automatically generates the file (exploit) 
such that running `./format_string < exploit` causes a shell to be spawned.

To run the attack just use the sequence of commands, replacing <FILENAME> by the
name of the file to leak. Note that it be at most 55 characters long.
```
make
python3 build_exploit.py <FILENAME>
echo -ne 'run\n-1' | gdb rop
```

### Limitations

Please note that this exploit can only print complete files if their size is up 
to 24576 bytes. For larger files, one could use the buffer iteratively by and
print a chunk of up to 24576 bytes at a time. For the purpose of this exercise
it seems unnecessary to implement such solution.
