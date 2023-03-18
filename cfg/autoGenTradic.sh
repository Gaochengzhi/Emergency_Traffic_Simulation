python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.06 \
--fringe-factor 1 \
-L \
--min-distance 1000 \
--max-distance 500000 \
--end 100 \
-r output.trips1.xml \
--seed 70 \
--validate \
--vehicle-class passenger \
--prefix passenger \
--trip-attributes="departSpeed=\"13.5\" maxSpeed=\"13.8\" departLane=\"best\" lcCooperative=\"1\" carFollowModel=\"EIDM\"" \

python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.09 \
--fringe-factor 1 \
-L \
--min-distance 1000 \
--max-distance 500000 \
--end 9 \
-r output.trips2.xml \
--seed 30 \
--validate \
--vehicle-class truck \
--prefix truck \
--trip-attributes="departSpeed=\"13.5\" departLane=\"best\" lcCooperative=\"1\" carFollowModel=\"EIDM\"" \


python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \
-p 0.09 \
--fringe-factor 1 \
-L \
--min-distance 1000 \
--max-distance 500000 \
--end 19 \
-r output.trips3.xml \
--seed 30 \
--validate \
--vehicle-class motorcycle \
--prefix motorcycle \
--trip-attributes="departSpeed=\"13.5\" departLane=\"best\" lcCooperative=\"1\"" \
