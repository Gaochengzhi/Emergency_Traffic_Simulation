# Emergency_Traffic_Simulation

This project aims to simulate emergency traffic on city roads using SUMO (Simulation of Urban Mobility).

![Screen Shot 2023-03-18 at 10.43.53](assets/Screen%20Shot%202023-03-18%20at%2010.43.53.jpg)



![Screen Shot 2023-03-18 at 10.42.17](assets/Screen%20Shot%202023-03-18%20at%2010.42.17.jpg)

## Getting Started

To get started, you have to download sumo https://www.eclipse.org/sumo/

If you are using Linux and apt, you can just paste the following command in your terminal:

```bash
sudo add-apt-repository ppa:sumo/stable 
sudo apt-get update
sudo apt-get install sumo sumo-tools
pip install traci  ## important! I didn't use the traditional 
## path import method because I was lazy 😅
```

## Have a quick run

```bash
git clone https://github.com/Gaochengzhi/Emergency_Traffic_Simulation.git --depth 1
cd Emergency_Traffic_Simulation
cd src
python3 main.py
```

## Adjustment parameter

all the config files are in the cfg folder:

```bash
➜  cfg git:(main) ✗ ls
addition.xml            emergency.city.sumo.cfg output.trips0.xml       output.trips3.xml
autoGenTradic.sh        net.xml                 output.trips1.xml       trips.trips.xml
clib.xml                netback.jpg             output.trips2.xml
```

* to change the route of the emergency vehicle, edit the `output.trips0.xml`

```shell

<route id="em_route" edges="E6 E8 E9 E9.823 E10 E11 "/> 
## use > netedit net.xml 
## if you are not sure the EDGE (not juction!) id
```

* to change the traffic flow volume and vehicle types, edit the `autoGenTradic.sh`

```shell
python3 $SUMO_HOME/tools/randomTrips.py \
-n net.xml \ 
-p 0.06 \ ## volume, smaller number result in larger volume
--fringe-factor 1 \ ## Whether the vehicle is generated only from the boundary of the road, larger(inf) is  
-L \
--min-distance 1000 \
--max-distance 500000 \
--end 100 \ ## time to stop generating 
-r output.trips1.xml \ ## output file name, if you dont want to add new type, just leave it, otherwise you have to add new file name in cfg file's <input_file>
--prefix passenger \ ## same as above
--seed 70 \
--validate \
--vehicle-class passenger \
--trip-attributes="departSpeed=\"13.5\" maxSpeed=\"13.8\" departLane=\"best\" lcCooperative=\"1\" carFollowModel=\"EIDM\"" \
```

