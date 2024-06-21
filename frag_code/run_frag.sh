#!/bin/bash

rm result_frag_L7_L8/L7/*
rm result_frag_L7_L8/L8/*

for ((r=7; r<=8; r++))
	do
	for ((i=0; i<=7; i++))
		do
			./frag_prob_L7_L8 $r $i 10000 >> ./result_frag_L7_L8/L$r/idx$i.dat
		done
	done
