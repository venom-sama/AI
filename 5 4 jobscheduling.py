def job_scheduling(jobs):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    time_slots = [-1] * (max_deadline + 1)

    for job in jobs:
        profit = job[2]
        deadline = job[1]

        # Find the maximum available time slot before the deadline
        for i in range(deadline, 0, -1):
            if i <= max_deadline and time_slots[i] == -1:
                time_slots[i] = job[0]  # Schedule the job
                break

    scheduled_jobs = [time_slots[i] for i in range(1, max_deadline + 1) if time_slots[i] != -1]
    total_profit = sum([jobs[job_id - 1][2] for job_id in scheduled_jobs])

    return scheduled_jobs, total_profit

def print_schedule(jobs, total_profit):
    print("Scheduled Jobs:", jobs)
    print("Total Profit:", total_profit)

def main():
    jobs = []
    while True:
        print("\nJob Scheduling Problem Menu:")
        print("1. Add Job")
        print("2. Schedule Jobs")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            job_id = int(input("Enter Job ID: "))
            deadline = int(input("Enter Deadline: "))
            profit = int(input("Enter Profit: "))
            jobs.append((job_id, deadline, profit))
        elif choice == "2":
            if jobs:
                scheduled_jobs, total_profit = job_scheduling(jobs)
                print_schedule(scheduled_jobs, total_profit)
            else:
                print("No jobs added yet. Please add jobs first.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
