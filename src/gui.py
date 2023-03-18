import traci
import csv
import os
import traci.constants as tc


veh_id="eme"
em_vehicle_start_time = 2900  # 100x, 1200 = 12s
end_time = 15690
road_id = "E6"

def get_vid_info(vid,step):
    acc = traci.vehicle.getAccel(vid)
    speed = traci.vehicle.getSpeed(vid)
    pos = traci.vehicle.getLanePosition(vid)
    lane = traci.vehicle.getLaneIndex(vid)
    return (step,vid,acc,speed,pos,lane)
    

def main():

    f = open('../data/data.csv', 'a+')
    writer = csv.writer(f)

    # writer.writerow(("step","vid","acc","speed","pos","lane"))
    step = 0 


    # sumo_exe = "sumo-gui"


    traci.start(["sumo-gui", "-c", "../cfg/emergency.city.sumo.cfg",\
                    "--lateral-resolution","0.5", \
                    "--random", \
                    "--device.bluelight.explicit","true"])

    traci.gui.setSchema("View #0","real world")
    while step < end_time:
        traci.simulationStep()
        if step == em_vehicle_start_time:
            traci.vehicle.add(veh_id,"em_route",typeID="emergency_v",departSpeed="19", departLane="best")
            traci.vehicle.setParameter(veh_id,"emergency","yes")
            traci.vehicle.setParameter(veh_id, "device.bluelight.reactiondist", str(90))
            traci.vehicle.setMaxSpeed(veh_id,33)
            traci.vehicle.setSpeedMode(veh_id,32)
            traci.gui.trackVehicle("View #0",veh_id)
            traci.gui.setZoom("View #0", 2000)

        if step % 5 == 0 and step > em_vehicle_start_time - 1000:
            car_list = traci.edge.getLastStepVehicleIDs(road_id)
            if car_list:
                for vid in car_list:
                    res = get_vid_info(vid,step)
                    # writer.writerow(res)
                
        if step % 500 == 0 and step > em_vehicle_start_time - 1000:
            f.flush()



        step+=1
if __name__ == "__main__":
    main()
