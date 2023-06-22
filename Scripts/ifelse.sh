#!/bin/bash

# The main difference in the if statement in the bash is that it works 
# In an if then manner  Example:
# The exit code of the command in if is the matter as it is the one which changes if into true

if pwd
then 
	echo "Worked"
fi

# We can use the grep to find the user presence
# Else is used to send the alternate response when the command result in non zero.

if grep kali /etc/passwd
then 
	echo "It Worked"
else 
	echo "User not found"
fi

# Like python we can use the elif command for an alternate the flow.

if fdssd
then 
	echo "worked"
elif pwd
then
	echo "Elif Worked"
fi

# we can use the test command to test the expressions like test and condition
# But the shell also provides square braces with the spaces example [ condition ]

#Using numeric comparissions involves operators like -eq, -ge, -gt, -le, etc.

val2=4

if [ $val2 -gt 2 ]
then 
	echo "Yes gt than 2"
else
	echo "No"
fi

# The string comparision is little bit tricky because using the > < signs can translated into 
# files so we must use the escape character \

if [ "hello" \> "helloB" ]
then
	echo "String Greater"
else
	echo "String Lesser"
fi

#Then an another exception is that in the shell script the Captitaized letters are lesser
#The small letters are greater 
# But the sort command will use the small as the smaller.

# Then the file comparision is the most important thing in the shell scripting.
# -d for is file and dir, -e check if file exist

#-d file Checks if file exists and is a directory
#-e file Checks if file exists
#-f file Checks if file exists and is a file
#-r file Checks if file exists and is readable
#-s file Checks if file exists and is not empty
#-w file Checks if file exists and is writable
#-x file Checks if file exists and is executable
#-O file Checks if file exists and is owned by the current user
#-G file Checks if file exists and the default group is the same as the 
#current user
#file1 -nt file2 Checks if file1 is newer than file2
#file1 -ot file2 Checks if file1 is older than file2

if [ -d /home/kali ]
then 
	echo "Directory present"
else
	echo "Directory not present"
fi
if [ -f /etc/shadow ]
then
	if [ -r /etc/shadow ]
	then 
		tail /etc/shadow
	else
		echo "No read access"
	fi
else
	echo "File Does not exist"
fi
