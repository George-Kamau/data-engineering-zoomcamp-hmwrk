{{
    config(
        materialized='table'
    )
}}

select
fhv_trips.*,
extract(year from pickup_datetime) as year,
extract(quarter from pickup_datetime) as quarter,
concat(cast(extract(year from pickup_datetime) as string), 
           '/Q', 
           cast(extract(quarter from pickup_datetime) as string)) as  year_quarter,
extract(month from pickup_datetime) as month,
pickup_zone.borough as pickup_borough, 
pickup_zone.zone as pickup_zone, 
dropoff_zone.borough as dropoff_borough, 
dropoff_zone.zone as dropoff_zone,  
from {{ref('stg_fhv_trips')}} as fhv_trips
inner join {{ref('dim_zones')}} as pickup_zone on fhv_trips.PUlocationid = pickup_zone.locationid
inner join {{ref('dim_zones')}} as dropoff_zone on fhv_trips.DOlocationid = dropoff_zone.locationid
