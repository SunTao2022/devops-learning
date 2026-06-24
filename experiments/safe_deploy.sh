#! /bin/bash



clean_up(){
    rm -rf /tmp/test-deploy
    echo "clean up done"
    }

trap clean_up EXIT


set -e
mkdir /tmp/test-deploy
cd /tmp/test-deploy
echo "done"




