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

# CONFIG VARIABLES
STEPS=10
baseDisk=17
baseCpu=17
baseMem=17

# FILE AND PATH VARIABLES
RELPATH=`dirname ${BASH_SOURCE[0]}`
SIMPY="$RELPATH/sim.py"
SETRESPY="$RELPATH/setSimResources.py"
PRINTRESPY="$RELPATH/printSimResources.py"
MULTIDOM_DIR="$RELPATH/../../simulation-configs/resourceReductionMax/multiDomain"


# RESOURCES RETRIEVAL
resources=$(python $PRINTRESPY)
NUMREGEX='[0-9]\+\(\.[0-9]\+\)*'
disk=`echo "$resources" | grep disk | grep -oe $NUMREGEX`
cpu=`echo "$resources" | grep cpu | grep -oe $NUMREGEX`
memory=`echo "$resources" | grep memory | grep -oe $NUMREGEX`
fatBw=`echo "$resources" | grep fatBw | grep -oe $NUMREGEX`
meshBw=`echo "$resources" | grep meshBw | grep -oe $NUMREGEX`

# Put resources as float
disk=`echo "scale=2; $disk / 1" | bc`
cpu=`echo "scale=2; $cpu / 1" | bc`
memory=`echo "scale=2; $memory / 1" | bc`

# PARAMS STEPS
diskStep=`echo "scale=2; ($disk - $baseDisk) / $STEPS" | bc`
cpuStep=`echo "scale=2; ($cpu - $baseCpu) / $STEPS" | bc`
memoryStep=`echo "scale=2; ($memory - $baseMem) / $STEPS" | bc`

# INITIALIZE ITER VARS
currDisk=$disk
currCpu=$cpu
currMem=$memory


# Iterate through different possible resources
while [ $(echo "$currDisk >= $baseDisk" | bc) -gt 0 ]\
    && [ $(echo "$currCpu >= $baseCpu" | bc) -gt 0 ]\
    && [ $(echo "$currMem >= $baseMem" | bc) -gt 0 ];
do
    rm -r $MULTIDOM_DIR
    suffixName="-d=$currDisk-cpu=$currCpu-mem=$currMem.log"
    echo currDisk: $currDisk
    echo currCpu: $currCpu
    echo -e "currMem: $currMem\n"
    
    # Set resources to current ones
    python $SETRESPY $currDisk $currCpu $currMem

    # Launch simulations (first one without & to be the one to write new domain)
    python $SIMPY greedy backtrackingCutoff d=9 > "$RELPATH/results/dfs-dpth9--$suffixName"
    python $SIMPY greedy Dijkstra d=9 > "$RELPATH/results/dijkstra-dpth9--$suffixName" &
    python $SIMPY greedy BFScutoff d=9 > "$RELPATH/results/bfs-dpth9--$suffixName" &
    python $SIMPY tabu greedy Dijkstra d=9 i=5 b=3 > "$RELPATH/results/tabu-dijkstra-dpth=9i=5b=3--$suffixName" &
    wait

    currDisk=`echo "$currDisk - $diskStep" | bc`
    currCpu=`echo "$currCpu - $cpuStep" | bc`
    currMem=`echo "$currMem - $memoryStep" | bc`
done


# Set multiDomain.json back to initial state
`cd $RELPATH && cd ../.. &&\
    cp simulation-configs/resourceReductionMax/multiDomainOrig.json\
     simulation-configs/resourceReductionMax/multiDomain.json`

