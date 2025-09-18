
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]

@dataclass(frozen=True)
class Creatives:
  def __init__(self):
     self.headline: Optional[str] = None
     self.url: Optional[str] = None
  


class CampaignBuilder:
    def __init__(self):
      # self.campaign = Campaign
      self.name: Optional[str] = None
      self.channel: Optional[str] = None
      self.daily_budget: Optional[float] = None
      self.start_date: Optional[date] = None
      self.end_date: Optional[date] = None
      self.target_audience: Optional[Dict[str, Any]] = {}
      self.creatives: Optional[Creatives] = []
      self.tracking: Optional[Dict[str, str]] = {}


      # TODO
      pass

    def with_name(self, name: str):
      # TODO
      # if not name:
      #   return
      
      self.name = name
      return self

    def with_channel(self, channel: str):

      self.channel = channel
      return self

    def with_budget(self, daily_budget: float):

      self.daily_budget = daily_budget
      return self

    def with_dates(self, start_date, end_date=None):
      
      self.start_date = start_date
      self.end_date = end_date
      return self

    def with_audience(self, **kwargs):

      for x,y in kwargs.items():
        self.target_audience.append({x:y})


      return self

    def add_creative(self, headline: str, image_url: str):
      
      if headline:
        self.creatives.headline = headline
      if image_url:
        self.creatives.url = image_url

      return self

    def with_tracking(self, **kwargs):

      for x,y in kwargs.items():
        self.tracking.append({x:y})

      return self

    def build(self) -> Campaign:
      # TODO: Validations and return Campaign instance

      if None in (self.name, self.channel, self.daily_budget, self.start_date):
            raise ValueError("Missing required fields")
      
      if len(self.creatives) < 1:
         raise ValueError("Missing required creative")
      
      if self.end_date and self.end_date < self.start_date:
         raise ValueError("Invalid end date")
      
# - A campaign must have a name.
# - A campaign must have a channel.
# - The daily budget must be provided and must be positive.
# - The start date is required.
# - If an end date is provided, the start date must be before or equal to the end date.
# - At least one creative (headline and image URL) is required.
      
      return Campaign(
        name=self.name,
        channel=self.channel,
        daily_budget=self.daily_budget,
        start_date=self.start_date,
        end_date=self.end_date,
        target_audience=self.target_audience,
        creatives=self.creatives,
        tracking=self.tracking
      )
