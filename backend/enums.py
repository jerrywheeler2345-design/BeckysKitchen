import enum

class UserRole(enum.Enum):
    admin = "admin"
    customer = "customer"


class OrderStatus(enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"