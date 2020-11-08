#!/bin/bash

../../out_to_json_rand_DPs.sh Scale_Profi zeta "Average Profit" profit.json
../../out_to_json_rand_DPs.sh Scale_Fede zeta "Federation Rate" federation.json
../../out_to_json_rand_DPs.sh Scale_Acce zeta "Acceptance Rate" acceptance.json


../../res_plotter_rand_DPs.py profit
../../res_plotter_rand_DPs.py federation
../../res_plotter_rand_DPs.py acceptance

../../gap_plotter_rand_DPs.py profit

