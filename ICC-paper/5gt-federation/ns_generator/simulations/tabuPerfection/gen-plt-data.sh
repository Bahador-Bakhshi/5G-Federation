#!/bin/bash - 
#===============================================================================
#
#          FILE: gen-plt-data.sh
# 
#         USAGE: ./gen-plt-data.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/08/17 16:36
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

VNFS=6
algorithms=(bfs dfs dijkstra)

for algorithm in ${algorithms[@]}; do
    outFile="results/$algorithm.dat"
    echo "iterations blocks improved success" > $outFile
    echo Generating $outFile

    for logFile in $(ls results/tabu-$algorithm*); do
        iters=$(echo $logFile | grep -oe '-i[0-9]*' | grep -oe '[0-9]*')
        blocks=$(echo $logFile | grep -oe '-b[0-9]*' | grep -oe '[0-9]*')
        blocks=$(( ($blocks + 1) / $VNFS - 1 ))
        improved=$(cat $logFile | grep -e 'improved requests' | grep -oe '[0-9]*')
        success=$(cat $logFile | grep -e 'success requests' | grep -oe '[0-9]*')
        requests=$(cat $logFile | grep -e 'NS requests' | grep -oe '[0-9]*')

        successRate=$(echo "$success / $requests * 100" | bc -l | grep -oe '[0-9]*\.[0-9][0-9]')
        improvedRate=$(echo "$improved / $requests * 100" | bc -l | grep -oe '[0-9]*\.[0-9][0-9]')
        
        echo "$iters $blocks $improvedRate $successRate" >> $outFile
        #echo "$iters $blocks $improved $success" >> $outFile
    done
done


