from fastapi import APIRouter

from ad_targeter.schemas.targeter import (AdCampaignsRequest,
                                          AdCampaignsResponse)
from ad_targeter.services.targeter import presenter, targeter

router = APIRouter(prefix="/target", tags=["target"])


@router.post("", response_model=AdCampaignsResponse)
def get_targets(ad_campaigns: AdCampaignsRequest):
    clusters = targeter(ad_campaigns)
    return presenter(ad_campaigns, clusters)
