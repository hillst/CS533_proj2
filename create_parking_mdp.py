#!/usr/bin/env python
import sys

class State():
    row = None
    spot_num = None
    next = None
    previous = None
    distance_from_start = None
    occupied = None
    handicapped = None

    """
    row - 0 or 1 for left row or right row
    spot_num - goes from zero to max_spot, where as max_spot is far from the store and zero is close.
    
    """
    def __init__(self, row, spot_num, next, previous, distance_from_start, occupied, max_spot, p_available, parked):
        self.row = row
        self.spot_num = spot_num
        self.next = next
        self.previous = previous
        self.distance_from_start = distance_from_start
        self.occupied = occupied
        self.max_spot = max_spot
        self.handicapped = (spot_num == 0)
        self.p_available = p_available
        self.parked = parked

    """
    0 is close to the store, max is far from the store, max_spot is the end of the store
    rolls over too
    """
    def calc_distance(self):
        self.distance_from_start = self.spot_num 

    """
    Returns a tuple of the next spot (row, spot_number)
    """
    def next_spot_index(self):
        if self.spot_num == 0 and self.row == 0:
            return 1, 0
        if self.spot_num == self.max_spot and self.row == 1:
            return 0, self.max_spot
    
    def print_transition_probabilities(self):
        p_available = given_available * store_distance / (spots + 1)
        if self.parked:
            return self, "1.0" 
            

def describe_state(i, j, action):
    if i % 4 == 0:
        print "Position", i/4, "Unavailable, Not Parked"
    if i % 4 == 1:
        print "Position", i/4, "available, Not Parked"
    if i % 4 == 2:
        print "Position", i/4, "Unavailable, Parked"
    if i % 4 == 3: 
        print "Position", i/4, "Available, Parked"
    

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
                    if i == spots - 1 and j == 0:
                        if s % 4 == 0:
                            print "%0.2f" % (1 - p_handicap),
                        if s % 4 == 1:
                            print "%0.2f" % p_handicap,
                        elif s % 4 == 2:
                            print "%0.2f" % 0.00,
                        elif s % 4 == 3:
                            print "%0.2f" % 0.00,
                    elif j == i + 1 and store_distance == 1:
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
                    elif j == 0 and i == spots + 1:
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
                    if i == j and ((t % 4 == 0 and s % 4 == 2) or (t % 4 == 1 and s % 4 == 3)):
                        print "%0.2f" % 1.0,
                    #already parked
                    elif i == j and (s % 4 == 3 or s % 4 == 2 and s == t):
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
