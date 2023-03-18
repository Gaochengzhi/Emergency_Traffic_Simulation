
rm vType.xml
python3 $SUMO_HOME/tools/createVehTypeDistribution.py vtype/car.config.txt --size 1000 --name "car"
python3 $SUMO_HOME/tools/createVehTypeDistribution.py vtype/bus.config.txt --size 1000 --name "bus"
python3 $SUMO_HOME/tools/createVehTypeDistribution.py vtype/motor.config.txt --size 1000 --name "motor"
sed -iE 's/.000//g' vTypeDistributions.add.xml
rm vTypeDistributions.add.xmlE
mv vTypeDistributions.add.xml vType.xml

python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.06 \
--fringe-factor 1 \
-l \
--min-distance 1000 \
--max-distance 500000 \
--end 100 \
-r output.trips1.xml \
--seed 70 \
--validate \
--prefix passenger \
--trip-attributes="type=\"car\" departSpeed=\"max\"" \
--additional-file vType.xml


python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.9 \
--fringe-factor 1 \
-l \
--min-distance 1000 \
--max-distance 500000 \
--end 90 \
-r output.trips2.xml \
--seed 30 \
--validate \
--prefix bus \
--trip-attributes="type=\"bus\" departSpeed=\"max\"" \
--additional-file vType.xml

python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.09 \
--fringe-factor 1 \
-l \
--min-distance 1000 \
--max-distance 500000 \
--end 19 \
-r output.trips3.xml \
--seed 30 \
--validate \
--prefix motorcycle \
--trip-attributes="type=\"motor\" departSpeed=\"max\"" \
--additional-file vType.xml







