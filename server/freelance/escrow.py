class MilestoneStateMachine:
    def __init__(self):
        self.state = 'HELD'
        self.release_percentage = 0.2  # 20% fund release

    def submit_work(self):
        if self.state == 'HELD':
            self.state = 'WORK_SUBMITTED'
            print("Work has been submitted.")
        else:
            raise Exception("Can't submit work in the current state.")

    def approve_client(self):
        if self.state == 'WORK_SUBMITTED':
            self.state = 'CLIENT_APPROVED'
            self.release_funds(self.release_percentage)
            print("Client has approved the work and 20% funds released.")
        else:
            raise Exception("Can't approve work in the current state.")

    def release_funds(self, percentage):
        # Logic to release funds here
        print(f"{percentage * 100}% of funds released.")

    def release_complete(self):
        if self.state == 'CLIENT_APPROVED':
            self.state = 'RELEASED'
            print("All funds released.")
        else:
            raise Exception("Can't release complete funds in the current state.")

    def get_state(self):
        return self.state

# Example usage:
# m = MilestoneStateMachine()
# m.submit_work()
# m.approve_client()
# m.release_complete()