set terminal pdfcairo size 8, 3
set output "UK.pdf"
set yrange [0.005:1.5]
set xlabel font "Helvetica,40" 
set xtics font "Helvetica,37"
set ylabel font "Helvetica,40" 
set ytics font "Helvetica,40"
set ytics ("10^{-3}" 1e-3, "10^{-2}" 1e-2, "10^{-1}" 1e-1, "10^{0}" 1e-0)
set key font "Helvetica,35"
set log x 
set log y
set xlabel "k"
set ylabel "C(k)"
set label "(b)" at 1.5, 0.03 font "Helvetica, 55"

set style data points
plot "./UK.dat" u ($0+1):1 lc rgb "black" pt 7 ps 1.0  t ""
pause mouse key
