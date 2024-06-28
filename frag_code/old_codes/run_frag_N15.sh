#!/bin/bash

#rm result_frag_L7_L8/L7/*
#rm result_frag_L7_L8/L8/*

rule_num=(7 8)
for r in ${rule_num[@]}
	do
	for ((i=0; i<=8; i++))
		do
			./frag_prob_N15 $r $i 10000 >> ./result_frag_N15/L$r/idx$i.dat
		done
	done
