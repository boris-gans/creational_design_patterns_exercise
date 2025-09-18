
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign

# Functional requirements:
# - Campaigns should allocate their daily budget to the global budget.
# - When a campaign is created, a external id should be returned. This id should have a prefix with the initial of the channel i.e. For facebook ads --> "f_<some_id>"
# - Two clients are needed: FacebookAds and GoogleAds
# - If different channel client is created, and error should arise.

class ChannelClient(ABC):
    # _id_counter = uuid4()

    def __init__(self, name: str):
      self.name = name
      self.budget = GlobalBudget()

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
      pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
      pass


class GoogleAdsClient(ChannelClient):
  def __init__(self):
     super().__init__("google")
  
  def create_campaign(self, campaign):
    self.budget.allocate(campaign.daily_budget)
    return f"g-{uuid4().hex}"

  def pause_campaign(self, campaign_id):
    print(f"Paused Google campaign with id {campaign_id}")


class FacebookAdsClient(ChannelClient):
  def __init__(self):
     super().__init__("facebook")

  def create_campaign(self, campaign):
    self.budget.allocate(campaign.daily_budget)
    return f"f-{uuid4().hex}"

  def pause_campaign(self, campaign_id):
    print(f"Paused Facebook campaign with id {campaign_id}")

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
      if channel.lower() == "google":
         return GoogleAdsClient()
      elif channel.lower() == "facebook":
         return FacebookAdsClient()
      else:
         raise ValueError("Improper channel entered")