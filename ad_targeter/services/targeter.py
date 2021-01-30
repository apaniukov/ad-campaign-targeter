from collections import Counter
from typing import Dict, Generator, List

from ad_targeter.model import CountriesClusters, countries_clusters
from ad_targeter.schemas.targeter import AdCampaign, AdCampaignsRequest


class TargeterService:
    def __init__(self, clusters: CountriesClusters) -> None:
        self.countries_clusters = clusters

    def classify_campaign(self, campaign: AdCampaign) -> int:
        counter = Counter(
            self.countries_clusters.get_cluster(country)
            for country in campaign.targeting
        )
        return counter.most_common(1)[0][0]

    def __call__(self, campaingns: AdCampaignsRequest) -> Generator[int, None, None]:
        return (self.classify_campaign(campaingn) for campaingn in campaingns)


class TargeterPresenter:
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


targeter = TargeterService(countries_clusters)
presenter = TargeterPresenter()
