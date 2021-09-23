#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Scale_Profi PC "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Fede PC "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Acce PC "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Reject PC "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit
../res_plotter_gr_dp_3ql_rl.py federation
../res_plotter_gr_dp_3ql_rl.py acceptance
../res_plotter_gr_dp_3ql_rl.py reject

../gap_plotter_gr_dp_3ql_rl.py profit

