#!/bin/bash

# Get the number of times to run command A from the command line argument
rm ../data/data.csv
num_times=$core

# Loop through and execute command A num_times
for (( i=1; i<=$num_times; i++ ))
do
    echo "run for $i times"
    nohup gui=False python3 main.py >/dev/null 2>&1 &
done


