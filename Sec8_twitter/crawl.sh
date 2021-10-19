#!/usr/bin/sh

while read line
do
    python3 get_friends.py $line
done<$1
