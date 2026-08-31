# 🐍 100 Days of Python for Data Engineering

A 100-day hands-on Python learning journey designed for a **beginner Data Engineer**.

This challenge starts with Python fundamentals and progressively moves toward **data processing, APIs, ETL, data quality, databases, incremental processing, concurrency, pipeline architecture, orchestration, metadata, lineage, and production-style data engineering systems**.

The goal is not simply to complete 100 Python projects.

The goal is to develop the ability to use Python to **build reliable, maintainable, and testable data pipelines**.

---

## 🎯 Goals

By the end of these 100 days, I aim to be comfortable with:

- Python programming fundamentals
- Git and GitHub
- Working with files and directories
- CSV, JSON, XML, and Parquet
- APIs and web data ingestion
- SQL and databases
- pandas and data manipulation
- Data cleaning and validation
- Data profiling
- Deduplication
- ETL/ELT pipelines
- Batch processing
- Incremental processing
- Data quality
- Schema validation
- Logging and monitoring
- Testing
- Concurrency
- Async programming
- Data ingestion frameworks
- Workflow orchestration concepts
- Data lineage
- Metadata management
- Change Data Capture (CDC)
- Production-oriented Python package development

---

# 🗺️ Roadmap

The 100 days are divided into five stages:

| Days   | Stage                   | Focus                                |
| ------ | ----------------------- | ------------------------------------ |
| 1–20   | Beginner                | Python & data fundamentals           |
| 21–40  | Beginner → Intermediate | Files, formats, APIs & ingestion     |
| 41–60  | Intermediate            | Data quality, transformation & ETL   |
| 61–80  | Advanced                | Concurrency, pipelines & engineering |
| 81–100 | Expert                  | Data platforms & capstone            |

The projects deliberately become more data-engineering focused as the challenge progresses.

---

# 🟢 Days 1–20 — Python & Data Fundamentals

The first 20 days focus on learning Python through small, practical projects.

---

## Day 1 — Basic Calculator

Build a basic command-line calculator capable of:

- Addition
- Subtraction
- Multiplication
- Division

### Concepts

- Variables
- User input
- Functions
- Arithmetic operators
- Error handling
- `eval()`

> If `eval()` is used, it should only be used for this controlled learning exercise. Arbitrary untrusted input should not be passed directly to `eval()`.

---

## Day 2 — Number Guessing Game

Build a simple number guessing game.

### Concepts

- Variables
- Loops
- Conditional statements
- Random numbers
- User input

This project provides a gentle introduction to program flow before moving further into data engineering.

---

## Day 3 — Password Strength Checker

Build a password strength checker that evaluates a password based on configurable rules.

### Concepts

- Strings
- Boolean logic
- Regular expressions
- Functions
- Validation

This introduces concepts that will later be reused for **data validation**.

---

## Day 4 — Data Type Converter

Build a utility that converts values between common data types.

Example:

```text
"123"          → 123
"45.67"        → 45.67
"true"         → True
"2026-08-23"   → datetime
```

Extend the project so that it can process selected columns in a CSV file.

### Concepts

- Type conversion
- CSV processing
- Data types
- Validation
- `datetime`
- Error handling

---

## Day 5 — Date & Time Converter

Build a utility that:

- Parses timestamps
- Converts time zones
- Converts strings to `datetime`
- Formats dates
- Handles invalid timestamps

### Concepts

- `datetime`
- Time zones
- String parsing
- Data normalization

Date and time handling is an important skill in real-world data pipelines.

---

## Day 6 — CLI Data Pipeline Runner

Create a simple command-line interface:

```text
1. Extract
2. Transform
3. Validate
4. Export
5. Exit
```

Initially, the pipeline can operate on a small CSV dataset.

### Concepts

- CLI applications
- Functions
- Program flow
- Pipeline thinking
- Separation of responsibilities

---

## Day 7 — CSV Row Counter

Build a CLI tool that reads a CSV file and reports:

- Number of rows
- Number of columns
- Column names
- Empty rows
- Malformed rows

### Concepts

- File handling
- CSV
- Iteration
- Error handling
- Data inspection

---

## Day 8 — CSV Column Statistics

Given a CSV file, calculate:

