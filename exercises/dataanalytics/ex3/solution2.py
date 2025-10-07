from scipy import stats as st
import numpy as np


## First get the result using Theoretical Probability to compare it with Simulation Method

# st.binom.pmf(k, n, p) => Output is the the probability that exactly k successes occur in n independent trials, each with success probability p
# k => The number of successes we care about (exactly 10)
# n => Total number of trials
# p => Probability of success in each tria

# Lets solve the problem using method ´.pmf()´ (Probability Mass Function)
p = 0.96                            # probability of a participant turns up for the session is 0.96
target_probability = 0.97           # the probability that the session is full (i.e. 8 or more participants turn up)
available_spots = 8                 # number of spots in seminar
spots_to_sell = available_spots     # start from available_spots / trials

# Start an infinite while loop (which we will break out of when satisfied ie > 0.97 probability
while True:
    # Sum probabilities of having at least 'spots' participants turn up
    seminar_full_probability = sum(st.binom.pmf(k=i, n=spots_to_sell, p=p) for i in range(available_spots, spots_to_sell + 1))
    
    # Break out when satisfied (> 0.97 probability was given in the problem statement)
    if seminar_full_probability > target_probability:
        print("****** Output from Theoretical Probability Method *********")
        print(f"Probability of full session (≥ {available_spots}): {seminar_full_probability:.4f}") # Probability of full session (≥ 8): 0.9938
        print(f"Minimum number of spots to sell: {spots_to_sell}") # Minimum number of spots to sell: 10
        print()
        break

    # In case we didn't break out, increase the number of spots to sell
    spots_to_sell += 1



# # Lets to the same using simulation

# Parameters
p = 0.96                    # probability of a participant turns up for the session is 0.96
available_spots = 8         # number of spots in seminar
spots_to_sell = 10           # start from available_spots / trials, change to get expected probability
experiments = 100_000       # set to large number to get stable estimates

simulation = st.binom.rvs(n=spots_to_sell, p=p, size=experiments)

print("****** Output from Simulation Method *********")
print(f'Occurences where session is full ie (i.e. 8 or more participants turn up)(out of {experiments} experiments): {sum(simulation>=8)}')
print(f'Induced Probability by changing spots_to_sell to {spots_to_sell} is: {sum(simulation>=8)/experiments:.4f}')
print(f"Minimum number of spots to sell: {spots_to_sell}")