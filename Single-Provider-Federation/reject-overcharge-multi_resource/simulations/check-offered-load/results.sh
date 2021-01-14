#!/bin/bash

../out_to_json_gr_dp_2ql_rl.sh Load_Profi l "Average Profit" profit.json
../out_to_json_gr_dp_2ql_rl.sh Load_Fede l "Federation Rate" federation.json
../out_to_json_gr_dp_2ql_rl.sh Load_Acce l "Acceptance Rate" acceptance.json
../out_to_json_gr_dp_2ql_rl.sh Load_Reject l "Acceptance Rate" reject.json


../res_plotter_gr_dp_2ql_rl.py profit
../res_plotter_gr_dp_2ql_rl.py federation
../res_plotter_gr_dp_2ql_rl.py acceptance
../res_plotter_gr_dp_2ql_rl.py reject

../gap_plotter_gr_dp_2ql_rl.py profit

