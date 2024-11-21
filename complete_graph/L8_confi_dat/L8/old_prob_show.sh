#!/bin/bash

N=$1
cidx=$2

tr ' ' '\n' < ./flip_dat/prob-N$N-L8-idx$2.dat | sort -n | uniq | paste -sd ' ' -
