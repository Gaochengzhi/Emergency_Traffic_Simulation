import traci
import traci.constants as tc

traci.start(["sumo-gui", "-c", "../cfg/emergency.city.sumo.cfg",\
                "--lateral-resolution","0.5", \
                "--device.bluelight.explicit","true"])

step = 0 
veh_id="eme"
end_time = 60000
traci.gui.setSchema("View #0","real world")
while step < end_time:
    traci.simulationStep()
    if step == 1900:
        traci.vehicle.add(veh_id,"em_route",typeID="emergency_v",departSpeed="19")
        traci.vehicle.setParameter(veh_id,"emergency","yes")
        # traci.vehicle.setParameter(veh_id,"maxDesiredSpeed","27")
        # traci.vehicle.setParameter(veh_id,"desiredMaxSpeed","27")
        traci.vehicle.setParameter(veh_id, "device.bluelight.reactiondist", str(90))
        traci.vehicle.setMaxSpeed(veh_id,33)
        traci.vehicle.setSpeedMode(veh_id,32)

        traci.gui.trackVehicle("View #0",veh_id)
        traci.gui.setZoom("View #0", 2000)
        print("yes")


    step+=1
