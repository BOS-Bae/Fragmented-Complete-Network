set terminal pdfcairo size 8, 3
set output "three_C_k.pdf"
set yrange [0.005:1.5]
set key font "Helvetica, 30" 
set xlabel font "Helvetica,40" 
set xtics font "Helvetica,37"
set ylabel font "Helvetica,40" 
set ytics font "Helvetica,40"
set key left bottom
set ytics ("10^{-3}" 1e-3, "10^{-2}" 1e-2, "10^{-1}" 1e-1, "10^{0}" 1e-0)
set log x 
set log y
set xlabel "k"
set ylabel "C(k)"

set style data points
plot "./Germany.dat" u ($0+1):1 lc rgb "purple" pt 7 ps 0.8 t "Germany", \
     "./UK.dat" u ($0+1):1 lc rgb "blue" pt 9 ps 0.8 t "UK", \
     "./Spain.dat" u ($0+1):1 lc rgb "green" pt 5 ps 0.8 t "Spain"
pause mouse key
