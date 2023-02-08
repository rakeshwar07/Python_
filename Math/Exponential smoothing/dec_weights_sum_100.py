import numpy as np
def weight_generator(ui): #number of splits
    d1 = 200/(ui*(ui-1)) #Split ratio or the smoothing factor
    if d1>5:
        d = 5
    else:
        d = d1 - 0.000001 #This is to reduce the roundoff error
    x0 = (100/ui) + ((d*(ui-1))/2) #Finds the first highest number

    weights = []
    new = x0
    for i in range(1,ui+1): 
        weights.append(new)
        new = new-d
    return np.array(weights,dtype="float32")

if __name__ == "__main__":
    res = weight_generator(5)
    print(res)