- Minimum
- Maximum
- Average
- Null count
- Unique count

### Concepts

- Aggregation
- Numeric data
- Missing values
- Dictionaries
- Functions

This becomes the foundation for future data profiling projects.

---

## Day 9 — Synthetic Dataset Generator

Create a program that generates realistic sample datasets.

Example:

```text
customer_id
name
email
country
signup_date
age
revenue
```

Export the generated data to CSV.

### Concepts

- Random data generation
- Functions
- CSV writing
- Data types
- Synthetic data

This dataset will be reused throughout the challenge.

---

## Day 10 — File Metadata Extractor

Create a tool that scans a directory and produces a CSV containing:

- File name
- Extension
- File size
- Created time
- Modified time
- Absolute path

### Concepts

- Filesystem operations
- Metadata
- `pathlib`
- CSV output
- Datetime handling

---

## Day 11 — Pipeline Execution Timer

Create a reusable timer that measures the execution time of functions or pipeline stages.

Example:

```text
Extract:     1.24 seconds
Transform:   0.82 seconds
Validate:    0.19 seconds
Export:      0.44 seconds

Total:       2.69 seconds
```

### Concepts

- Functions
- Decorators
- Performance measurement
- `time`
- Pipeline monitoring

---

## Day 12 — Dataset Metadata Registry

Create a small metadata registry that stores:

```text
dataset_name
file_path
format
row_count
column_count
last_updated
```

Save the registry as JSON.

### Concepts

- Dictionaries
- JSON
- Metadata
- File handling
- Structured data

---

## Day 13 — Transaction Data Analyzer

Create a transaction analyzer capable of calculating:

- Total revenue
- Total expenses
- Revenue by category
- Expenses by category
- Daily totals
- Monthly totals

Export summary results to CSV.

### Concepts

- Aggregation
- Grouping
- CSV
- Dates
- Data analysis

---

## Day 14 — Data Quality Report Generator

Given a CSV file, produce a report containing:

- Row count
- Column count
- Data types
- Missing values
- Duplicate rows
- Unique values
- Invalid records

### Concepts

- Data quality
- Profiling
- Validation
- Reporting

---

## Day 15 — JSON Dataset Explorer

Load a JSON dataset and inspect:

- Record count
- Available fields
- Nested fields
- Data types
- Missing fields

Support nested JSON structures.

### Concepts

- JSON
- Dictionaries
- Lists
- Nested data
- Schema discovery

---

## Day 16 — CSV Filtering CLI

Create a command-line tool capable of basic dataset filtering.

Example:

```text
filter country = "Qatar"
filter revenue > 1000
sort revenue descending
select name, revenue
```

### Concepts

- Filtering
- Sorting
- Functions
- Expressions
- Structured data

---

## Day 17 — Log File Statistics

Read a log file and calculate:

- Total lines
- Number of errors
- Number of warnings
- Successful requests
- Most common error
- Requests by status code

### Concepts

- Text processing
- Regular expressions
- Dictionaries
- Aggregation
- Log analysis

---

## Day 18 — Batch File Processor

Process every CSV file in a directory and generate a summary for each file.

### Concepts

- Directory traversal
- Batch processing
- Functions
- File handling
- Error handling

---

## Day 19 — Incremental CSV Processor

Track which files have already been processed.

Example:

```text
incoming/
├── customers_01.csv
├── customers_02.csv
└── customers_03.csv

processed/
└── customers_01.csv
```

Only new files should be processed.

### Concepts

- Incremental processing
- State management
- Filesystem operations
- Idempotency

---

## Day 20 — CSV → SQLite Loader

Read a CSV dataset and load it into SQLite.

Pipeline:

```text
CSV
 ↓
Python
 ↓
Validation
 ↓
SQLite
```

### Concepts

- CSV
- SQL
- SQLite
- Database connections
- Inserts
- Schema creation

This is the first major bridge between Python programming and database-oriented Data Engineering.

---

# 🟡 Days 21–40 — Data Processing, Formats & Ingestion

## Day 21 — Column Value Frequency Analyzer

Analyze the frequency of values in a CSV column.

Example:

```text
Country

Qatar      1,250
UAE          830
India        720
USA          610
```

### Concepts

