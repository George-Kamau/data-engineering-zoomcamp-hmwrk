# Data Engineering Zoomcamp Homework - Week 3 Queries

### Creating an External Table
```sql
CREATE OR REPLACE EXTERNAL TABLE `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_external`
OPTIONS (
  format = 'Parquet',
  uris = ['gs://de_practice_hw_wk3/yellow_tripdata_2024-*.parquet']);
```

### Creating a Regular Table
```sql
CREATE OR REPLACE TABLE `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`
AS SELECT * FROM `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_external`;
```

### Question 1
**Query:**
```sql
SELECT count(*) FROM `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`;
```


### Question 2
**Query:**
```sql
Select count(distinct PULocationID) from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`; 
Select count(distinct PULocationID) from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_external`;
```


### Question 3
**Query:**
```sql
Select PULocationID from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`;
Select PULocationID, DOLocationID from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`;
```


### Question 4
**Query:**
```sql
Select count(*) from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`
where fare_amount=0;
```

### Question 5
**Query:**
```sql
CREATE OR REPLACE TABLE `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_partitioned_and_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular`;
```

### Question 6
**Query:**
```sql
Select distinct VendorID from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_regular` --310.24MB 
where tpep_dropoff_datetime BETWEEN '2024-03-01' and '2024-03-15';

Select distinct VendorID from `earnest-setup-415116.ny_taxi.yellow_tripdata_hwk_wk3_partitioned_and_clustered` --26.84MB 
where tpep_dropoff_datetime BETWEEN '2024-03-01' and '2024-03-15';
```
### Bonus Question
Zero bytes will be process for the ``` SELECT COUNT (*)``` query.
This is because BigQuery mainatains metadata about tables which includes the count of rows. So it will simply fetch this information about that table.

