#!/bin/bash

../out_to_json_gr_dp_2ql_rl.sh Scale_Profit LC "Average Profit" profit.json
../out_to_json_gr_dp_2ql_rl.sh Scale_Fede LC "Federation Rate" federation.json
../out_to_json_gr_dp_2ql_rl.sh Scale_Acce LC "Acceptance Rate" acceptance.json
../out_to_json_gr_dp_2ql_rl.sh Scale_Reject LC "Rejection Rate" reject.json


../res_plotter_gr_dp_2ql_rl.py profit
../res_plotter_gr_dp_2ql_rl.py federation
../res_plotter_gr_dp_2ql_rl.py acceptance
../res_plotter_gr_dp_2ql_rl.py reject

../gap_plotter_gr_dp_2ql_rl.py profit

