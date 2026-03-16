class ChatMessageModel:
    def __init__(self, sender_id, receiver_id, message):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message