"""
pipeline.py → aquí “armas” el pipeline conectando tus funciones (nodes) con los datasets del catálogo.
"""

from kedro.pipeline import Node, Pipeline  # noqa


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([])
