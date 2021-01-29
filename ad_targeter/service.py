from typing import Dict, Generator, List

from ad_targeter.schemas import AdCampaign, AdCampaignsRequest


class ClusteringService:
    def classify_campaign(self, campaign: AdCampaign) -> int:
        return 1

    def __call__(self, campaingns: AdCampaignsRequest) -> Generator[int, None, None]:
        return (self.classify_campaign(campaingn) for campaingn in campaingns)


class ClusteringPresenter:
    def __call__(
        self, campaigns: AdCampaignsRequest, clusters: Generator[int, None, None]
    ) -> List[Dict[str, int]]:
        return [
            {
                "campaign_id": campaign.campaign_id,
                "cluster_id": cluster,
            }
            for campaign, cluster in zip(campaigns, clusters)
        ]


clusterer = ClusteringService()
presenter = ClusteringPresenter()
