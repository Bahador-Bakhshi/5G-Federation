#!/bin/bash

../../out_to_json_rand_DPs.sh Class_Num_Profi "Class Num"  "Average Profit" profit.json
../../out_to_json_rand_DPs.sh Class_Num_Fede "Class Num" "Federation Rate" federation.json
../../out_to_json_rand_DPs.sh Class_Num_Acce "Class Num" "Acceptance Rate" acceptance.json


../../res_plotter_rand_DPs.py profit
../../res_plotter_rand_DPs.py federation
../../res_plotter_rand_DPs.py acceptance

../../gap_plotter_rand_DPs.py profit

