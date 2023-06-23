#!/bin/bash

#Here clearly see that I had used bash instead of sh
#This is due to the c like syntax is not available in sh and only in bash
#So if we want to use in sh we can use the while with the counter
#We can also use the normal for loop as a counter and increment or decrement as in C

for (( a=1; a <= 10; a++ ))
do 
    echo The next number is $a
done

#We can also use the multiple variables in the for in c

for (( a=1, b=10; a<=10; a++, b-- ))
do
    (( var2=$b - $a ))
    echo The difference is $var2
done