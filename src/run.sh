#!/bin/bash

# Get integer input from command line
echo "Enter the number of the core on your computer:"
read count

# Run command 'count' number of times
for ((i=1;i<=$count;i++))
do
  # Replace 'command A' with the actual command to be run
  nohup python3 main.py &
done
