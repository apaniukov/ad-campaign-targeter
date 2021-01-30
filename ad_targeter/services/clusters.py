from typing import Any, Dict, List, Optional

from iso3166 import countries as iso_countries  # type: ignore

from ad_targeter.model import CountriesClusters, countries_clusters


class ClusterPresenter:
    def __init__(self, clusters: CountriesClusters) -> None:
        self.countries_clusters = clusters

    def __call__(
        self, cluster_id: int, countries: List[str], full_names: Optional[bool] = False
    ) -> Dict[str, Any]:
        result = {
            "cluster_id": cluster_id,
            "countries": countries,
        }
        if full_names:
            result["countries_full_name"] = [
                self.get_full_name(country) for country in countries
            ]

        return result

    @staticmethod
    def get_full_name(country: str) -> str:
        return (
            iso_info.name
            if (iso_info := iso_countries.get(country, False))
            else country
        )


cluster_presenter = ClusterPresenter(countries_clusters)
