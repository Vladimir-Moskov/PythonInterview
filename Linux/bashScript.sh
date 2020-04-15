#!/bin/bash

# this is a comment

echo "Hello from cool bash script!"

# exit code - 0 all is ok, if exit > 0 - there is some error with some code
# exit without any number will return rusult of last command

message="Very important message"
echo $message
echo "I have message for you ${message}"


# what's our file name?
echo "file name: ${0}"

# how many arguments script has
echo "Script has been called with $# arguments"

# what were the arguments
echo "argument 1 = $1, arument 2 = $2, argument 3 = $3 ...."


# if statements
if [[ $# == 0 ]]; then
    echo "where are the arguments!?"
fi

NAME=$1
GREETING="Hi there"
HAT_TIP="*tip of the hat*"
HEAD_SHAKE="*slow head shake*"

if [ "$NAME" == "vova" ]; then
    echo "${GREETING} vova!!!"
elif [ "$NAME" == "vavas" ]; then
    echo "${HAT_TIP} Sup, vavas"
else
    echo "${HEAD_SHAKE} who are you?"
fi



NUM_REQUIRED_ARGS=2

if [[ $# -lt NUM_REQUIRED_ARGS ]]; then
    echo "Nor enough arguments. Call this script with {$0} <name> <name>"
fi

NOT_NULL_VALUE="this is something"
NULL_VALUE=""

if [ -n "$NOT_NULL_VALUE" ]; then
   echo "${NOT_NULL_VALUE} - is not null"
fi

if [ -z "$NULL_VALUE" ]; then
    echo "null/zeroo"
fi

# exit 0