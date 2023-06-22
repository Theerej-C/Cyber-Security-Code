#!/bin/bash

# The for is to iterate in the list of commands of anything
#For last iteration the var we use has the last value
for test in Alabama Alaska Arizona
do
    echo The next state is $test    
done

echo The last value is $test
#The main draw back is it will recognize single quotes like characters 
#and it will consider as a same word so use escape or the "" for the single one
#The double quotes is also used to escape multi words in single word

for test in I don\'t know the place in "this'll" work
do 
    echo The sentences are: $test
done

#We can use a variable to store the list of words and we can append just by reassigining

list="Chennai Mumbai Kolkata Delhi"
list=$list" Bangalore"

for test in $list
do
    echo The main cities are: $test
done

#We can also read the output of an command and iterate over it
#This is known as the command substitution in the .sh '()'
file="../Linux/test.txt"

for test in $(cat $file)
do
    echo The contents are: $test
done

#The for loop take the space as the field seperator dur to Internal Field Seperator(IFS)
#The best practicse in ifs change is to change the IFS after we needed by storing the value
#any character can be used as an field seperator.
#If we want to have multiple then we can string them together in the double quotes.

oldIfs=$IFS
IFS=$'\n'
for test in $(ls -la)
do
    echo The field seperator is newline so: $test
done
IFS=$oldIfs

#Without the command substitution we can use the file globbing to iterate a dir
#Here in the if statement we used the double quotes this is due to the multistring filenames
for file in /home/kali/Downloads/*
do
    if [ -d "$file" ]
    then   
        echo $file is a directory
    else
        echo $file is a file
    fi
done

#We can use the both the listing and dir methods at same time
#Then we should be cautious in the non existance of the files and folders
# The for will consider the non existance also in consideration
# So we should first check the file before we use that so that we can know it
for file in /home/kali/Downloads/* /home/kali/Scripts/*
do 
    if [ -d "$file" ] && [[ "$file" == /home/kali/Dow* ]]
    then
        echo The dir for Downloads "$file"
    elif [[ "$file" == /home/kali/Scr* ]]
    then 
        echo The file in Scripts "$file"
    else
        echo none
    fi
done

#So the for can be tricky so that we should use in carefully

