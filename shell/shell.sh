#!/usr/bin/env bash

for  file in * ;
do
    if grep -q POSIX $file
    then
        ls -l  $file
        more $file
    fi
done

exit 0

