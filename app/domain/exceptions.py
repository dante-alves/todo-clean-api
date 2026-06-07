class DomainExceptionError(Exception):
    pass

class TaskNotFoundError(DomainExceptionError):
    pass

class UnauthorizedAccessError(DomainExceptionError):
    pass

class SubtasksPendingError(DomainExceptionError):
    pass

class TagAlreadyExistsError(DomainExceptionError):
    pass

class EmailAlreadyExistsError(DomainExceptionError):
    pass

class InvalidCredentialsError(DomainExceptionError):
    pass