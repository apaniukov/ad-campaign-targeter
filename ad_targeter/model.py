import csv
from itertools import groupby
from pathlib import Path
from typing import Dict, Generator, List, Tuple

from settings import config


class CountriesClusters:
    def __init__(self) -> None:
        self.file: Path = config.CLUSTER_FILE
        self.country_to_cluster: Dict[str, int] = {
            country: cluster_id for country, cluster_id in self._get_countries()
        }
        self.cluster_to_countries: Dict[int, List[str]] = {
            cluster_id: [country[0] for country in countries]
            for cluster_id, countries in groupby(
                sorted(self.country_to_cluster.items(), key=lambda x: x[1]),
                key=lambda x: x[1],
            )
        }

    def _get_countries(self) -> Generator[Tuple[str, int], None, None]:
        yield from self._csv_reader()

    def _csv_reader(self) -> Generator[Tuple[str, int], None, None]:
        with open(self.file) as f:
            reader = csv.reader(f)
            yield from ((row[0], int(row[1])) for row in reader)

    def get_cluster(self, country):
        return self.country_to_cluster[country]


countries_clusters = CountriesClusters()