- Grouping
- Counting
- Cardinality
- Data profiling

---

## Day 22 — Column Cardinality Analyzer

Calculate:

- Unique values
- Duplicate values
- Cardinality ratio
- Null percentage

### Concepts

- Data profiling
- Uniqueness
- Missing data
- Statistics

---

## Day 23 — Schema Comparison Tool

Compare two datasets and identify:

- Missing columns
- New columns
- Changed data types
- Column differences

### Concepts

- Schemas
- Data contracts
- Validation
- Dataset compatibility

---

## Day 24 — Dataset Statistics Analyzer

Build a reusable dataset profiler.

Output:

```text
Rows: 100,000
Columns: 14

Null values:
customer_id: 0%
email: 2.1%
country: 0.4%

Unique values:
country: 42
```

### Concepts

- Data profiling
- Statistics
- Null analysis
- Cardinality

---

## Day 25 — File Organizer

Organize data files based on:

- Extension
- Dataset
- Date
- Source

Example:

```text
data/
├── csv/
├── json/
├── xml/
└── parquet/
```

### Concepts

- Filesystem automation
- Paths
- File metadata

---

## Day 26 — Dataset Partition Organizer

Organize files into date-based partitions:

```text
data/
└── year=2026/
    └── month=08/
        └── day=23/
            └── data.csv
```

### Concepts

- Partitioning
- Data layout
- Filesystem organization

---

## Day 27 — Duplicate File Detector

Detect duplicate files using file hashes.

### Concepts

- Hashing
- File metadata
- Duplicate detection
- Efficient processing

---

## Day 28 — Data Lake Directory Profiler

Analyze a data directory and report:

- Number of files
- Total size
- Size by extension
- Largest files
- Oldest files
- Newest files

### Concepts

- Filesystem analytics
- Metadata
- Aggregation

---

## Day 29 — CSV Reader & Profiler

Build a robust CSV reader that reports:

- Schema
- Row count
- Column count
- Null values
- Numeric statistics
- Duplicates
- Invalid rows

### Concepts

- CSV
- Data profiling
- Validation
- Error handling

---

## Day 30 — JSON Dataset Parser

Build a JSON parser supporting:

- Nested JSON
- Arrays
- Schema discovery
- JSON Lines / NDJSON

### Concepts

- JSON
- Nested structures
- Schema inference
- Streaming JSON

---

## Day 31 — CSV → JSON Converter

Convert CSV datasets into JSON.

Support:

- Different delimiters
- Missing values
- Type conversion
- Nested output where appropriate

---

## Day 32 — JSON → CSV Converter

Convert JSON datasets into tabular CSV data.

Handle:

- Nested objects
- Missing fields
- Lists
- Flattening

---

## Day 33 — XML Parser

Parse XML data and transform it into a structured representation.

### Concepts

- XML
- Trees
- Parsing
- Transformation

---

## Day 34 — Structured Log Analyzer

Parse log files into structured records:

```text
timestamp
level
service
message
status_code
```

Export the results to CSV or JSON.

---

## Day 35 — Web Scraper

Build a scraper using:

- `requests`
- BeautifulSoup

Support:

- Pagination
- Error handling
- Rate limiting
- Structured output

### Concepts

- HTTP
- HTML parsing
- Data extraction
- API-like ingestion

---

## Day 36 — Generic REST API Ingestion Pipeline

Build a reusable API ingestion tool:

```text
API
 ↓
JSON
 ↓
Validation
 ↓
Transformation
 ↓
CSV / JSON
```

Support:

- HTTP errors
- Pagination
- Authentication configuration
- Retries
- Logging

---

## Day 37 — API → Database Pipeline

Fetch data from an API and store it in SQLite.

Example fields:

```text
timestamp
asset
price
volume
source
```

### Concepts

- API ingestion
- Persistence
- SQL
- Incremental storage

---

## Day 38 — Incremental API Ingestion

Fetch API data repeatedly while storing only new records.

Implement:

- Timestamps
- Watermarks
- Deduplication
- Idempotency

---

## Day 39 — API Pagination Handler

Build a reusable API client capable of:

- Requesting multiple pages
- Combining responses
- Retrying failures
- Saving results
- Logging progress

---

