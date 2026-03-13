class SwapRequestModel:
    def __init__(self, requester_id, receiver_id, skill_offered, skill_requested):
        self.requester_id = requester_id
        self.receiver_id = receiver_id
        self.skill_offered = skill_offered
        self.skill_requested = skill_requested