#!/bin/sh

if [ ifelse.sh -nt ifelse1.sh ]
then
	echo "Newer Than"
else
	echo "Older Than"
	if [ ifelse.sh -ot ifelse1.sh ]
	then
		echo "Nested and older than"
	else
		echo "Nested and newer"
	fi
fi
