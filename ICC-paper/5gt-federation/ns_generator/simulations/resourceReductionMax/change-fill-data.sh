#!/bin/bash - 
#===============================================================================
#
#          FILE: change-fill-data.sh
# 
#         USAGE: ./change-fill-data.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 16/08/17 16:16
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

DATA_ORIG='results/results.dat'
NEW_DATA='results/fillResults.dat'
dataLines=`cat $DATA_ORIG | wc -l`
data=`tail -n$(( dataLines - 1)) $DATA_ORIG`

currMin=''
currMax=''
currStep=0

echo "step middle minAccept maxAccept" > $NEW_DATA


while read -r dataLine; do
    step=`echo $dataLine | grep -oe '^[0-9]\+'`
    accepted=`echo $dataLine | cut -f3 -d' '`

    if [ $currStep -ne $step ]; then
        if [ $currStep -ne 0 ]; then
            middle=`echo "scale=2; ($currMin + $currMax) / 2" | bc`
            echo "$currStep $middle $currMin $currMax" >> $NEW_DATA
        fi
        currStep=$step
        currMin=$accepted
        currMax=$accepted
    elif [ $accepted -gt $currMax ]; then
        currMax=$accepted
    elif [ $accepted -lt $currMin ]; then
        currMin=$accepted
    fi
done <<< "$data"

