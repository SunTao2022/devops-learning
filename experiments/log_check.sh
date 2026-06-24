#! /bin/bash

# set -e 
# trap clean_up EXIT

# chean_up(){
#     rm -rf /tmp/temp=dir
# }

for line in $(cat app.log); do 
    result = $(line)
done