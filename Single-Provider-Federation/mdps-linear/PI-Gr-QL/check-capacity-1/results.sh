#!/bin/bash

../../out_to_json_rand_DPs.sh Capacity_Profi capacity "Average Profit" profit.json
../../out_to_json_rand_DPs.sh Capacity_Fede capacity "Federation Rate" federation.json
../../out_to_json_rand_DPs.sh Capacity_Acce capacity "Acceptance Rate" acceptance.json


../../res_plotter_rand_DPs.py profit
../../res_plotter_rand_DPs.py federation
../../res_plotter_rand_DPs.py acceptance

../../gap_plotter_rand_DPs.py profit

