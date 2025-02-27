{{
    config(
        materialized='table'
    )
}}

select
*,
timestamp_diff(dropoff_datetime, pickup_datetime,SECOND) as trip_duration
from {{ref('dim_fhv_trips')}} as fhv_trips


