{{
    config(
        materialized='view'
    )
}}

select 
*
from {{source('staging','fhv_tripdata_1')}}
where dispatching_base_num is not null