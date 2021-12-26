#python3 run-cli.py $1 mix2colors,1,all2avg
#python3 run-cli.py $1 mix2colors,1,avg2ifgt
#python3 run-cli.py $1 mix2colors,1,maxifgt
#python3 run-cli.py $1 mix2colors,2,all2avg
#python3 run-cli.py $1 mix2colors,2,miniflt
#python3 run-cli.py $1 mix2colors,2,maxifgt
#python3 run-cli.py $1 mix2colors,2,all2avg

python3 run-cli.py $1 convertmatrix2,0.299,0.649,1,0.932,0.61,0 multiplycolor,3,0.4 convertinvmatrix2,0.299,0.649,1,0.932,0.61,0
python3 run-cli.py $1 convertmatrix2,0.299,0.649,1,0.932,0.61,0 scurve,3,75 convertinvmatrix2,0.299,0.649,1,0.932,0.61,0
python3 run-cli.py $1 convertmatrix2,0.522,0.510,0.388,0.665,0.518,0.525 multiplycolor,3,0.4 convertinvmatrix2,0.522,0.510,0.388,0.665,0.518,0.525
python3 run-cli.py $1 convertmatrix2,1,0.5,0,0.8,0.8,0.5 zerocolor,3 convertinvmatrix2,1,0.5,0,0.8,0.8,0.5
python3 run-cli.py $1 convertmatrix2,0.7,0.7,0.7,1,0.5,0 zerocolor,3 convertinvmatrix2,0.7,0.7,0.7,1,0.5,0
python3 run-cli.py $1 convertmatrix2,1,0.5,0,0.2,1,0.5 multiplycolor,3,0.6 convertinvmatrix2,0.6,0.6,0,0.2,1,0.5
python3 run-cli.py $1 convertmatrix2,0.945,1,0.376,0.235,0.148,0.849 scurve,3,75 convertinvmatrix2,0.945,1,0.376,0.235,0.148,0.849
python3 run-cli.py $1 convertmatrix2,1,0.114,0.847,0.537,0.985,0.119 scurve,3 convertinvmatrix2,1,0.114,0.847,0.537,0.985,0.119