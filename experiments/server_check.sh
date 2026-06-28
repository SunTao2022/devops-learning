#!/bin/sh

if [ "$2" = "running" ]; then
    emoji="✅"
else
    emoji="❌"
fi
echo "Server $1 is $emoji $2"