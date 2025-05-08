### 📘 PS-6 (B): Job Scheduling with Maximum Profit

---

### **Job Scheduling Problem (Theory)**

The **Job Scheduling** problem involves selecting jobs to maximize the total profit. Given a list of jobs, each with a deadline and profit, the goal is to schedule the jobs in a way that maximizes the total profit while respecting the constraints on job deadlines. 

Here are the 4 main points to understand about Job Scheduling:

---

### 1. **Greedy Approach**

* The job scheduling problem is solved using a **greedy algorithm**, where we prioritize jobs with higher profit and schedule them in the latest available time slots (before their deadline).
* The algorithm maximizes profit by ensuring that the highest-profit jobs are selected first, and each job is scheduled as late as possible to leave room for other jobs.

---

### 2. **Steps of the Algorithm**

* Sort the jobs based on profit in decreasing order.
* Create a slot availability array for each deadline.
* Try to schedule each job in the latest available slot before its deadline.
* Repeat this process for all jobs.

---

### 3. **Optimality**

* The greedy approach ensures that the total profit is maximized, as it selects the most profitable jobs that can be scheduled within the given time slots.

---

### **Summary:**

The Job Scheduling problem is solved using a greedy algorithm that schedules jobs with the highest profit in the latest available slots before their deadline. This ensures that the total profit is maximized.

---

### CODE

---

## 🧠 Goal of the Program

Implement a Job Scheduling function to select jobs that can be completed within their deadlines to maximize total profit. The jobs are represented using a `Job` class with details such as job id, deadline, and profit.

### 1. **Job Class Definition**

```python
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
````

* The `Job` class defines a job with an `id`, a `deadline`, and a `profit`. The constructor initializes these attributes.

---

### 2. **Job Scheduling Function**

```python
def job_scheduling(jobs, max_deadline):
```

* The function `job_scheduling` takes a list of `jobs` and `max_deadline` as input. The goal of this function is to select jobs and schedule them to maximize profit.

---

### 3. **Sort Jobs Based on Profit**

```python
    jobs.sort(key=lambda x: x.profit, reverse=True)
```

* The jobs are sorted in descending order of profit using Python’s `sort()` function with a key function. This ensures that the most profitable jobs are considered first.

---

### 4. **Initialize Slot Availability and Variables**

```python
    result = [None] * max_deadline
    total_profit = 0
    job_details = []
```

* `result = [None] * max_deadline`: Initializes an array `result` to represent the available slots for each job. Each slot is initially set to `None`, indicating that it's empty.
* `total_profit = 0`: Initializes the `total_profit` to keep track of the total profit of scheduled jobs.
* `job_details = []`: Initializes a list to keep track of the scheduled job ids and their profits.

---

### 5. **Main Scheduling Loop**

```python
    for job in jobs:
        for t in range(job.deadline - 1, -1, -1):
            if result[t] is None:
                result[t] = job.id
                total_profit += job.profit
                job_details.append((job.id, job.profit))
                break
```

* The outer loop goes through each job.
* The inner loop tries to schedule the job in the latest available slot before its deadline.

  * If a slot is available (`None`), the job is scheduled in that slot, the profit is added to `total_profit`, and the job id and profit are stored in `job_details`.

---

### 6. **Output the Result**

```python
    scheduled_jobs = [job for job in result if job is not None]
    return scheduled_jobs, total_profit, job_details
```

* `scheduled_jobs`: Filters out the `None` values from `result`, leaving only the jobs that were scheduled.
* The function returns `scheduled_jobs` (list of scheduled jobs), `total_profit` (the total profit of scheduled jobs), and `job_details` (a list of job ids and their profits).

---

### Example Jobs Definition

```python
jobs = [
    Job('A', 4, 20),
    Job('B', 1, 10),
    Job('C', 1, 40),
    Job('D', 1, 30),
    Job('E', 3, 50),
]
```

* This is a list of `Job` objects, each representing a job with a specific `id`, `deadline`, and `profit`.

---

### Running the Job Scheduling Function

```python
max_deadline = 4
scheduled_jobs, total_profit, job_details = job_scheduling(jobs, max_deadline)
```

* The `job_scheduling()` function is called with the list of jobs and the maximum deadline (`4` in this case). It returns the scheduled jobs, total profit, and job details.

---

### Output the Results

```python
print("Scheduled jobs and their profits:")
for job_id, profit in job_details:
    print(f"Job {job_id}: Profit = {profit}")

print("\nScheduled jobs:", scheduled_jobs)
print(f"Total profit: {total_profit}")
```

* The scheduled jobs and their profits are printed, showing each job with its associated profit.
* The total profit from all scheduled jobs is also printed.

---

### Example Output

```plaintext
Scheduled jobs and their profits:
Job C: Profit = 40
Job E: Profit = 50
Job A: Profit = 20

Scheduled jobs: ['C', 'E', 'A']
Total profit: 110
```

---

### ALGORITHM

```
ALGORITHM JOB_SCHEDULING
-------------------------
1. Define a class `Job` with attributes `id`, `deadline`, and `profit`.
2. Define a function `job_scheduling(jobs, max_deadline)`:
   a. Sort the jobs in decreasing order of profit.
   b. Initialize a list `result` to track the scheduled jobs.
   c. Initialize `total_profit` and `job_details` to store the total profit and job details.
   
3. For each job:
   a. Try to schedule the job in the latest available slot before its deadline.
   b. If a slot is free, schedule the job, update the total profit, and record the job details.
   
4. Return the scheduled jobs, total profit, and job details.

5. Print the scheduled jobs and their profits, along with the total profit.

END
```
