#!/bin/bash

../../out_to_json_rand_DPs.sh Multiplier_Profi eta "Average Profit" profit.json
../../out_to_json_rand_DPs.sh Multiplier_Fede eta "Federation Rate" federation.json
../../out_to_json_rand_DPs.sh Multiplier_Acce eta "Acceptance Rate" acceptance.json


../../res_plotter_rand_DPs.py profit
../../res_plotter_rand_DPs.py federation
../../res_plotter_rand_DPs.py acceptance

../../gap_plotter_rand_DPs.py profit

