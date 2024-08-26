set title font "Helvetica,20"
set xtics font "Helvetica,15"
set ytics font "Helvetica,15"
set key font "Helvetica,14"
set key left top

set xrange [0.1:1]

set title "L8, 50 MC samples"
p "fixation_L8_N23.dat" u 1:2:3 w yerrorbars t "" ls 1, \
	'' u 1:2 w lp t "N=23" ls 1, \
	"fixation_L8_N21.dat" u 1:2:3 w yerrorbars t "" ls 2, \
	'' u 1:2 w lp t "N=21" ls 2, \
	"fixation_L8_N19.dat" u 1:2:3 w yerrorbars t "" ls 3, \
	'' u 1:2 w lp t "N=19" ls 3, \
	"fixation_L8_N17.dat" u 1:2:3 w yerrorbars t "" ls 2, \
	'' u 1:2 w lp t "N=17" ls 2, \
	"fixation_L8_N15.dat" u 1:2:3 w yerrorbars t "" ls 2, \
	'' u 1:2 w lp t "N=15" ls 2


pause mouse key
