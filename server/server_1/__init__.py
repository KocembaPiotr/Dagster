from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    SkipReason,
    DagsterRunStatus,
    RunStatusSensorContext,
    run_status_sensor,
    RunRequest
)
from . import assets

all_assets = load_assets_from_modules([assets])

job_1 = define_asset_job(name="job_1", selection=[assets.asset_1, assets.asset_2, assets.asset_3])
job_2 = define_asset_job(name="job_2", selection=[assets.asset_4, assets.asset_5])

schedule_1 = ScheduleDefinition(
    job=job_1,
    cron_schedule="*/15 * * * *",
)


@run_status_sensor(
    run_status=DagsterRunStatus.SUCCESS,
    request_job=job_2,
)
def report_status_sensor(context: RunStatusSensorContext):
    if context.dagster_run.job_name == job_1.name:
        return RunRequest()
    else:
        return SkipReason("job_2 success run!")


defs = Definitions(
    assets=all_assets,
    jobs=[job_1, job_2],
    schedules=[schedule_1],
    sensors=[report_status_sensor],
)
