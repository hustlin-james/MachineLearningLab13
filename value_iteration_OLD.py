import sys
from copy import deepcopy
#  if states[r_idx][c_idx] != 'X':
#                     stay_action = transition((r_idx,c_idx),(r_idx,c_idx),"")
#                 if c_idx - 1 < states[r_idx][c_idx-1] != 'X':
#                     left_action = transition((r_idx,c_idx-1),(r_idx,c_idx),"left")
#                 if states[r_idx+1][c_idx] != 'X':
#                     up_action = transition((r_idx+1,c_idx),(r_idx,c_idx),"up")
#                 if states[r_idx][c_idx+1] != 'X':
#                     right_action = transition((r_idx,c_idx+1),(r_idx,c_idx),"right")
#                 if states[r_idx-1][c_idx] != 'X':
#                     down_action =  transition((r_idx-1,c_idx),(r_idx,c_idx),"down")
#                 u_2[r_idx][c_idx] = reward(r_idx,c_idx,non_terminal_reward) + gamma*max(left_action,up_action,right_action,down_action)


# #s: set of states, the grids in the f


#s: set of states, the grids in the file
#a(s): set of actions available at each state s
#p(s'|s,a)
#R reward function
#discount facotr gamma
#e maximum error
def value_iteration(environment_file,non_terminal_reward,gamma,k_iterations):

    k_iterations = int(k_iterations)
    non_terminal_reward = float(non_terminal_reward)
    gamma = float(gamma)

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

    Y_MAX = len(envo[0])
    X_MAX = len(envo)

    print('X_MAX:%d'%X_MAX)
    print('Y_MAX:%d'%Y_MAX)

    states = envo

    #n = X_MAX*Y_MAX
    #u_2 = [0.0]*n

    u_2 = []
    for r in states:
        t = []
        for c in r:
            t.append(0.0)
        u_2.append(t)

    
    for i in range(k_iterations):
        #print(i)
        #u = u_2[:]
        u = deepcopy(u_2)
        delta = 0.0
        if i == 1:
            print(u)

        for y_idx in range(Y_MAX):
            for x_idx in range(X_MAX):
                #x_idx is the first array index for states
                if states[x_idx][y_idx] == '-1':
                    u_2[x_idx][y_idx] = -1.0
                elif states[x_idx][y_idx] == '1':
                    u_2[x_idx][y_idx] = 1.0
                else:
                    if states[x_idx][y_idx] != 'X':
                        #pass
                        # left_action = utility_value((r_idx,c_idx),u,"left")
                        # up_action = utility_value((r_idx,c_idx),u,"up")
                        # right_action = utility_value((r_idx,c_idx),u,"right")
                        # down_action =  utility_value((r_idx,c_idx),u,"down")
                        
                        r_val = reward(x_idx,y_idx,non_terminal_reward)
                        #print(r_val)
                
                        u_2[x_idx][y_idx] = r_val  + gamma*max_action(x_idx,y_idx,u)

        
        # if i == 2:
        #     break
        print(u_2)

       
def max_action(x_idx,y_idx,u):
    #x is 0-2
    #y is 0-3
    
    left_same = utility_value((x_idx,y_idx), (x_idx,y_idx),u,"left", "same")
    left_left = utility_value((x_idx,y_idx-1), (x_idx,y_idx),u,"left", "left")
    left_up= utility_value((x_idx+1,y_idx), (x_idx,y_idx),u,"left","up")
    left_right = utility_value((x_idx,y_idx+1), (x_idx,y_idx),u,"left","right")
    left_down = utility_value((x_idx-1,y_idx), (x_idx,y_idx),u,"left","down")

    left_total = left_same+left_left+left_up+left_right+left_down

    print('left_total: %f'%(left_total))
    print('----------------------------------------------------------------------------------')


    right_same = utility_value((x_idx,y_idx), (x_idx,y_idx),u,"right","same")
    right_left = utility_value((x_idx,y_idx-1), (x_idx,y_idx),u,"right","left")
    right_up= utility_value((x_idx+1,y_idx), (x_idx,y_idx),u,"right","up")
    right_right = utility_value((x_idx,y_idx+1), (x_idx,y_idx),u,"right","right")
    right_down = utility_value((x_idx-1,y_idx), (x_idx,y_idx),u,"right","down")


    right_total = right_same+right_left+right_up+right_right+right_down

    
    print('right_total: %f'%(right_total))
    print('----------------------------------------------------------------------------------')


    up_same = utility_value((x_idx,y_idx), (x_idx,y_idx),u,"up","same")
    up_left = utility_value((x_idx,y_idx-1), (x_idx,y_idx),u,"up","left")
    up_up= utility_value((x_idx+1,y_idx), (x_idx,y_idx),u,"up","up")
    up_right = utility_value((x_idx,y_idx+1), (x_idx,y_idx),u,"up","right")
    up_down = utility_value((x_idx-1,y_idx), (x_idx,y_idx),u,"up","down")

    up_total = up_same+up_left+up_up+up_right+up_down

    
    print('up_total: %f'%(up_total))
    print('----------------------------------------------------------------------------------')

    down_same = utility_value((x_idx,y_idx), (x_idx,y_idx),u,"down","same")
    down_left = utility_value((x_idx,y_idx-1), (x_idx,y_idx),u,"down","left")
    down_up= utility_value((x_idx+1,y_idx), (x_idx,y_idx),u,"down","up")
    down_right = utility_value((x_idx,y_idx+1), (x_idx,y_idx),u,"down","right")
    down_down = utility_value((x_idx-1,y_idx), (x_idx,y_idx),u,"down","down")

    down_total = down_same+down_left+down_up+down_right+down_down


        
    print('down_total: %f'%(up_total))
    print('----------------------------------------------------------------------------------')
    
    max_val = max(left_total,right_total,up_total,down_total)
    print('max_val: %f'%max_val)
    return max_val

