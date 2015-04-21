#!/usr/bin/env python
import sys

def main():
    if len(sys.argv) < 8 or "-h" in sys.argv or "--help" in sys.argv:
        print_usage()
        sys.exit()

    given_available, r_park, r_crash, r_handicap, r_drive, spots, r_distance  = [float(arg) for arg in sys.argv[1:]]
    p_handicap = .9
    print 8*int(spots), 2
    print ""
    """
    generates movement probabilities for each state
    
    our states are this:
    Row, Available (t/f), Parked (t/f)
    RowRowB Unavailable RowA Available RowB Available
   
    F,F, T,F F,T, T,T 

    A1 A2 A3 B1 B2 B3, A1 A2 A3 B1 B2 B3, ....
    """ 
    spots = int(spots)
    for t in range(4):
        for i in range(spots * 2):
            for s in range(4):
                for j in range(spots * 2):
                    # i represents our "row", so our current state,
                    #wrap around states
                    if i < (spots):
                        store_distance = spots - i
                    else:
                        store_distance = i - spots + 1
                        #store_distance = (i + 1) / 2
                    p_available = given_available * store_distance / (spots + 1)
                    #next spot  
                    if j == i + 1 and store_distance == 1 or i == spots - 1 and j == 0:
                        if s % 4 == 0:
                            print "%0.2f" % (1 - p_handicap),
                        if s % 4 == 1:
                            print "%0.2f" % p_handicap,
                        elif s % 4 == 2:
                            print "%0.2f" % 0.00,
                        elif s % 4 == 3:
                            print "%0.2f" % 0.00,
                            
                    elif j == i + 1: 
                        #not empty and not parked
                        if s % 4 == 0:
                            print "%0.2f" % (1 - p_available),
                        #empty and not parked
                        elif s % 4 == 1:
                            print "%0.2f" % p_available,
                        #not empty and parked
                        elif s % 4 == 2:
                            print "%0.2f" % 0.00,
                        #not empty and parked
                        elif s % 4 == 3:
                            print "%0.2f" % 0.00,

                    elif i == spots - 1 and j == 0:
                        #not empty and not parked
                        if s % 4 == 0:
                            print "%0.2f" % (1 - p_available),
                        #empty and not parked
                        elif s % 4 == 1:
                            print "%0.2f" % p_available,
                        #not empty and parked
                        elif s % 4 == 2:
                            print "%0.2f" % 0.00,
                        #empty and  parked
                        elif s % 4 == 3:
                            print "%0.2f" % 0.00,
                    else:
                            print "%0.2f" % 0.00,
            print ""
    print ""
    #print park action
    for t in range(4):
        for i in range(spots * 2):
            for s in range(4):
        
                for j in range(spots * 2):
                    # we transition from the current unparked position to the parked position
                    if i == j and ((s % 4 == 3 and t % 4 == 0) or (s % 4 == 2 and t % 4 == 1)):
                        print "%0.2f" % 1.0,
                    #already parked
                    elif i == j and (s % 4 == 3 or s % 4 == 2):
                        print "%0.2f" % 1.0,
                    #parking cannot put us in a non-parked state and it cannot move us
                    else:
                        print "%0.2f" % 0.00,
            print ""
    #print rewards
    print ""
    for s in range(4):
        for i in range(spots * 2):
            if i < (spots):
                store_distance = spots - i
            else:
                store_distance = i - spots + 1
            #handicap
            if store_distance == 1:
                #driving
                if s % 4 < 2:
                    print "%0.2f" % r_drive,
                #parked and occupado
                if s % 4 == 2:
                    print "%0.2f" % r_crash,
                #parked success
                if s % 4 == 3:
                    print "%0.2f" % (r_handicap + r_distance * store_distance),
            else:
                #driving
                if s % 4 < 2:
                    print "%0.2f" % r_drive,
                #parked and occupied
                if s % 4 == 2:
                    print "%0.2f" % r_crash,
                #parked success
                if s % 4 == 3:
                    print "%0.2f" % (r_park + r_distance * store_distance),

                
                 
    

def print_usage():
    print >> sys.stderr, "Creates a parking MDP based on specified parameters, A1 and B1 are handicap spots, probability of availble is a linear function of distance, p * distance/nspots. Rewards are applied, may specify negative. distance reward is applied for each tile the person needs to walk" 
    print >> sys.stderr, "create_parking_mdp.py\t<p_available>\t<parking_reward>\t<crashing_reward>\t<handicap_reward>\t<drive_reward>\t<n_spots>\t<distance_reward> "

if __name__ == "__main__":
    main()
