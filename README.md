# Emergency_Traffic_Simulation

This project aims to simulate emergency traffic on city roads using SUMO (Simulation of Urban Mobility).

![Screen Shot 2023-03-18 at 10.43.53](/Users/kounarushi/mycode/Emergency_Traffic_Simulation/assets/Screen%20Shot%202023-03-18%20at%2010.43.53.jpg)



![Screen Shot 2023-03-18 at 10.42.17](/Users/kounarushi/mycode/Emergency_Traffic_Simulation/assets/Screen%20Shot%202023-03-18%20at%2010.42.17.jpg)

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

to change the route of the emergency vehicle, edit the `output.trips0.xml`
