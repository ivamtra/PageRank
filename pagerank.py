import numpy as np

def generateQ(textFile):
    arr = np.genfromtxt(textFile, delimiter=',')
    arr = np.delete(arr, 0, 0) # delete first row

    # Graph
    has_link_from = {}
    N_j = {}

    for row in arr:
        # Create key value pair
        # and switch columns so it is easier
        # to create Q matrix
        try:
            has_link_from[row[1]].append(row[0])
        except:
            has_link_from[row[1]] = [row[0]]
        # Calculate N_j    
        try: 
            N_j[row[0]] += 1
        except:
            N_j[row[0]] = 1

    # size of Q matrix
    size = int(np.amax(arr)) 
    Q = np.zeros((size,size))

    # Create Q from links
    for key, value in has_link_from.items():
        for i in value:
            col = int(i) -1
            row = int(key) - 1
            Q[row,col] = 1 / N_j[i]

    return Q        

def power_iteration(Q, epsilon):
    # Q.shape[0] = n
    r_old = np.ones(Q.shape[0])/Q.shape[0]

    r_new = np.dot(Q, r_old)

    while np.linalg.norm(r_old - r_new) >= epsilon:
        r_old = r_new
        r_new = np.dot(Q, r_old)
    return r_new    


Q = generateQ('graph.txt')

print('r =', power_iteration(Q, 0.004))    
print('Q =', Q)
