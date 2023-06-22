#!/bin/sh

if [ -d $HOME ] && [ -w $HOME/Scripts/ ]
then
  echo "We have Both"
else
  echo "We don't have both"
fi
