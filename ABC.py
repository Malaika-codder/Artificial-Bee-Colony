import random

random.seed(68)                  

# the function we're minimizing , 
# This function is used to define the problem
def f(x):
    return (x - 7) ** 2 + 4     

# higher fitness = closer to the minimum 
#This function help to select better food sources
def fitness(x):
    return 1 / (1 + f(x))        

#Generate Random food sources values between (0 - 14)
sources = [random.uniform(0, 14) for _ in range(5)]

# how many tries since a source last improved or fail to improve
trials = [0 for _ in range(5)]

# abandon a source after this many failed tries 
#This is use to check that if a particular  food source improve or not
limit = 8   

#Number of Iterations
iterations = 40


for it in range(iterations):

    # Employed bee That search nearby food source in his own circle
    for i in range(5):

        k = random.choice(
            [j for j in range(5) if j != i]
        )

        #By looking at the nearby food source employee bee generate a new location or food source
        candidate = (
            sources[i]
            + random.uniform(-1, 1)
            * (sources[i] - sources[k])
        )                        

        #this condition check that if the new location/food source is better then the current food source
        if fitness(candidate) > fitness(sources[i]):
            #if YES then assign new food source as current food source and make trail = 0
            sources[i], trials[i] = candidate, 0

        else:
            #otherwise add 1 in the trail (so that the food sourse is not improving)
            trials[i] = trials[i] + 1


    # Scout bee phase
    for i in range(5):
        #The check the if the trail is greater then limit
        if trials[i] > limit:
            #if YES then Generate a new random food source
            sources[i] = random.uniform(0, 14)

            # and set its trails to 0
            trials[i] = 0


# Find best solution
best = max(sources, key=fitness)

print("Best x:", best)
print("Minimum value:", f(best))