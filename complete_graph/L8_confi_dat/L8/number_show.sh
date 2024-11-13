#!/bin/bash

N=$1

tr ' ' '\n' < flip_dat/N$N-L8-flip-paradise.dat | sort -n | uniq | paste -sd ' ' -
