#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Usage: "$0 "grep_token x_label y_label output"
   exit  
fi

cat res.out | grep $1 -A 10 | gawk -v x_label="$2" -v y_label="$3" -f ../out_to_json_dp_ql_rl.awk > $4

