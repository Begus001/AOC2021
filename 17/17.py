def A():
    file = open("17/input", "r")
    line = file.read().strip("target area: ").replace("x=", "").replace(", y=", "..").split("..")

    
    targetminx = int(line[0])
    targetmaxx = int(line[1])
    targetminy = int(line[2])
    targetmaxy = int(line[3])
    
    target = set()
    for y in range(targetminy, targetmaxy + 1):
        for x in range(targetminx, targetmaxx + 1):
            target.add((y, x))

    threshold = 100
    xovershot = yovershot = 0
    startxvel = startyvel = 1
    trajectory = []
    trajectories = []
    while True:
        lastlen = len(trajectories)
        trajectory.clear()
        trajectory.append((0, 0))
        yvel, xvel = startyvel, startxvel
        # simulate
        while True:
            lasty, lastx = trajectory[len(trajectory)-1]
            trajectory.append((lasty + yvel, lastx + xvel))
            lasty, lastx = trajectory[len(trajectory)-1]
            if targetminy <= lasty <= targetmaxy and targetminx <= lastx <= targetmaxx:
                trajectories.append(trajectory.copy())
                break # found trajectory
            if lasty < targetminy or lastx > targetmaxx:
                break # overshot

            if xvel < 0: xvel += 1
            elif xvel > 0: xvel -= 1
            yvel -= 1
        
        if lastlen == len(trajectories):
            xovershot += 1
            if xovershot > threshold:
                if xovershot >= startxvel:
                    yovershot += 1
                    if yovershot > threshold:
                        break
                
                startyvel += 1
                xovershot = 0
                startxvel = 0
                continue
        else:
            xovershot = 0
            yovershot = 0
        
        startxvel += 1


    select = None
    for t in trajectories:
        highest = 0
        for y, x in t:
            if y > highest:
                highest = y
                select = t
    
    print("A: %d" % (max(select)[0]))

    file.close()


def B():
    file = open("17/input", "r")
    line = file.read().strip("target area: ").replace("x=", "").replace(", y=", "..").split("..")

    
    targetminx = int(line[0])
    targetmaxx = int(line[1])
    targetminy = int(line[2])
    targetmaxy = int(line[3])
    
    target = set()
    for y in range(targetminy, targetmaxy + 1):
        for x in range(targetminx, targetmaxx + 1):
            target.add((y, x))

    threshold = 1000
    xovershot = yovershot = 0
    startxvel = 0
    startyvel = -10000
    trajectory = []
    trajectories = []
    notrajfoundyet = True
    while True:
        lastlen = len(trajectories)
        trajectory.clear()
        trajectory.append((0, 0))
        yvel, xvel = startyvel, startxvel
        # simulate
        while True:
            lasty, lastx = trajectory[len(trajectory)-1]
            trajectory.append((lasty + yvel, lastx + xvel))
            lasty, lastx = trajectory[len(trajectory)-1]
            if targetminy <= lasty <= targetmaxy and targetminx <= lastx <= targetmaxx:
                trajectories.append(trajectory.copy())
                if notrajfoundyet:
                    notrajfoundyet = False
                break # found trajectory
            if lasty < targetminy or lastx > targetmaxx:
                break # overshot

            if xvel < 0: xvel += 1
            elif xvel > 0: xvel -= 1
            yvel -= 1
        
        if lastlen == len(trajectories):
            xovershot += 1
            if xovershot > threshold:
                if xovershot >= startxvel:
                    yovershot += 1
                    if yovershot > threshold and not notrajfoundyet:
                        break
                
                startyvel += 1
                xovershot = 0
                startxvel = 0
                continue
        else:
            xovershot = 0
            yovershot = 0
        
        startxvel += 1
    
    print("B: %d" % (len(trajectories)))

    file.close()


if __name__ == "__main__":
    A()
    B()