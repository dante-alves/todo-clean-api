from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.task import Task

class ITaskRepository(ABC):
    @abstractmethod
    async def create(self, task: Task) -> Task: ...

    @abstractmethod
    async def get_by_id(self, task_id: UUID, user_id: UUID) -> Task | None: ...

    @abstractmethod
    async def list_by_user(self, user_id: UUID, **filters) -> list[Task]: ...

    @abstractmethod
    async def update(self, task: Task) -> Task: ...

    @abstractmethod
    async def delete(self, task_id: UUID) -> None: ...

    @abstractmethod
    async def delete_completed(self, user_id: UUID) -> int: ...