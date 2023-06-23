#!/bin/bash

#We can nest the loops inside one another but should be carefull
#because it can run long

for (( a=1; a<=10; a++ ))
do
    echo This is main loop $a
    for (( b=1; b<=4; b++ ))
    do
        echo This is inside loop $b
    done
done

#Mixed loop commands were also there where you can use another loop inside different loop.

var1=5
file="test.txt"
while [ $var1 -gt 0 ]
do
    echo The outer loop is $var1
    for test in $(cat $file)
    do
        echo The contents are $test
    done
    var1=$[ var1 - 1 ]
done