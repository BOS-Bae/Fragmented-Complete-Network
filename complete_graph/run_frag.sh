#!/bin/bash

M=$1
ns=$2
nit=$3
N=0

L=$((M+M-1))
for ((i=1; i<=$M; i++))
	do
		N=$((N+i))	
	done

mkdir result_frag_N$N/
mkdir result_frag_N$N/L7
mkdir result_frag_N$N/L8
mkdir result_frag_N$N/L7/num_data
mkdir result_frag_N$N/L8/num_data

rule_num=(7 8)

for ((s=0; s<$ns; s++))
	do
		for r in ${rule_num[@]}
			do
			for ((i=0; i<$L; i++))
				do
					./frag_prob $M $r $i $nit > ./result_frag_N$N/L$r/num_data/idx$i-sample$s.dat
				done
			done
	done