def utility_value(dest,orig,u,action,direction):
  
    x = orig[0]
    y = orig[1]
    dest_x = dest[0]
    dest_y = dest[1]
    u_val = 0.0
   
    if action == "left":
        #staying at the same spot
        if dest_x == x and dest_y == y:
            print('x: %d'%(x))
            print('y: %d'%(y))
            #left
            if y-1 == -1 or states[x][y-1] == 'X':
                print('left')
                print( .8*u[dest_x][dest_y])
                u_val += .8*u[dest_x][dest_y]
            #up
            if x+1 == X_MAX or  states[x+1][y] =='X':
                print('up')
                u_val += .1*u[dest_x][dest_y]
                print(.1*u[dest_x][dest_y])
            #down
            if x-1 == -1 or states[x-1][y]=='X':
                print('down')
                u_val += .1*u[dest_x][dest_y]
                print(.1*u[dest_x][dest_y])

        #Going left
        if dest_x == x and dest_y == y-1:
            if y-1 != -1 and states[dest_x][dest_y] != 'X':
                u_val += .8*u[dest_x][dest_y]
        #Going Up
        if dest_x == x+1 and dest_y == y:
            if dest_x != X_MAX and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
    
        #down
        if dest_x == x-1 and dest_y == y:
            if dest_x != -1 and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
    elif action == "right":
        #staying at the same spot
        if dest_x == x and dest_y == y:
            #right
            if y+1 == Y_MAX or states[x][y+1] == 'X':
                u_val += .8*u[x][y]
            #up
            if x+1 == X_MAX or states[x+1][y] == 'X':
                u_val += .1*u[x][y] 
            #down
            if x-1 == -1 or states[x-1][y] == 'X':
                u_val += .1*u[x][y]
        #right
        if x == dest_x and dest_y == y+1:
            if y+1 != Y_MAX and states[dest_x][dest_y] != 'X':
                u_val += .8*u[dest_x][dest_y]
        #up
        if x+1 == dest_x and dest_y == y:
            if dest_x != X_MAX and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
        #down
        if x-1==dest_x and dest_y == y:
            if dest_x != -1 and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
    elif action == 'up':
        #staying same spot
        if dest_x == x and dest_y == y:
            #up
            if x+1 == X_MAX or states[x+1][y] == 'X':
                u_val += .8*u[x][y]
            #right
            if y+1 == Y_MAX or states[x][y+1] == 'X':
                u_val += .1*u[x][y]
            #left
            if y-1 == -1 or states[x][y-1] == 'X':
                u_val += .1*u[x][y]
        #up
        if dest_x==x+1 and y == dest_y:
            if dest_x != X_MAX and states[dest_x][dest_y] != 'X':
                u_val += .8*u[dest_x][dest_y]

        #left
        if dest_y == y-1 and x==dest_x:
            if dest_y != -1 and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
        #right
        if dest_y == y+1 and x == dest_x:
            if dest_y != Y_MAX and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
    elif action == 'down':
        #staying same spot
        if dest_x == x and dest_y == y:
            #down
            if x-1 == -1 or states[x-1][y] =='X':
                u_val += .8*u[x][y]
            #left
            if y-1 == -1 or states[x][y-1] == 'X':
                u_val += .1*u[x][y]
            #right
            if y+1 == Y_MAX or states[x][y+1] == 'X':
                u_val += .1*u[x][y]
        #down
        if dest_x == x-1 and y == dest_y:
            if dest_x != -1 and states[dest_x][dest_y] != 'X':
                u_val += .8*u[dest_x][dest_y]
        #left
        if dest_y == y-1 and x==dest_x:
            if dest_y != -1 and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]
        #right
        if dest_y == y+1 and x == dest_x:
            if dest_y != Y_MAX and states[dest_x][dest_y] != 'X':
                u_val += .1*u[dest_x][dest_y]            

    print('action: '+action)
    print('direction: '+direction)
    print(dest)
    print(orig)
    print('u_val: %f'%(u_val))
    return u_val

def is_float(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def reward(x,y,non_terminal_reward):
    val = states[x][y]
    if val == ".":
        return non_terminal_reward
    else:
        if is_float(val):
            print(val)
            return float(val)
        elif val == 'X':
            return 0.0
        
def main():
    if len(sys.argv)== 5:
        environment_file = sys.argv[1]
        non_terminal_reward = sys.argv[2]
        gamma = sys.argv[3]
        k_iterations=sys.argv[4]

        value_iteration(environment_file,non_terminal_reward,gamma,k_iterations)

if __name__ == "__main__":
    main()