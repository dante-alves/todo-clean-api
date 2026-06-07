from enum import Enum

class Status(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"