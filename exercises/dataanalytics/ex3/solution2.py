from scipy import stats as st
n, p, size = 10, 0.5, 5
print(st.binom.rvs(n, p, size))

