#!/bin/bash

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -k1 -r -n | awk '{print $2" "$1}'
