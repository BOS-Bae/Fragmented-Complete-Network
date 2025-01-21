set terminal pdfcairo size 7, 4.5
set output "./Rm14.pdf"

set xlabel "m"
set ylabel "R(14,n)"
set xlabel font "Helvetica, 30"
set ylabel font "Helvetica, 30"
set xtics font "Helvetica,27"
set ytics font "Helvetica,27"
set ytics (0.0024, 0.0026, 0.0028, 0.003, 0.0032, 0.0034)

set lmargin 10
set rmargin 5
set xrange [0:15]
set style line 1 lt 1 lw 2 ps 2 linecolor rgb "black"

set style data points
set key right top
plot "../R_m14.dat" u 1:($3 > 0 ? $3 : 1/0):4 w yerrorbars lw 2.5 lc rgb "black" pt 7 ps 0.7  t "", \
	 '' u 1:($3 > 0 ? $3 : 1/0) w lines lw 2 lc rgb "black" t "", \
	 '' u 1:($2 > 0 ? $2 : 1/0) w lp lc rgb "green" dt 2 lw 2.5 pt 7 ps 0.7  t ""

pause mouse key
