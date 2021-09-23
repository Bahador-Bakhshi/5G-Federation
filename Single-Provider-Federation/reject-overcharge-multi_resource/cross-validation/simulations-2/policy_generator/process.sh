#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Specify file name"
	exit
fi

in_file=$1
out_file="$1-proc"

echo "l1, l2, f1, f2, a1, a2, action" > $out_file
cat $in_file | sed 's/,/ /g' | sed 's/\[(//g' | sed 's/)(/ /g' | sed 's/)\]//g' | sed 's/(/ /g' | sed 's/)//g' | sed 's/://g' | sed 's/Actions.//' | sed 's/  / /g' | sed 's/  / /g' | sed 's/ /,/g' >> $out_file
