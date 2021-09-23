#!/bin/bash

../out_to_json_dp_ql_rl.sh Episode_Profi episode "Average Profit" profit.json
../out_to_json_dp_ql_rl.sh Episode_Fede episode "Federation Rate" federation.json
../out_to_json_dp_ql_rl.sh Episode_Acce episode "Acceptance Rate" acceptance.json


../res_plotter_dp_ql_rl.py profit
../res_plotter_dp_ql_rl.py federation
../res_plotter_dp_ql_rl.py acceptance

../gap_plotter_dp_ql_rl.py profit

