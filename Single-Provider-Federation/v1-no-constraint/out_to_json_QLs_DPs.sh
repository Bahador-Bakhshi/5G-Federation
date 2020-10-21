#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: "$0 "grep_token x_label output"
   exit  
fi

echo $PWD

cat res.out | grep $1 -A 6 | gawk -v x_label="$2" -f ../../out_to_json_QLs_DPs.awk > $3

echo "Remove the last comma!!!"
