#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: "$0 "grep_token x_label"
   exit  
fi

cat res.out | grep $1 -A 5 | gawk -v x_label=$2 'BEGIN{FS="="; print "{ \"x_label\":\"" x_label "\", \"results\":["; cnt = 0} {if(length($0) > 2){cnt++; if(cnt == 1) print "{ \"x\":" $2","; else if (cnt == 2) print "\"greedy000\":" $2 ","; else if (cnt == 3) print "\"greedy050\":" $2 ","; else if (cnt == 4) print "\"greedy100\":" $2 ",";  else if (cnt == 5) print "\"DP\":" $2","; else if (cnt == 6) {print "\"QL\":" $2"},"; cnt = 0}}} END{print "]}"}' > res.json

echo "Remove the last comma!!!"
