#!/bin/sh
 status=$1


if [ "$status" = "running" ]; then
    echo "✅ Server is running"
elif [ "$status" = "stopped" ]; then
    echo "❌ Server is stopped"
else
    echo "❓ Server is unknow"
fi
