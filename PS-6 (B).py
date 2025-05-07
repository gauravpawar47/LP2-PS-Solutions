# Job class to store job details
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

# Greedy Job Scheduling function
def job_scheduling(jobs, max_deadline):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Create a slot availability array (for each deadline)
    result = [None] * max_deadline
    total_profit = 0
    job_details = []

    # Go through all jobs and schedule them in available slots
    for job in jobs:
        for t in range(job.deadline - 1, -1, -1):  # Try the latest available slot
            if result[t] is None:  # If slot is free
                result[t] = job.id
                total_profit += job.profit
                job_details.append((job.id, job.profit))  # Keep track of job id and profit
                break

    # Output the result (jobs selected)
    scheduled_jobs = [job for job in result if job is not None]
    return scheduled_jobs, total_profit, job_details

# Example jobs with id, deadline, and profit
jobs = [
    Job('A', 4, 20),
    Job('B', 1, 10),
    Job('C', 1, 40),
    Job('D', 1, 30),
    Job('E', 3, 50),
]

# Maximum number of slots (based on the latest deadline)
max_deadline = 4

# Run the job scheduling
scheduled_jobs, total_profit, job_details = job_scheduling(jobs, max_deadline)

# Output scheduled jobs and profits
print("Scheduled jobs and their profits:")
for job_id, profit in job_details:
    print(f"Job {job_id}: Profit = {profit}")

print("\nScheduled jobs:", scheduled_jobs)
print(f"Total profit: {total_profit}")
