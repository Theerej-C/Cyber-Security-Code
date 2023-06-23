#!/bin/bash

#The while loop is also like the if-else but we should carefully
#give the correct condition or else it will run infinitely.

var1=10
while [ $var1 -gt 0 ]
do
    echo -n "$var1 " 
    var1=$[ $var1 - 1 ]
done

#We can also use the multiple test commands in the while loop

var2=10
var3=20
while [ $var2 -ge 0 ]
      [ $var3 -le 30 ]
do
    echo The values of var2 and var3 are $var2 and $var3
    var2=$[ var2 - 1 ]
    var3=$[ var3 + 1 ]
done