## Day 40 — Data Source Health Checker

Check the availability of multiple data sources.

Example:

```text
customers.csv       OK
orders.csv          OK
payments.csv        ERROR
external_api        OK
database            OK
```

### Concepts

- Monitoring
- Health checks
- Error handling
- Pipeline reliability

---

# 🟠 Days 41–60 — Core Data Engineering

This stage focuses heavily on **data quality, transformation, scalability, and ETL**.

---

## Day 41 — Email Extractor

Extract email addresses from unstructured text.

### Concepts

- Regular expressions
- Text processing
- Validation

---

## Day 42 — Phone Number Extractor

Extract phone numbers using regular expressions.

### Concepts

- Regex
- Pattern matching
- Data extraction

---

## Day 43 — Data Validation Utility

Build a reusable validation library supporting rules such as:

```text
required
unique
numeric
email
min/max
allowed values
regex
```

---

## Day 44 — CSV Data Cleaning Tool

Clean CSV datasets by:

- Removing whitespace
- Standardizing case
- Normalizing dates
- Converting types
- Handling missing values

---

## Day 45 — Missing Value Detector

Analyze missing data and report:

```text
column        null_count    null_percentage
email         2,130         2.13%
country       421           0.42%
phone         5,820         5.82%
```

---

## Day 46 — Duplicate Record Remover

Detect and remove duplicate records using configurable keys.

Support:

- Exact duplicates
- Key-based duplicates
- Keep-first
- Keep-last

---

## Day 47 — Data Profiler

Build a reusable profiler that produces:

- Schema
- Data types
- Null counts
- Unique counts
- Min/max
- Statistics
- Duplicate counts

---

## Day 48 — Large CSV Chunk Processor

Process datasets too large to comfortably load into memory.

Implement:

```text
Read chunk
 ↓
Transform
 ↓
Validate
 ↓
Write chunk
 ↓
Read next chunk
```

Measure:

- Runtime
- Memory usage
- Rows processed

---

## Day 49 — Data Deduplication Pipeline

Build a complete deduplication pipeline supporting:

- Exact duplicates
- Key-based duplicates
- Hash-based matching
- Duplicate reporting

---

## Day 50 — Dataset Merger

Merge multiple datasets while handling:

- Different schemas
- Missing columns
- Type differences
- Duplicate records

---

## Day 51 — Nested JSON Flattener

Convert nested JSON into tabular structures.

Example:

```text
customer.address.city
customer.address.country
customer.email
```

### Concepts

- Nested data
- Flattening
- Normalization

---

## Day 52 — Data Normalization Utility

Normalize:

- Strings
- Dates
- Numbers
- Categories
- Null representations

---

## Day 53 — Data Anonymizer

Anonymize sensitive-looking fields using techniques such as:

- Hashing
- Tokenization
- Replacement
- Synthetic values

---

## Day 54 — Data Masking Tool

Mask sensitive fields:

```text
john@example.com
→ j***@example.com
```

```text
1234567890
→ ******7890
```

---

## Day 55 — ETL Pipeline for CSV Files

Build a complete ETL pipeline:

```text
Extract
  ↓
Validate
  ↓
Transform
  ↓
Load
```

Include:

- Logging
- Configuration
- Error handling
- Metrics

---

## Day 56 — Incremental File Processor

Process only new or changed files.

Implement:

- Processing state
- File hashes
- Modification timestamps
- Idempotency

---

## Day 57 — Data Quality Checker

Build a reusable quality checker supporting:

- Null checks
- Duplicate checks
- Range checks
- Uniqueness checks
- Referential checks

---

## Day 58 — Schema Validator

Validate datasets against a defined schema.

Example:

```text
customer_id → integer, required, unique
email       → string, optional
age         → integer, 0–120
country     → string
```

---

## Day 59 — Data Transformation Engine

Build a configurable transformation system.

Example:

```text
rename_column
cast_type
trim
lowercase
fill_null
filter
derive_column
```

---

## Day 60 — Batch Data Processor

Build a batch-processing framework capable of processing multiple datasets.

Track:

```text
files processed
rows processed
rows rejected
rows transformed
execution time
errors
```

---

# 🔴 Days 61–80 — Advanced Python & Pipeline Engineering

