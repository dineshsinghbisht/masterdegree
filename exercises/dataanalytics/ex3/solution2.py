from scipy import stats as st

n, p, size = 10, 0.5, 5
print("Type of size:", type(size))

#a = st.binom.rvs(n=n, p=p, size=size)
a = st.binom.rvs(n, p, size=size)
print("a =", a)
print("type(a) =", type(a))


# seat_capacity = 10
# p_turnup = 0.95

# tickets_sold = seat_capacity  # Start with 10 tickets

# while True:
#     # Calculate probability that at least seat_capacity passengers show up
#     probs = [st.binom.pmf(k, tickets_sold, p_turnup) for k in range(seat_capacity, tickets_sold + 1)]
#     prob_full = sum(probs)

#     print(f"Tickets sold: {tickets_sold}, P(flight full): {prob_full:.6f}")
    
#     if prob_full > 0.99:
#         print(f"\n✅ Minimum tickets to sell = {tickets_sold}")
#         break

#     tickets_sold += 1



# seat_capacity = 8        # total spots
# p_turnup = 0.96          # probability a participant shows up

# tickets_sold = seat_capacity  # start with selling exactly 8

# while True:
#     # Sum probabilities P(X = k) for k = 8, 9, ..., tickets_sold
#     probs = [st.binom.pmf(k, tickets_sold, p_turnup) 
#              for k in range(seat_capacity, tickets_sold + 1)]
#     prob_full = sum(probs)

#     print(f"Tickets sold: {tickets_sold}, P(session full): {prob_full:.6f}")

#     if prob_full > 0.97:
#         print(f"\n✅ Minimum spots to sell = {tickets_sold}")
#         break

#     tickets_sold += 1
