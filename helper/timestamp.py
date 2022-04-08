from datetime import datetime


class Timestamp:
    @staticmethod
    def unix_time_millis_now():
        timestamp = int(datetime.utcnow().timestamp())
        return timestamp
