#!/bin/bash

#The main difference between the while and until is that while will run
#till the condition is satisfied but the until will run until the condition is not met
#It exits if the condition is true

var1=10
until [ $var1 -eq 0 ]
do 
    echo -n "$var1 "
    var1=$[ var1 - 1 ]
done

#The multiple commands also like the while loop we can use in the until
