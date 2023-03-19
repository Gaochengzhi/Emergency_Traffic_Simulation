import traci
import csv
import os
import traci.constants as tc



em_vid="eme"
em_vehicle_start_time = 2000  # 100x, 1200 = 12s
end_time = 15690
detect_range = 80
lctime = 3
lcmode=0b011001000101

road_id = "E6"

def get_vid_info(vid,step):
    acc = traci.vehicle.getAccel(vid)
    speed = traci.vehicle.getSpeed(vid)
    pos = traci.vehicle.getLanePosition(vid)
    lane = traci.vehicle.getLaneIndex(vid)
    return (step,vid,acc,speed,pos,lane)
    

def main(road_id):

    f = open('../data/data.csv', 'a+')
    writer = csv.writer(f)

    # writer.writerow(("step","vid","acc","speed","pos","lane"))
    step = 0 


    # sumo_exe = "sumo-gui"


    traci.start(["sumo-gui", "-c", "../cfg/emergency.city.sumo.cfg",\
                    # "--lateral-resolution","0.5", \
                    "--lanechange.duration", "2" , \
                    "--random", \
                    "--device.bluelight.explicit","true"])

    traci.gui.setSchema("View #0","real world")
    while step < end_time:
        traci.simulationStep()
        if step == em_vehicle_start_time:
            traci.vehicle.add(em_vid,"em_route",typeID="emergency_v",departSpeed="19", departLane="0")
            traci.vehicle.setParameter(em_vid,"emergency","yes")
            traci.vehicle.setParameter(em_vid, "device.bluelight.reactiondist", str(90))
            traci.vehicle.setMaxSpeed(em_vid,33)
            traci.vehicle.setSpeedMode(em_vid,32)
            traci.gui.trackVehicle("View #0",em_vid)
            traci.gui.setZoom("View #0", 3000)

        if step % 20 == 0 and step > em_vehicle_start_time+800:
            road_id = traci.vehicle.getRoadID(em_vid)
            em_info = get_vid_info(em_vid,step)
            car_list = traci.edge.getLastStepVehicleIDs(road_id)
            if car_list:
                for vid in car_list:
                    res = get_vid_info(vid,step)

                    traci.vehicle.setLaneChangeMode(vid,lcmode)

                    if (res[4]-em_info[4]< detect_range) and (res[4]-em_info[4]>0) and res[5]==em_info[5]:
                        lcsl = traci.vehicle.couldChangeLane(vid,1) ## 1 is left
                        lcsr = traci.vehicle.couldChangeLane(vid,-1) ## -1 is right
                        if lcsl:
                            traci.vehicle.changeLaneRelative(vid,1,lctime)
                            print(f"vid:{vid},change left")
                        else:
                            # if lcsr:
                            traci.vehicle.changeLaneRelative(vid,-1,lctime)
                            print(f"vid:{vid},change right")
                    elif (res[4]-em_info[4]< detect_range) and (res[4]-em_info[4]>0):
                        if (res[5]-em_info[5]>0): # change to left
                            traci.vehicle.changeLaneRelative(vid,1,lctime)
                            pass
                        if (res[5]-em_info[5]<0): # change to right
                            traci.vehicle.changeLaneRelative(vid,-1,lctime)
                            pass
                        

            
        if step % 10 == 0 and step > em_vehicle_start_time - 10000 and step< em_vehicle_start_time+800:
            car_list = traci.edge.getLastStepVehicleIDs(road_id)
            if car_list:
                for vid in car_list:
                    res = get_vid_info(vid,step)
                    # writer.writerow(res)
                
        if step % 500 == 0 and step > em_vehicle_start_time - 1000:
            f.flush()



        step+=1
if __name__ == "__main__":
    main(road_id)
