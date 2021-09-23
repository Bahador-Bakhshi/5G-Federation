#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Threshold_Profi Theta "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Threshold_Fede Theta "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Threshold_Acce Theta "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Threshold_Reject Theta "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit
../res_plotter_gr_dp_3ql_rl.py federation
../res_plotter_gr_dp_3ql_rl.py acceptance
../res_plotter_gr_dp_3ql_rl.py reject

../gap_plotter_gr_dp_3ql_rl.py profit

