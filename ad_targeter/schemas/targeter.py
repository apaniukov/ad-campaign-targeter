from typing import List

from pydantic import BaseModel


class AdCampaign(BaseModel):
    campaign_id: int
    targeting: List[str]

    class Config:
        schema_extra = {
            "example": {
                "campaign_id": 123321,
                "targeting": ["RU", "DE"],
            }
        }


class AdCampaignsRequest(BaseModel):
    __root__: List[AdCampaign]

    class Config:
        schema_extra = {
            "example": [
                {
                    "campaign_id": 123321,
                    "targeting": ["RU", "DE"],
                }
            ]
        }

    def __iter__(self):
        yield from self.__root__


class CampaignPrediction(BaseModel):
    campaign_id: int
    cluster_id: int

    class Config:
        schema_extra = {
            "example": {
                "campaign_id": 123321,
                "cluster_id": 7,
            }
        }


class AdCampaignsResponse(BaseModel):
    __root__: List[CampaignPrediction]

    class Config:
        schema_extra = {
            "example": [
                {
                    "campaign_id": 123321,
                    "cluster_id": 7,
                }
            ]
        }
