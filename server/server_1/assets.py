from dagster import asset, get_dagster_logger


@asset
def asset_1() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_1')


@asset(deps=[asset_1])
def asset_2() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_2 to trigger after asset_1 in the same job')


@asset(deps=[asset_1])
def asset_3() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_3 to trigger after asset_1 in the same job parallel to asset_2')


@asset
def asset_4() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_4 to trigger after job with asset_1 will be finished')


@asset(deps=[asset_4])
def asset_5() -> None:
    logger = get_dagster_logger()
    logger.info('This is asset_5 to trigger after asset_4 in the same job')
