from typing import List, Optional

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from ad_targeter.model import countries_clusters
from ad_targeter.schemas.clusters import ClusterResponse
from ad_targeter.services.clusters import cluster_presenter

router = APIRouter(prefix="/clusters", tags=["clusters"])


@router.get("", response_model=List[ClusterResponse])
def get_all_clusters(full_names: Optional[bool] = False):
    return [
        cluster_presenter(cluster, countries, full_names)
        for cluster, countries in countries_clusters.cluster_to_countries.items()
    ]


@router.get("/{cluster_id}", response_model=ClusterResponse)
def get_cluster(cluster_id: int, full_names: Optional[bool] = False):
    try:
        countries = countries_clusters.cluster_to_countries[cluster_id]
    except KeyError:
        raise HTTPException(404, f"There is no cluster with id {cluster_id}.")
    return cluster_presenter(cluster_id, countries, full_names)
