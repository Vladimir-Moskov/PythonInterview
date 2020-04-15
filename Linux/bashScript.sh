#!/bin/bash

# this is a comment

echo "Hello from cool bash script!"

# exit code - 0 all is ok, if exit > 0 - there is some error with some code
# exit without any number will return rusult of last command

message="Very important message"
echo $message
echo "I have message for you ${message}"

# exit $?