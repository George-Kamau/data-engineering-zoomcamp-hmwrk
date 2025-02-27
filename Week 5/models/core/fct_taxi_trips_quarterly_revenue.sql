{{
    config(
        materialized='table'
    )
}}

select 
extract(year from pickup_datetime) as year,
extract(quarter from pickup_datetime) as quarter,
concat(cast(extract(year from pickup_datetime) as string), 
           '/Q', 
           cast(extract(quarter from pickup_datetime) as string)) as  year_quarter,
extract(month from pickup_datetime) as month,
*
 from {{ref("fact_trips")}}