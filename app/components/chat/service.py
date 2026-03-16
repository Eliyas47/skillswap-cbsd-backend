def send_message(message):
    return {
        "message": "Message sent successfully",
        "content": message.message
    }


def get_messages():
    return [
        {"message": "Hello"},
        {"message": "Skill exchange confirmed"}
    ]