
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """

    _instance = None

    def __new__(cls, initial_amount: float = 0.0):

      if cls._instance is None and initial_amount > 0:
         cls._instance = super().__new__(cls)
         cls._instance._balance = initial_amount
      return cls._instance


    def allocate(self, amount: float) -> None:
      if amount > 0 and self._balance - amount > 0:
        self._balance -= amount
      else:
        raise ValueError("Cannot allocate more than budget")
  
      return self._balance

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
