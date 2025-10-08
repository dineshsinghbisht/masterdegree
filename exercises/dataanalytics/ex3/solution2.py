from scipy import stats as st
import numpy as np

## Lets first solve the problem using Theoretical method using function st.binom.pmf from scipy.stats

# st.binom.pmf(k, n, p) 
# → Returns the probability of getting exactly k successes in n independent Bernoulli trials, 
#   where each trial has a probability p of success.
#
# k → The number of successes of interest (e.g., exactly 10 successes).
# n → The total number of independent trials.
# p → The probability of success in each trial.

p = 0.96                            # probability of a participant turns up for the session is 0.96
target_probability = 0.97           # the probability that the session is full (i.e. 8 or more participants turn up)
available_spots = 8                 # number of spots in seminar
spots_to_sell = available_spots     # start from available_spots / trials

# Start an infinite while loop (which we will break out of when satisfied ie > 0.97 probability
print("****** Output from Theoretical Probability Method *********")
while True:
    # Sum probabilities of having at least 'spots' participants turn up
    seminar_full_probability = sum(st.binom.pmf(k=i, n=spots_to_sell, p=p) for i in range(available_spots, spots_to_sell + 1))
    print(f"Probability of full session (≥ {available_spots}) with spots_to_sell={spots_to_sell}: {seminar_full_probability:.4f}")

    # Break out when satisfied (> 0.97 probability was given in the problem statement)
    if seminar_full_probability > target_probability:
        print(f"\nBy Theoretically Method => Minimum number of spots to sell for full session (≥ 8) = {spots_to_sell}")
        break

    # In case we didn't break out, increase the number of spots to sell
    spots_to_sell += 1


## Now solve the problem using Simulation Method by using function st.binom.rvs from scipy.stats 

# st.binom.rvs(n, p, size)
# → Generates random variates (samples) from a binomial distribution.
#   Each sample represents the number of successes in n independent Bernoulli trials 
#   with a success probability p.
#
# n → The number of independent trials per experiment (e.g., spots_to_sell).
# p → The probability of success in each trial.
# size → The number of experiments (i.e., how many samples to generate).


# Parameters
p = 0.96                    # probability of a participant turns up for the session is 0.96
available_spots = 8         # number of spots in seminar
spots_to_sell = 10          # start from available_spots / trials, change to get expected probability
experiments = 100000        # set to large number to get stable estimates

print("\n\n****************** Output from Simulation Method *********************")
# print(f'Occurences where session is full ie (i.e. 8 or more participants turn up)(out of {experiments} experiments): {sum(simulation>=8)}')
# print(f'Induced Probability by changing spots_to_sell to {spots_to_sell} is: {sum(simulation>=8)/experiments:.4f}')
# print(f"Minimum number of spots to sell: {spots_to_sell}")

for spots_to_sell in range (8,15):
    simulation = st.binom.rvs(n=spots_to_sell, p=p, size=experiments)
    induced_probability = sum(simulation>=8)/experiments
    print(f"Induced Probability with spots_to_sell={spots_to_sell} for full session (≥ {available_spots}): {induced_probability:.4f}")
    
    if induced_probability > 0.97:
        print(f"\nBy Simulation Method => Minimum number of spots to sell for full session (≥ 8) = {spots_to_sell}")
        break