from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4
from app.domain.value_objects.priority import Priority
from app.domain.value_objects.status import Status

@dataclass
class Task:
    id: UUID = field(default_factory=uuid4)
    user_id = UUID
    parent_task_id: UUID | None = None
    title: str
    description: str | None = None
    status: Status = Status.todo
    priority: Priority = Priority.medium
    due_date: datetime | None = None
    completed_at: datetime | None = None
    created_at: datetime = field(default_factory=datetime.now(datetime.timezone.utc))
    updated_at: datetime = field(default_factory=datetime.now(datetime.timezone.utc))