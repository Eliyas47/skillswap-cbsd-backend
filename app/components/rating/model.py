class RatingModel:
    def __init__(self, reviewer_id, reviewed_user_id, score, feedback):
        self.reviewer_id = reviewer_id
        self.reviewed_user_id = reviewed_user_id
        self.score = score
        self.feedback = feedback