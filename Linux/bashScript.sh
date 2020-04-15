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

# exit 0