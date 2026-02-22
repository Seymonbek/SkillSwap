import random

# Constants for data generation
total_users = 10
skills_range = 20
sessions_range = 5
jobs_range = 3

# Generate test users
users = [
    {"id": i, "name": f"User {i}", "email": f"user{i}@example.com"}
    for i in range(1, total_users + 1)
]

# Generate test skills
skills = [
    {"id": i, "name": f"Skill {i}"}
    for i in range(1, skills_range + 1)
]

# Generate test sessions
sessions = [
    {"id": i, "title": f"Session {i}", "description": f"Description for session {i}", "user_id": random.randint(1, total_users)}
    for i in range(1, sessions_range + 1)
]

# Generate test jobs
jobs = [
    {"id": i, "title": f"Job {i}", "requirements": [random.choice(skills)["name"] for _ in range(3)], "session_id": random.randint(1, sessions_range)}
    for i in range(1, jobs_range + 1)
]

# Output the generated data
if __name__ == '__main__':
    print("Users:", users)
    print("Skills:", skills)
    print("Sessions:", sessions)
    print("Jobs:", jobs)