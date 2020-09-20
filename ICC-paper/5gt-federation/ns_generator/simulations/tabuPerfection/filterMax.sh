#!/bin/bash - 
#===============================================================================
#
#          FILE: filterMax.sh
# 
#         USAGE: ./filterMax.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/08/17 19:14
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

dataFile="results/dijkstra.dat"
outFile="results/dijkstraFiltered.dat"

head -n1 $dataFile > $outFile

iterations=$(tail -n1 $dataFile | grep -oe '^[0-9]*')

for (( it = 1; it < $iterations + 1; it++ )); do
    highestSuccess=$(grep "^$it" $dataFile | sort -n -k4 -r | head -n1)
    echo $highestSuccess >> $outFile
done