## Day 61 — Parallel File Processor

Use `multiprocessing` to process independent files concurrently.

Learn when parallelism improves performance and when it does not.

---

## Day 62 — Async API Data Collector

Use `asyncio` to collect data from multiple APIs concurrently.

Focus on I/O-bound workloads.

---

## Day 63 — Multi-threaded Web Scraper

Build a concurrent scraper with:

- Thread pools
- Rate limiting
- Retries
- Error handling

---

## Day 64 — Producer-Consumer Data Pipeline

Implement:

```text
Producer
   ↓
Queue
   ↓
Consumer
```

Use it to process records concurrently.

---

## Day 65 — File Monitoring Service

Monitor a directory for new files and trigger processing automatically.

---

## Day 66 — Streaming Log Processor

Continuously read incoming logs and produce real-time statistics.

---

## Day 67 — Real-Time CSV Watcher

Watch a directory and process new CSV files as they arrive.

---

## Day 68 — Custom Caching System

Build a configurable caching system.

Support:

- Cache keys
- Expiration
- Eviction
- Persistence

---

## Day 69 — Configuration Management Library

Create a configuration system supporting:

- YAML/JSON
- Environment variables
- Defaults
- Validation
- Secrets references

---

## Day 70 — Python Package for Reusable ETL Utilities

Turn previous utilities into a reusable Python package.

Include:

```text
io
validation
transformation
logging
profiling
```

---

## Day 71 — Generic Data Pipeline Framework

Build a configurable framework where pipeline stages can be composed:

```text
extract()
→ validate()
→ transform()
→ load()
```

---

## Day 72 — Plugin-Based Transformation Framework

Allow transformations to be loaded as plugins.

Example:

```text
trim_strings
normalize_dates
remove_duplicates
mask_email
```

---

## Day 73 — Workflow Execution Engine

Build a simple workflow engine capable of executing dependent tasks.

---

## Day 74 — Retry Mechanism with Exponential Backoff

Implement configurable retries:

```text
Attempt 1 → wait 1s
Attempt 2 → wait 2s
Attempt 3 → wait 4s
Attempt 4 → wait 8s
```

Use this in API and pipeline projects.

---

## Day 75 — Data Ingestion Framework

Create a framework capable of ingesting:

- CSV
- JSON
- APIs
- XML

Standardize them into a common internal representation.

---

## Day 76 — Custom CSV Parser

Build a CSV parser optimized for large files.

Focus on:

- Memory usage
- Parsing speed
- Streaming
- Error recovery

---

## Day 77 — Memory-Efficient File Reader

Build readers that process data without loading entire datasets into memory.

Compare:

```text
load entire file
```

versus:

```text
stream records/chunks
```

---

## Day 78 — Dataset Compression Utility

Build a utility that compresses datasets and compares:

- Original size
- Compressed size
- Compression ratio
- Processing time

---

## Day 79 — Archive Extraction Automation

Automatically extract datasets from archives and route them into the appropriate processing pipeline.

---

## Day 80 — Python Logging Framework

Create a reusable logging framework supporting:

- Console logging
- File logging
- Log levels
- Structured logs
- Rotation
- Pipeline context

---

# 🟣 Days 81–100 — Data Systems & Capstone

The final stage moves from individual utilities toward **data-platform concepts**.

---

## Day 81 — Mini Pandas-Like DataFrame

Implement a simplified DataFrame supporting:

- Columns
- Rows
- Filtering
- Selection
- Aggregation
- Sorting

The purpose is to understand the concepts behind tabular data structures.

---

## Day 82 — SQL-Like Query Engine for CSV

Support operations such as:

```sql
SELECT
WHERE
ORDER BY
GROUP BY
```

This project should be paired with learning actual SQL.

---

## Day 83 — Python + Database Data Warehouse Pipeline

Instead of building another CSV database engine, build a pipeline that loads datasets into a relational database.

```text
CSV
 ↓
Python
 ↓
Validation
 ↓
Transformation
 ↓
Database
 ↓
SQL
```

Learn:

- Tables
- Primary keys
- Indexes
- Transactions
- Inserts
- Updates
- Queries

---

## Day 84 — MapReduce Using Python

Implement a simplified MapReduce model.

