import sys



#s: set of states, the grids in the file
#a(s): set of actions available at each state s
#p(s'|s,a)
#R reward function
#discount facotr gamma
#e maximum error
def value_iteration(environment_file,non_terminal_reward,gamma,k_iterations):
    

def main():
    if len(sys.argv)== 5:
        environment_file = sys.argv[1]
        non_terminal_reward = sys.argv[2]
        gamma = sys.argv[3]
        k_iterations=sys.argv[4]

        value_iteration(environment_file,non_terminal_reward,gamma,k_iterations)

if __name__ == "__main__":
    main()