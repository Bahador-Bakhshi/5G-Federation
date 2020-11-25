#!/bin/bash

../out_to_json_gr_dp_ql_rl.sh Load_Profi load "Average Profit" profit.json
../out_to_json_gr_dp_ql_rl.sh Load_Fede load "Federation Rate" federation.json
../out_to_json_gr_dp_ql_rl.sh Load_Acce load "Acceptance Rate" acceptance.json


../res_plotter_gr_dp_ql_rl.py profit
../res_plotter_gr_dp_ql_rl.py federation
../res_plotter_gr_dp_ql_rl.py acceptance

../gap_plotter_gr_dp_ql_rl.py profit

