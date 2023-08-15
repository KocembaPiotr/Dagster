from dagster import asset, get_dagster_logger


@asset
def asset_1() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_1')
