#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Episode_Profi Episode "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Episode_Fede Episode "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Episode_Acce Episode "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Episode_Reject Episode "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit NO_GREEDY
../res_plotter_gr_dp_3ql_rl.py federation NO_GREEDY
../res_plotter_gr_dp_3ql_rl.py acceptance NO_GREEDY
../res_plotter_gr_dp_3ql_rl.py reject NO_GREEDY
 
../gap_plotter_gr_dp_3ql_rl.py profit NO_GREEDY

