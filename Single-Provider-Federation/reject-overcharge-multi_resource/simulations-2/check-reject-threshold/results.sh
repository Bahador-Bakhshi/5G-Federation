#!/bin/bash

../out_to_json_gr_dp_2ql_rl.sh Threshold_Profi PC "Average Profit" profit.json
../out_to_json_gr_dp_2ql_rl.sh Threshold_Fede PC "Federation Rate" federation.json
../out_to_json_gr_dp_2ql_rl.sh Threshold_Acce PC "Acceptance Rate" acceptance.json
../out_to_json_gr_dp_2ql_rl.sh Threshold_Reject PC "Rejection Rate" reject.json


../res_plotter_gr_dp_2ql_rl.py profit
../res_plotter_gr_dp_2ql_rl.py federation
../res_plotter_gr_dp_2ql_rl.py acceptance
../res_plotter_gr_dp_2ql_rl.py reject

../gap_plotter_gr_dp_2ql_rl.py profit
