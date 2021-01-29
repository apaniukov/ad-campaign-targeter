from fastapi import APIRouter

from ad_targeter.schemas import AdCampaignsRequest, AdCampaignsResponse
from ad_targeter.service import clusterer, presenter

router = APIRouter(prefix="/target", tags=["target"])


@router.post("", response_model=AdCampaignsResponse)
def get_targets(ad_campaigns: AdCampaignsRequest):
    clusters = clusterer(ad_campaigns)
    return presenter(ad_campaigns, clusters)
