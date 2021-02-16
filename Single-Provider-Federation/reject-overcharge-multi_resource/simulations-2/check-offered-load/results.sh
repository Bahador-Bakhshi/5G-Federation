#!/bin/bash

../out_to_json_gr_dp_3ql_rl.sh Load_Profi Lambda "AP" profit.json
../out_to_json_gr_dp_3ql_rl.sh Load_Fede Lambda "FR" federation.json
../out_to_json_gr_dp_3ql_rl.sh Load_Acce Lambda "AR" acceptance.json
../out_to_json_gr_dp_3ql_rl.sh Load_Reject  Lambda "RR" reject.json


../res_plotter_gr_dp_3ql_rl.py profit
../res_plotter_gr_dp_3ql_rl.py federation
../res_plotter_gr_dp_3ql_rl.py acceptance
../res_plotter_gr_dp_3ql_rl.py reject

../gap_plotter_gr_dp_3ql_rl.py profit

