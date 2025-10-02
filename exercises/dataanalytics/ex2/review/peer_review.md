# Peer Review Comments

## Problem - 1
- **Feedback on the Solution**: The code executes successfully, and all results are as expected for all the tasks. The solution is explained clearly with comments — nice work.  
  However, while reviewing, I noticed that the contents of the file **private/exrc_02/data/XXXXX_prob01_profiles.csv** are different from mine. As a result, the output does not match my results. I also observed that the solution includes additional logic to remove prefixes (ie Mr., Dr.) or suffixes (e.g. (ie Phd, DDS)) from the **name** column. This logic is not present in my solution as my input file, column **name** does not contains prefix or suffix. 
  This highlights an important issue: if the reviewee were to run my solution with his/her input file, it would not work correctly and evlaute my solution based on this. At times, this makes it difficult to execute another person’s solution with different input data.
- **Evaluation**: I would rate the solution **5 points**.  
- **Self-Evaluation**: I would also rate my own work **5 points**, as all outputs were as expected and the code was explained with proper comments.

---

## Problem - 2
- **Feedback on the Solution**: The solution is acceptable as it produces the expected outputs for both tasks. The comments around the code are helpful in explaining the flow and logic.  
  However, once again, the input data is different from mine, which explains why our outputs do not match. Despite this, the logic itself looks correct.
- **Evaluation**: I would rate the solution **5 points**.   
- **Self-Evaluation**: I would also rate my own work **5 points**, as I completed all the tasks as required and the results are correct. I even ran the reviewee’s solution with my data and obtained the same result, which confirms that my solution is also correct.

---

## Problem - 3
- **Feedback on the Solution**: The solution is almost correct but due to but due to a small mistake the output is not accurate. While creating the DataFrame for the `awayTeam`, the values of `awayScore` and `homeScore` were swapped.

```python
away = pd.DataFrame({"team": df["awayTeam"], "awayScore": df["awayScore"], "homeScore": df["homeScore"], "games": df["games"]})
```

Must be

```python
away = pd.DataFrame({"team": df["awayTeam"], "awayScore": df["homeScore"], "homeScore": df["awayScore"] ,'games': df['games']})
```
- **Evaluation**: I would rate the solution **3 points**.  
- **Self-Evaluation**: I would rate my own work **5 points**, as I completed the task as required and my output was correct. I also applied the fix shown above to the reviewee’s solution and ran it with my input data. The results then matched my original output exactly.

---

## Problem - 4
- **Feedback on the Solution**: The solution is acceptable, as it produces the expected output and the program runs without any issues.
- **Evaluation**: I would rate the solution **5 points**.  
- **Self-Evaluation**: I would rate my own work **5 points**, as I completed the task successfully and obtained the expected output.

---

## Problem - 5
- **Feedback on the Solution**: The solution looks good, as the resulting table is meaningful. However, it would have been better to include a short summary (one or two sentences) describing the insights from the table.
- **Evaluation**: I would rate the solution almost **5 points**.  
- **Self-Evaluation**: I would rate my own work **5 points**, as I completed the task, created meaningful data, and provided a summary (since we did not create any graphs for visualization).