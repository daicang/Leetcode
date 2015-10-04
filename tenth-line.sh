#!/bin/bash

i=0
cat tenth-line.sh | while read line
do
    let i=$i+1
    if [ $i -eq 10 ]
    then
	echo $line
    fi
done
