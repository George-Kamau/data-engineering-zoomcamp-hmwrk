## Week 1 SQL queries

### Question 3
**How many trips were there in October 2019 for different trip distances?**

- Up to 1 mile: 104838
- In between 1 (exclusive) and 3 miles (inclusive): 199013
- In between 3 (exclusive) and 7 miles (inclusive): 109645
- In between 7 (exclusive) and 10 miles (inclusive): 27688
- Over 10 miles: 35202

SQL Query:
```sql
SELECT
count(*)
FROM public."green_tripdata_2019-10" as main
WHERE trip_distance <= 1
--WHERE trip_distance > 1 AND trip_distance <= 3
--WHERE trip_distance > 3 AND trip_distance <= 7
--WHERE trip_distance > 7 AND trip_distance <= 10
--WHERE trip_distance > 10
```

### Question 4
**What is the latest pickup time in October 2019?**

Answer: "2019-10-31 23:23:41"

SQL Query:

```sql
SELECT
lpep_pickup_datetime,
max(trip_distance) as "Trip Distance"
FROM public."green_tripdata_2019-10" as main
GROUP BY lpep_pickup_datetime
order by "Trip Distance" desc
```

### Question 5
**Which zones had the highest total amount on October 18, 2019?**

Answer: East Harlem North, East Harlem South, Morningside Heights

SQL Query:

```sql
with cte as(
SELECT
--"PULocationID",
lk."Zone",
sum(total_amount) as "Total Amount"
FROM public."green_tripdata_2019-10" as main
left join public.taxi_zone_lookup as lk on main."PULocationID"=lk."LocationID"
where date(lpep_pickup_datetime) = '2019-10-18'
group by "PULocationID", lk."Zone"
)
select * from cte
where "Total Amount">13000
order by "Total Amount" desc;
```

### Question 6
**Which zone had the highest tip amount for pickups in East Harlem North in October 2019?**

Answer: JFK Airport

SQL Query:
```sql
SELECT
PUlk."Zone" as "Pick Up Zone",
DOlk."Zone" as "Drop off Zone",
tip_amount as "Tip Amount"
FROM public."green_tripdata_2019-10" as main
left join public.taxi_zone_lookup as PUlk on main."PULocationID"=PUlk."LocationID"
left join public.taxi_zone_lookup as DOlk on main."DOLocationID"=DOlk."LocationID"
where PUlk."Zone"='East Harlem North'
and EXTRACT(MONTH FROM lpep_pickup_datetime)=10
order by "Tip Amount" desc
```
