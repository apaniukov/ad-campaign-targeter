import csv
from typing import Dict, Generator, List, Union

from iso3166 import countries  # type: ignore

from settings import config


class CountriesClusters:
    def __init__(self) -> None:
        self.file = config.cluster_file
        self.countries = {
            country: {
                "full_name": countries.get(country).name
                if country in countries
                else None,
                "cluster_id": cluster_id,
            }
            for country, cluster_id in self._get_countries()
        }

    def _get_countries(self) -> Generator[List[str], None, None]:
        yield from self._csv_reader()

    def _csv_reader(self) -> Generator[List[str], None, None]:
        with open(self.file) as f:
            reader = csv.reader(f)
            yield from reader

    def __getitem__(self, item: str) -> Dict[str, Union[str, int]]:
        return self.countries[item]

    def get_cluster(self, country):
        return self.countries[country]["cluster_id"]


countries_clusters = CountriesClusters()