```text
Input
 ↓
Map
 ↓
Shuffle
 ↓
Reduce
```

The purpose is to understand distributed processing concepts.

---

## Day 85 — Distributed Task Simulator

Simulate workers processing tasks across multiple nodes.

Learn:

- Workers
- Queues
- Task assignment
- Failures
- Retries

---

## Day 86 — Mini Scheduler

Build a scheduler capable of running jobs based on:

- Time
- Dependencies
- Intervals
- Success/failure

---

## Day 87 — Pipeline Dependency Graph

Represent pipelines as a Directed Acyclic Graph (DAG).

Example:

```text
Extract
  ↓
Validate
  ↓
Transform
  ├──→ Customer Summary
  └──→ Revenue Summary
          ↓
        Export
```

This becomes the conceptual foundation for workflow orchestration.

---

## Day 88 — Configurable ETL Framework

Create an ETL framework controlled by configuration rather than hard-coded pipeline logic.

Example:

```yaml
pipeline:
  name: customer_pipeline

steps:
  - extract
  - validate
  - transform
  - load
```

---

## Day 89 — Streaming Data Transformation Library

Build a library capable of transforming records continuously rather than processing only complete files.

---

## Day 90 — Incremental Data Synchronization Engine

Synchronize two datasets while transferring only new or changed records.

Implement:

- Watermarks
- Change detection
- Deduplication
- Idempotency

---

## Day 91 — Change Data Capture Simulator

Simulate:

```text
INSERT
UPDATE
DELETE
```

Track changes and apply them to a destination dataset.

---

## Day 92 — Data Lineage Tracker

Track the relationship between datasets:

```text
raw/customers.csv
        ↓
clean/customers.csv
        ↓
warehouse/customers
        ↓
analytics/customer_summary
```

---

## Day 93 — Metadata Management Library

Store metadata including:

- Dataset name
- Owner
- Source
- Location
- Schema
- Row count
- Size
- Last updated
- Pipeline
- Dependencies

---

## Day 94 — Data Catalog Generator

Automatically generate a catalog of datasets.

For each dataset, include:

```text
name
format
schema
size
row_count
last_modified
source
description
```

---

## Day 95 — Rule-Based Data Validation Framework

Build a configurable framework supporting rules such as:

```text
email IS NOT NULL
customer_id IS UNIQUE
age BETWEEN 18 AND 100
country IN (...)
```

Generate a quality report for each dataset.

---

## Day 96 — Generic File Ingestion Platform

Build a platform that can automatically identify and ingest supported files.

Example:

```text
CSV  → CSV Reader
JSON → JSON Reader
XML  → XML Reader
```

Then route all data into a common pipeline.

---

## Day 97 — End-to-End Data Processing Framework

Combine previous components:

```text
Ingestion
    ↓
Validation
    ↓
Transformation
    ↓
Data Quality
    ↓
Storage
    ↓
Profiling
    ↓
Metadata
    ↓
Logging
```

---

## Day 98 — Workflow Orchestration Simulator

Build an orchestration system capable of:

- Defining tasks
- Managing dependencies
- Scheduling jobs
- Retrying failures
- Recording task status
- Logging execution

---

## Day 99 — Production-Ready Python ETL Toolkit

Turn the best components from the previous 98 days into a cohesive package.

Include:

- CLI
- Configuration
- Logging
- Validation
- Transformations
- ETL
- Retries
- Metrics
- Tests
- Documentation
- Type hints
- Packaging
- CI

This should be treated as a portfolio-quality project.

---

# 🏆 Day 100 — Complete Python Data Engineering Platform

The final capstone combines everything learned throughout the challenge.

## Objective

Build a configurable Python-based data engineering platform capable of:

- Ingesting datasets
- Validating schemas
- Checking data quality
- Transforming records
- Deduplicating data
- Profiling datasets
- Processing batches
- Processing incremental data
- Exporting data
- Tracking metadata
- Tracking lineage
- Logging pipeline execution
- Monitoring pipeline health
- Handling failures
- Retrying failed operations

### High-Level Architecture

