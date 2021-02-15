#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Scale_Profi FC "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Fede FC "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Acce FC "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Scale_Reject FC "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit
../res_plotter_gr_dp_3ql_rl.py federation
../res_plotter_gr_dp_3ql_rl.py acceptance
../res_plotter_gr_dp_3ql_rl.py reject

../gap_plotter_gr_dp_3ql_rl.py profit

