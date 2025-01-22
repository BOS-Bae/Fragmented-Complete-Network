#!/bin/bash

paste c_dist_action_N100_avg.dat c_dist_action_N100_stderr.dat > output_action.dat
paste cumul_action_dist_N100_avg.dat c_dist_action_N100_stderr.dat > output_cumul_action.dat
gnuplot c_dist_plot.gnu
gnuplot cumul_plot.gnu
