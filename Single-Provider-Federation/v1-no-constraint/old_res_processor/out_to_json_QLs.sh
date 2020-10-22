#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: "$0 "grep_token x_label"
   exit  
fi

cat res.out | grep $1 -A 3 | gawk -v x_label=$2 'BEGIN{FS="="; print "{ \"x_label\":\"" x_label "\", \"results\":["; cnt = 0} {if(length($0) > 2){cnt++; if(cnt == 1) print "{ \"x\":" $2","; else if (cnt == 2) print "\"DP\":" $2 ","; else if (cnt == 3) print "\"QL-Dynamic\":" $2 ","; else if (cnt == 4) {print "\"QL-Static\":" $2 "},"; cnt = 0}}} END{print "]}"}' > res.json

echo "Remove the last comma!!!"
