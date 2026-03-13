def create_swap_request(request):
    return {
        "message": "Swap request created successfully",
        "details": request.skill_offered
    }


def list_swap_requests():
    return [
        {"status": "pending"},
        {"status": "accepted"}
    ]