```text
                         DATA SOURCES
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
           CSV              JSON              API
             │                │                │
             └────────────────┼────────────────┘
                              ↓
                       ┌──────────────┐
                       │  INGESTION   │
                       └──────┬───────┘
                              ↓
                       ┌──────────────┐
                       │    SCHEMA    │
                       │  VALIDATION  │
                       └──────┬───────┘
                              ↓
                       ┌──────────────┐
                       │ DATA QUALITY │
                       └──────┬───────┘
                              ↓
                       ┌──────────────┐
                       │TRANSFORMATION│
                       └──────┬───────┘
                              ↓
                   ┌──────────┴──────────┐
                   ↓                     ↓
              FILE STORAGE           DATABASE
                   │                     │
                   └──────────┬──────────┘
                              ↓
                       ┌──────────────┐
                       │  PROFILING   │
                       └──────┬───────┘
                              ↓
                       ┌──────────────┐
                       │  METADATA &  │
                       │   LINEAGE    │
                       └──────┬───────┘
                              ↓
                       ┌──────────────┐
                       │  MONITORING  │
                       │  & LOGGING   │
                       └──────────────┘
```

---

# 🧰 Technology Progression

The technology stack should grow alongside the projects.

## Days 1–20

```text
Python
Standard Library
CLI
pathlib
CSV
JSON
SQLite
```

## Days 21–40

```text
Python
CSV
JSON
XML
requests
BeautifulSoup
SQLite
Regular Expressions
```

## Days 41–60

Introduce:

```text
pandas
SQL
Data validation
ETL
Testing
Logging
```

## Days 61–80

Introduce:

```text
asyncio
threading
multiprocessing
PyArrow
Parquet
DuckDB
Packaging
Configuration
```

## Days 81–100

Explore:

```text
Workflow orchestration
Data lineage
Metadata
CDC
Streaming
Distributed processing
Cloud storage
Production ETL
```

---

# ⭐ Priority Skills

Not every technology has equal importance.

| Skill                  |   Priority |
| ---------------------- | ---------: |
| Python                 | ⭐⭐⭐⭐⭐ |
| SQL                    | ⭐⭐⭐⭐⭐ |
| Git/GitHub             | ⭐⭐⭐⭐⭐ |
| CSV/JSON               | ⭐⭐⭐⭐⭐ |
| pandas                 | ⭐⭐⭐⭐⭐ |
| Data cleaning          | ⭐⭐⭐⭐⭐ |
| ETL/ELT                | ⭐⭐⭐⭐⭐ |
| APIs                   | ⭐⭐⭐⭐⭐ |
| Databases              | ⭐⭐⭐⭐⭐ |
| Data quality           | ⭐⭐⭐⭐⭐ |
| Testing                | ⭐⭐⭐⭐⭐ |
| Logging                | ⭐⭐⭐⭐⭐ |
| Parquet                |  ⭐⭐⭐⭐☆ |
| PyArrow                |  ⭐⭐⭐⭐☆ |
| DuckDB                 |  ⭐⭐⭐⭐☆ |
| Docker                 |  ⭐⭐⭐⭐☆ |
| Workflow orchestration |  ⭐⭐⭐⭐☆ |
| Async Python           |   ⭐⭐⭐☆☆ |
| Multiprocessing        |   ⭐⭐⭐☆☆ |
| Distributed systems    |   ⭐⭐⭐☆☆ |

The objective is to understand the **concepts**, not simply collect technologies.

---

# 🧪 Engineering Practices

Good engineering practices should be introduced throughout the challenge rather than saved for Day 100.

## Early Days

Focus on:

- Functions
- Meaningful variable names
- Docstrings
- Basic error handling

## Around Day 20

Introduce:

- Git
- GitHub
- Virtual environments
- Project documentation
- `.gitignore`
- `pyproject.toml`

## Around Day 40

Introduce:

- Logging
- Type hints
- Unit tests
- Integration tests

## Around Day 60

Introduce:

- Configuration
- CLI arguments
- Modular project structures
- Reusable components

## Around Day 80

Introduce:

- Python packaging
- Docker
- CI/CD
- Performance testing
- Metrics

## Day 100

The final platform should resemble a small production-oriented system.

---

# 📁 Repository Structure

The repository should evolve throughout the challenge.

