#!/bin/bash
for dir in ./*/     # list directories in the form "/tmp/dirname/"
do
    #dir=${dir%*/}      # remove the trailing "/"
    pushd ${dir}    # print everything after the final "/"
    nohup python3 analyze.py > res.out &
    popd 
done
