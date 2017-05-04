import sys



#s: set of states, the grids in the file
#a(s): set of actions available at each state s
#p(s'|s,a)
#R reward function
#discount facotr gamma
#e maximum error
def value_iteration(environment_file,non_terminal_reward,gamma,k_iterations):
    with open(environment_file) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 

    envo = []
    for c in content:
        t = c.split(",")
        envo.append(t)
    
    global X_MAX
    global Y_MAX
    global states

    envo.reverse()

    X_MAX = len(envo)
    Y_MAX = len(envo[0])
    states = envo

    n = X_MAX*Y_MAX
    u_2 = [0.0]*n

    for i in range(k_iterations):
        u = u_2[:]
        delta = 0

        for s in states:
            u_2 = 

    print(envo)
    print(u)

    p = transition((0,0),(0,0),"left")

def is_float(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
def reward(x,y):
    val = states[x][y]
    if val == ".":
        return -0.04
    else:
        if is_float(val):
            return float(val)
        elif val == 'X':
            return 0.0
        

def transition(dest,origin,action):
    dest_x = dest[0]
    dest_y = dest[1]
    origin_x = origin[0]
    origin_y = origin[1]

    p = 0.0
    #staying same spot

    #change to origin 
    if dest_x == origin_x and dest_y == origin_y:
        #left
        if action == "left":
            if (origin_x - 1) == -1: p += .8
            if (origin_y - 1) == -1: p += .1
            if (origin_y + 1) == Y_MAX: p += .1 
        #up 
        if action == "up":
            if (origin_y + 1) == Y_MAX: p += .8
            if (origin_x - 1) == -1: p += .1
            if (origin_x + 1) == X_MAX: p += .1
        #right 
        if action == "right":
            if (origin_x + 1) == X_MAX: p += .8
            if (origin_y + 1) == Y_MAX: p += .1
            if (origin_y - 1) == -1: p += .1
        #down 
        if action == "down":
            if (origin_y - 1) == -1: p+=.8
            if (origin_x + 1) == X_MAX: p+= .1
            if (origin_x - 1) == -1: p+= .1   
    #moving left
    if dest_x == origin_x - 1 and dest_y == origin_y:   
        if action == "left":
            if dest_x != -1:p += .8
        if action == "up":
            if (dest_x) != -1: p += .1
        if action == "right":pass
        if action == "down":
            if (dest_x) != -1: p += .1
    #moving up
    if dest_x == origin_x and dest_y == origin_y + 1:
        if action == "left":
            if (dest_y) != Y_MAX: p += .1
        if action == "up":
            if (dest_y) != Y_MAX: p += .8
        if action == "right": 
            if(dest_y) != Y_MAX: p+= .1
        if action == "down": 
            pass
    #moving right
    if dest_x == (origin_x + 1) and dest_y == origin_y:
        if action == "left": pass
        if action == "up": 
            if (dest_x) != X_MAX: p += .1
        if action == "right": 
            if(dest_x) != X_MAX: p += .8
        if action == "down": 
            if (dest_x) != X_MAX: p += .1
    #moving down
    if dest_x == origin_x and dest_y == (origin_y - 1):
        if action == "left": 
            if dest_y != -1: p+=.1
        if action == "up": 
            if dest_y != -1: pass
        if action == "right": 
            if dest_y != -1: p+= .1
        if action == "down": 
            if dest_y != -1: p+= .8

    return p  

def main():
    if len(sys.argv)== 5:
        environment_file = sys.argv[1]
        non_terminal_reward = sys.argv[2]
        gamma = sys.argv[3]
        k_iterations=sys.argv[4]

        value_iteration(environment_file,non_terminal_reward,gamma,k_iterations)

if __name__ == "__main__":
    main()