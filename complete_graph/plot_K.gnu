set terminal pdf
set output "K_kmax.pdf"

set xlabel font "Helvetica,30" 
set xtics font "Helvetica,27"
set ylabel font "Helvetica,30" 
set ytics font "Helvetica,27"

set xlabel "1/k_{max}"
set ylabel "K"
set xrange [0:1.0]
set yrange [0:100]

set style data points
set key right top
plot "Mathematica_K_L8.dat" u (1/$1):2 w lp lc rgb "black" pt 7 ps 1.0 lw 3 t ""

