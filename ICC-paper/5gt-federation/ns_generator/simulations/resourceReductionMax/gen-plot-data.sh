#!/bin/bash - 
#===============================================================================
#
#          FILE: gen-plot-data.sh
# 
#         USAGE: ./gen-plot-data.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 15/08/17 11:26
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

RES_DIR='results'
PLOTF="$RES_DIR/results.dat"
disks=''

DFS_PRFX="$RES_DIR/dfs-dpth9---"
BFS_PRFX="$RES_DIR/bfs-dpth9---"
DIJK_PRFX="$RES_DIR/dijkstra-dpth9---"
TABU_DIJK_PRFX="$RES_DIR/tabu-dijkstra-dpth=9i=5b=3---"



#################################################################
# Yields the plot line based on the simulation file
# args:
#   $1: log file prefix
#   $2: disk ammount
#   $3: algorithm name
# returns:
#   "$step algorithm $accepted $improved $time $disk $mem $cpu"
#################################################################
yieldOutput () {
    local PRFX=$1
    local disk=$2
    local alg=$3

    local file=`ls "$PRFX"d="$disk"*`
    local mem=`ls $file | grep -oe 'mem=[0-9]*' | grep -oe '[0-9]*'`
    local cpu=`ls $file | grep -oe 'cpu=[0-9]*' | grep -oe '[0-9]*'`
    local improved=`grep improved $file | grep -oe '[0-9]*'`
    local accepted=`grep success $file | grep -oe '[0-9]*'`
    local time=`grep -e 'ellapsed time' $file | grep -oe '[0-9]*\(\.[0-9]*\)*'`

    echo "$step $alg $accepted $improved $time $disk $mem $cpu"
}


# Retrieve disk sizes
for simulation in `ls results | grep -e '^dfs'`; do
    disk=`echo $simulation | grep -oe 'd=[0-9]*\(\.[0-9]*\)*' | grep -oe '[0-9]*\(\.[0-9]*\)*'`

    if [ -z $disks ]; then
        disks=$disk
    else
        disks="$disks\n$disk"
    fi
done


sortedDisks=`echo -e "$disks" | sort -n -r`

# Generate file to be plotted
echo "step algorithm accepted improved time disk memory cpu" > $PLOTF
step=1
for disk in `echo -e "$sortedDisks"`; do
    echo "printing for disk: $disk"

    # Plotting data retrieval
    yieldOutput $DFS_PRFX $disk dfs >> $PLOTF
    yieldOutput $BFS_PRFX $disk bfs >> $PLOTF
    yieldOutput $DIJK_PRFX $disk dijkstra >> $PLOTF
    yieldOutput $TABU_DIJK_PRFX $disk tabuDijkstra >> $PLOTF

    (( step += 1 ))
done

