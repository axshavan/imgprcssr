python3 run-cli.py $1 mix2colors_sym,1,all2avg
python3 run-cli.py $1 mix2colors_sym,1,avg2ifgt
python3 run-cli.py $1 mix2colors_sym,1,maxifgt
python3 run-cli.py $1 mix2colors_sym,2,miniflt
python3 run-cli.py $1 mix2colors_sym,2,maxifgt
python3 run-cli.py $1 mix2colors_sym,2,all2avg

python3 run-cli.py $1 convertmatrix2,0.299,0.649,1,0.932,0.61,0 multiplycolor,3,0.4 convertinvmatrix2,0.299,0.649,1,0.932,0.61,0
python3 run-cli.py $1 convertmatrix2,0.299,0.649,1,0.932,0.61,0 scurve,3,75 convertinvmatrix2,0.299,0.649,1,0.932,0.61,0
python3 run-cli.py $1 convertmatrix2,0.522,0.510,0.388,0.665,0.518,0.525 multiplycolor,3,0.4 convertinvmatrix2,0.522,0.510,0.388,0.665,0.518,0.525
python3 run-cli.py $1 convertmatrix2,1,0.5,0,0.8,0.8,0.5 zerocolor,3 convertinvmatrix2,1,0.5,0,0.8,0.8,0.5
python3 run-cli.py $1 convertmatrix2,0.7,0.7,0.7,1,0.5,0 zerocolor,3 convertinvmatrix2,0.7,0.7,0.7,1,0.5,0
python3 run-cli.py $1 convertmatrix2,1,0.5,0,0.2,1,0.5 multiplycolor,3,0.6 convertinvmatrix2,0.6,0.6,0,0.2,1,0.5
python3 run-cli.py $1 convertmatrix2,0.945,1,0.376,0.235,0.148,0.849 scurve,3,75 convertinvmatrix2,0.945,1,0.376,0.235,0.148,0.849
python3 run-cli.py $1 convertmatrix2,1,0.114,0.847,0.537,0.985,0.119 scurve,3 convertinvmatrix2,1,0.114,0.847,0.537,0.985,0.119
python3 run-cli.py $1 convertmatrix2,0.912,0.147,0.867,0.068,0.422,0.099 scurve,3,100 convertinvmatrix2,0.912,0.147,0.867,0.068,0.422,0.099
python3 run-cli.py $1 convertmatrix2,1,0.430,0.867,0.449,0.603,0.760 scurve,3,10 convertinvmatrix2,1,0.430,0.867,0.449,0.603,0.760
python3 run-cli.py $1 convertmatrix2,0.838,0.628,0.045,0.066,0.755,0.451 multiplycolor,3,0.4 convertinvmatrix2,0.838,0.628,0.045,0.066,0.755,0.451
python3 run-cli.py $1 convertmatrix2,0.1,0.632,0.003,0.887,0.521,0.332 multiplycolor,3,0.4 convertinvmatrix2,0.1,0.632,0.003,0.887,0.521,0.332 scurve,1

