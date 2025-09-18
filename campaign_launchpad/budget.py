
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
# Functional requirements:
# - Ensure there is only a single bugdet
# - Ensure bugdet cannot go below zero
# - Allow no negative allocations
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
      # TODO: Singleton pattern implementation

      if cls._instance is None and initial_amount > 0:
         cls._instance = super().__new__(cls)
         cls._instance._balance = initial_amount
      return cls._instance
      # pass

    def allocate(self, amount: float) -> None:
      # TODO: Allocate amount from the budget
      if amount > 0:
        self._balance -= amount
      return self._balance

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
