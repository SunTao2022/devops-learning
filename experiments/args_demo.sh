#!/bin/bash
ARGS=$(getopt -o f:v --long file:,verbose -n "$0" -- "$@")
eval set -- "$ARGS"

while true; do
    case "$1" in
        -f|--file)      echo "file to be read"; shift 2 ;;
        -v|--verbose)   echo "Verbose"; shift ;;
        --)             shift; break ;;
        *)              echo "Unknown"; exit 1 ;;
    esac
done


