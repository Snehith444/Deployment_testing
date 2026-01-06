class DomainError(Exception):
    """Base class for domain exceptions"""


class ValidationError(DomainError):
    pass


class NotFoundError(DomainError):
    pass