```text
100-days-of-python-data-engineering/
│
├── README.md
│
├── days/
│   ├── 001_calculator/
│   ├── 002_number_guessing/
│   ├── 003_password_checker/
│   ├── ...
│   ├── 055_etl_pipeline/
│   ├── ...
│   ├── 099_etl_toolkit/
│   └── 100_data_platform/
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── shared/
│   ├── io/
│   ├── validation/
│   ├── transformations/
│   ├── profiling/
│   └── logging/
│
├── tests/
│
├── docs/
│
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# 🔄 The Challenge Is One Continuous Journey

The projects are intentionally connected.

The synthetic datasets created on **Day 9** can be reused throughout the challenge.

For example:

```text
Day 9
Synthetic Dataset Generator
        ↓
Day 14
Data Quality Report
        ↓
Day 20
CSV → SQLite
        ↓
Day 29
CSV Profiler
        ↓
Day 44
Data Cleaning
        ↓
Day 45
Missing Values
        ↓
Day 46
Deduplication
        ↓
Day 48
Chunk Processing
        ↓
Day 55
ETL Pipeline
        ↓
Day 56
Incremental Processing
        ↓
Day 57
Data Quality
        ↓
Day 58
Schema Validation
        ↓
Day 70
Reusable ETL Package
        ↓
Day 87
Pipeline Dependency Graph
        ↓
Day 92
Data Lineage
        ↓
Day 93
Metadata
        ↓
Day 94
Data Catalog
        ↓
Day 99
Production ETL Toolkit
        ↓
Day 100
Complete Data Platform
```

This approach turns the 100 days into **one evolving Data Engineering portfolio** rather than 100 unrelated scripts.

---

# 📈 How I Will Measure Progress

For every project, I will document:

```text
Project
Problem being solved
Python concepts learned
Data Engineering concepts learned
Libraries used
Input
Output
Challenges
What I learned
What I would improve
```

For data-processing projects, I will also track:

```text
Rows processed
Rows rejected
Rows transformed
Execution time
Memory usage
Errors
Output size
```

This encourages thinking about both **correctness and performance**.

---

# 🏗️ From Script to Data Platform

The ultimate progression of the challenge is:

```text
Single Python Script
        ↓
Functions
        ↓
Modules
        ↓
Reusable Utilities
        ↓
Data Processing Tools
        ↓
ETL Pipeline
        ↓
Configurable Pipeline
        ↓
Tested Pipeline
        ↓
Incremental Pipeline
        ↓
Monitored Pipeline
        ↓
Orchestrated Pipeline
        ↓
Data Platform
```

This progression mirrors the engineering mindset I want to develop.

---

# 🎓 What Success Looks Like

At the beginning of the challenge, the objective is simply:

> **Learn Python.**

By the middle:

> **Use Python to process and move data.**

By the end:

> **Use Python to build reliable data pipelines and data-processing systems.**

The final goal is to understand the complete lifecycle of data:

```text
             INGEST
                ↓
             VALIDATE
                ↓
              CLEAN
                ↓
           TRANSFORM
                ↓
             DEDUPE
                ↓
             PROFILE
                ↓
              LOAD
                ↓
             MONITOR
                ↓
              LOG
                ↓
            DOCUMENT
```

---

# 🚀 Final Goal

By Day 100, I want this repository to demonstrate more than the ability to write Python.

I want it to demonstrate that I understand how to:

- Work with real-world data formats
- Build data ingestion processes
- Validate data
- Clean and transform datasets
- Handle missing and duplicate data
- Process large files efficiently
- Build batch and incremental pipelines
- Work with APIs
- Work with databases and SQL
- Design reusable ETL components
- Handle failures and retries
- Add logging and monitoring
- Test data-processing code
- Track metadata and lineage
- Understand workflow orchestration
- Think about scalability and performance
- Design maintainable data systems

The ultimate outcome is a progression from:

**🐍 Python Beginner → 📊 Data Processing → 🔄 ETL → 🏗️ Data Pipelines → ⚙️ Data Engineering → 🚀 Data Platform**

---

## 🏁 100 Days. 100 Projects. One Goal.

> **Build the Python and Data Engineering skills needed to turn raw data into reliable, usable information.**

Every day is another step toward becoming a better Data Engineer.
