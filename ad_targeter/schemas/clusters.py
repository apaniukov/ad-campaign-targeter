from typing import List, Optional

from pydantic import BaseModel


class ClusterResponse(BaseModel):
    cluster_id: int
    countries: List[str]
    countries_full_name: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "cluster_id": 7,
                "countries": ["RU"],
                "countries_full_name": ["Russia"],
            }
        }
