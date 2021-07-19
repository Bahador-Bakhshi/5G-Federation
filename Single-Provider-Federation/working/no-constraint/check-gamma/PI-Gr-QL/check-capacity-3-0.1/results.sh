#!/bin/bash

../../out_to_json_gr_dp_ql_rl.sh Capacity_Profi capacity "Average Profit" profit.json
../../out_to_json_gr_dp_ql_rl.sh Capacity_Fede capacity "Federation Rate" federation.json
../../out_to_json_gr_dp_ql_rl.sh Capacity_Acce capacity "Acceptance Rate" acceptance.json


../../res_plotter_gr_dp_ql_rl.py profit
../../res_plotter_gr_dp_ql_rl.py federation
../../res_plotter_gr_dp_ql_rl.py acceptance

../../gap_plotter_gr_dp_ql_rl.py profit

