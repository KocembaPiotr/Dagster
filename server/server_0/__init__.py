from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)
from .assets_1 import assets_1
from .assets_2 import assets_2

assets = load_assets_from_modules([assets_1, assets_2])
job_1 = define_asset_job(name="job_1", selection=[assets_1.asset_1])
job_2 = define_asset_job(name="job_2", selection=[assets_2.asset_2])

schedule_1 = ScheduleDefinition(
    job=job_1,
    cron_schedule="*/15 * * * *",
)

schedule_2 = ScheduleDefinition(
    job=job_2,
    cron_schedule="*/30 * * * *",
)

defs = Definitions(
    assets=assets,
    jobs=[job_1, job_2],
    schedules=[schedule_1, schedule_2],
)
