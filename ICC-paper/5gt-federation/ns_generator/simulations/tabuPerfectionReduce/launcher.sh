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
#       CREATED: 14/08/17 19:13
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

# FILE AND PATH VARIABLES
RELPATH=`dirname ${BASH_SOURCE[0]}`
SIMPY="$RELPATH/sim.py"
SETRESPY="$RELPATH/setSimResources.py"
PRINTRESPY="$RELPATH/printSimResources.py"
MULTIDOM_DIR="$RELPATH/../../simulation-configs/tabuPerfectionReduce/multiDomain"
VNFS=`grep vnfs $RELPATH/../../simulation-configs/tabuPerfectionReduce/nsBunch.json | grep -oE '[0-9]*'`


# --- Resources steps ---
# ORIGINAL FROM TABU PERFECTION EXPERIMENT:
# disk: 190
# cpu: 65
# memory: 200
# fatBw: 1024000
# meshBw: 23040
#-----------------
# disk: 200
# cpu: 200
# memory: 200
# fatBw: 5000
# meshBw: 9000

declare -a disks
declare -a cpus
declare -a memories
disks=(400 200)
cpus=(400 200)
memories=(400 200)
fatBws=(10000 5000)
meshBws=(18000 9000)

# Best tabu params settings
dfsIters=6
dfsBlocks=4
bfsIters=6
bfsBlocks=2
dijIters=5
dijBlocks=3


# Iterate through different possible resources
for (( i = 0; i < ${#disks}; i++ )); do
    rm -r $MULTIDOM_DIR
    suffixName="-d=${disks[i]}-cpu=${cpus[i]}-mem=${memories[i]}.log"
    echo disks: ${disks[@]}
    echo i: $i
    echo currDisk: ${disks[i]}
    echo currCpu: ${cpus[i]}
    echo -e "currMem: ${memories[i]}\n"
    
    # Set resources to current ones
    python $SETRESPY ${disks[i]} ${cpus[i]} ${memories[i]} ${fatBws[i]} ${meshBws[i]}

    # Calc number of blockings
    dfsBlk=$(( $VNFS * ($dfsBlocks + 1) - 1 ))
    bfsBlk=$(( $VNFS * ($bfsBlocks + 1) - 1 ))
    dijBlk=$(( $VNFS * ($dijBlocks + 1) - 1 ))

    # Launch simulations (first one without & to be the one to write new domain)
    python $SIMPY tabu greedy backtrackingCutoff d=9 i=6 b=$dfsBlk > "$RELPATH/results/tabu-dfs-dpth=9i=6b=$dfsBlk--$suffixName" &
    python $SIMPY tabu greedy BFScutoff d=9 i=6 b=$bfsBlk > "$RELPATH/results/tabu-bfs-dpth=9i=6b=$bfsBlk--$suffixName" &
    python $SIMPY tabu greedy Dijkstra d=9 i=5 b=$dijBlk > "$RELPATH/results/tabu-dijkstra-dpth=9i=5b=$dijBlk--$suffixName" &
    wait
done


# Set multiDomain.json back to initial state
`cd $RELPATH && cd ../.. &&\
    cp simulation-configs/tabuPerfectionReduce/multiDomainOrig.json\
     simulation-configs/tabuPerfectionReduce/multiDomain.json`

