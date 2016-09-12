#!/bin/bash

awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
	}
    }
    
}
END {
    for (i = 1; s[i] != ""; i++) {
	print s[i]
    }
}' file.txt





# Memory Limit Exceeded

# arr1=()
# arr2=()
# i=0
# while read line
# do
#     arr1[$i]=`echo $line | cut -d " " -f 1`
#     arr2[$i]=`echo $line | cut -d " " -f 2`
#     let i=i+1
# done < file.txt

# echo ${arr1[*]}
# echo ${arr2[*]}
