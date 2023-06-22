#!/bin/bash
echo -n "Hello Boy: "
echo "The Uid is " $UID
echo "The paths are " $PATH
#To define a variable it is easy and straightforward
#But should not leave gaps between equal signs
days=55
echo $days

# We can save the output a command in a file using redirection
# If we want to append new contents then we use >>

date > test.txt

# Then we can send a text file into a command as an input

wc < test.txt
day=$(date +%y%m%d)
echo $day

# We can use the appending << with a param to indicate start and end of individual commands like EOF
# The bc is an simple calculator used to perform float operations and all that things

var2=$(bc<< EOF
scale=4
a1 = 5
a2 = 4
a1+a2
EOF
)

echo $var2
var=$[4*5*6]
echo $var
# We can pipe the output of an command to an input of an another command by |
var1=$(echo "scale=4; 3.44/5"|bc)


echo $var1

# This will show the status of the command we last executed.
echo $?

# We can allocate own exit commands using exit command
# But the exit status should be inside 255


exit 5


