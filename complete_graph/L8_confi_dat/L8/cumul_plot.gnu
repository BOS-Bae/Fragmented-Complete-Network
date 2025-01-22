set terminal pdfcairo size 8, 3
set output "output2.pdf"

set xtics font "Helvetica,27"
set ytics font "Helvetica,25"
set log x 
set log y
set ytics ("10^{-6}" 1e-6, "10^{-5}" 1e-5, "10^{-4}" 1e-4, "10^{-3}" 1e-3, "10^{-2}" 1e-2, "10^{-1}" 1e-1)
set lmargin 10
set rmargin 5
set xrange [1:100]
set yrange [0.000001:0.65]
set style line 1 lt 1 lw 2 ps 2 linecolor rgb "black"

set style data points
set key right top
plot "./output_cumul_action.dat" u ($0+1):1:2 w yerrorbars lw 1.5 lc rgb "black" pt 7 ps 1.0  t "", \
	 '' u ($0+1):1 w lines lw 2 lc rgb "black" t ""

pause mouse key
