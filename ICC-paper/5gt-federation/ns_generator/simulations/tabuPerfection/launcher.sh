#!/bin/bash - 
#===============================================================================
#
#          FILE: launcher.sh
# 
#         USAGE: ./launcher.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/08/17 11:38
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

VNFS=$(grep vnfs ../../simulation-configs/tabuPerfection/nsBunch.json | grep -oE '[0-9]*')
topIters=6
bottomIters=1
CPUS=8

minIters=1
minBlocks=$(( $VNFS * ($minIters + 1) - 1 ))
blockStep=$VNFS
tasks="simTasks.log"

i=1

# Generate the simmulations' calls
for (( iters = $bottomIters; iters < $topIters + 1; iters++ )); do
    maxBlocks=$(( $VNFS * ($iters-1 + 1) - 1 ))

    for blocks in $( seq $minBlocks $blockStep $(( $maxBlocks + 1 )) ); do
        echo "sim.py tabu greedy Dijkstra d=9 i=$iters b=$blocks &> /tmp/tabuPerfection/tabu-dijkstra-d9-i$iters-b$blocks.log" >> $tasks
        echo "sim.py tabu greedy backtrackingCutoff d=9 i=$iters b=$blocks &> /tmp/tabuPerfection/tabu-dfs-d9-i$iters-b$blocks.log" >> $tasks
        echo "sim.py tabu greedy BFScutoff d=9 i=$iters b=$blocks &> /tmp/tabuPerfection/tabu-bfs-d9-i$iters-b$blocks.log" >> $tasks
    done
done

# Execute them in parallel
cat $tasks | parallel -k -j$CPUS
rm $tasks

