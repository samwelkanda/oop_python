class DatabaseService:
    def get_data(self):
        return "Data from database"


class UserController:
    def __init__(self, db_service):
        self.db_service = db_service

    def handle_request(self):
        data = self.db_service.get_data()
        return data


# Usage
db_service = DatabaseService()
user_controller = UserController(db_service)