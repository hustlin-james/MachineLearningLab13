import sys
from copy import deepcopy

def value_iteration(environment_file,non_terminal_reward,gamma,k_iterations):

    k_iterations = int(k_iterations)
    non_terminal_reward = float(non_terminal_reward)
    gamma = float(gamma)

    with open(environment_file) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 

    states = []
    for c in content:
        t = c.split(",")
        states.append(t)
    
    global X_MAX
    global Y_MAX
    global BLOCK_TOKEN


    R_MAX = len(states)
    C_MAX = len(states[0])
    BLOCK_TOKEN = 'X'

    u = []
    for r in states:
        t = []
        for c in r:
            if c=='.':
                t.append(0.0)
            elif c == 'X':
                t.append(BLOCK_TOKEN)
            else:
                if is_float(c):
                    t.append(float(c))
        u.append(t)

    u_2 = zero_matrix(3,4)

    for i in range(k_iterations):
        for r_idx in range(R_MAX):
            for c_idx in range(C_MAX):
                if u[r_idx][c_idx] == 1.0 or u[r_idx][c_idx] == -1.0 or u[r_idx][c_idx] == BLOCK_TOKEN:
                    u_2[r_idx][c_idx] = u[r_idx][c_idx]
                else:
                    down_val = 0.0
                    up_val = 0.0
                    left_val = 0.0
                    right_val = 0.0
                    
                    if (r_idx - 1) == -1 or u[r_idx-1][c_idx] == BLOCK_TOKEN:
                        down_val = u[r_idx][c_idx]
                    elif (r_idx - 1) >= 0:
                        down_val = u[r_idx-1][c_idx]

                    if (r_idx+1) >= R_MAX or u[r_idx+1][c_idx] == BLOCK_TOKEN:
                        up_val = u[r_idx][c_idx]
                    elif (r_idx+1) < R_MAX:    
                        up_val = u[r_idx+1][c_idx]

                    if c_idx -1 == -1 or u[r_idx][c_idx-1] == BLOCK_TOKEN:
                        left_val = u[r_idx][c_idx]
                    elif (c_idx - 1) >= 0:
                        left_val = u[r_idx][c_idx-1]

                    if c_idx + 1 >= C_MAX or u[r_idx][c_idx+1] == BLOCK_TOKEN:
                        right_val = u[r_idx][c_idx]
                    elif (c_idx + 1) < C_MAX:
                        right_val = u[r_idx][c_idx+1]

                    u_2[r_idx][c_idx] = max_utility(non_terminal_reward,gamma,right_val,left_val,up_val,down_val)

        u = deepcopy(u_2)

    for r in u_2:
        s = ''
        for c in r:
            if c == 'X':
                s += "%6.3f,"%(0.0)
            else:
                s += "%6.3f,"%(c)
        s = s[0:len(s)-1]
        print s


def max_utility(non_terminal_reward,gamma,right_val,left_val,up_val,down_val):
    right_utility = non_terminal_reward + gamma*right_val
    left_utility = non_terminal_reward + gamma*left_val
    up_utility = non_terminal_reward + gamma*up_val
    down_utility = non_terminal_reward  + gamma*down_val

    expected_right = .8*right_utility + .1*up_utility + .1*down_utility
    expected_left = .8*left_utility + .1*up_utility + .1*down_utility
    expected_up = .8*up_utility + .1*left_utility + .1*right_utility
    expected_down = .8*down_utility + .1*left_utility + .1*right_utility
    return max(expected_down,expected_up,expected_left,expected_right)


def zero_matrix(r_size,c_size):
    m = []
    for i in range(r_size):
        t=[]
        for j in range(c_size):
            t.append(0.0)
        m.append(t)
    return m

def is_float(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
        
def main():
    if len(sys.argv)== 5:
        environment_file = sys.argv[1]
        non_terminal_reward = sys.argv[2]
        gamma = sys.argv[3]
        k_iterations=sys.argv[4]

        value_iteration(environment_file,non_terminal_reward,gamma,k_iterations)

if __name__ == "__main__":
    main()