from uuid import uuid4

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_session(self, session_id):
        return self.sessions.setdefault(session_id, [])

    def update_session(self, session_id, user_msg, bot_msg):
        self.sessions.setdefault(session_id, []).append(
            {"user": user_msg, "bot": bot_msg}
        )

session_manager = SessionManager()
