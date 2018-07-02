#!/bin/bash
for i in 1 2 3 4 5
do
echo "Starting to program $i"
dd if=/path/to/image of=/dev/sd$i bs=1M
echo "We have completed $i"
done
