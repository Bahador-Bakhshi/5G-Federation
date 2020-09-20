#!/bin/bash - 
#===============================================================================
#
#          FILE: gen-cdfs.sh
# 
#         USAGE: ./gen-cdfs.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 29/08/17 12:44
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

RELPATH=`dirname ${BASH_SOURCE[0]}`
RESULTS=$RELPATH/results

for result in `ls $RESULTS/*.log`; do
    cdfFile=`echo $result | sed -E 's/log/cdf/'`
    ./$RELPATH/getCDF.sh $result  $cdfFile
done




