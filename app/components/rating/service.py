def submit_rating(rating):
    return {
        "message": "Rating submitted successfully",
        "score": rating.score
    }


def list_ratings():
    return [
        {"score": 5},
        {"score": 4}
    ]