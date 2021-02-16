#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Overcharge_Profi Omega "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Overcharge_Fede Omega "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Overcharge_Acce Omega "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Overcharge_Reject Omega "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit
../res_plotter_gr_dp_3ql_rl.py federation
../res_plotter_gr_dp_3ql_rl.py acceptance
../res_plotter_gr_dp_3ql_rl.py reject

../gap_plotter_gr_dp_3ql_rl.py profit

