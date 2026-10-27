# SQL Practice

Practice queries I wrote while learning SQL, run on a small SQLite database that the script builds by itself. No other files are needed.

## What it covers
| Task | Concept |
|---|---|
| 1 | Filtering with `WHERE` and sorting with `ORDER BY` |
| 2 | `LEFT JOIN` with `GROUP BY` and `SUM`, keeping customers who have no orders |
| 3 | `HAVING`, to filter groups after grouping |
| 4 | A subquery inside `WHERE` |
| 5 | Window functions: `RANK` and `DENSE_RANK` |
| 6 | `PARTITION BY`, to rank inside each group |
| 7 | Top row per group, using a subquery in `FROM` |

## Data
Two small tables, built inside the script:
- `customers`: customer_id, name, city
- `orders`: order_id, customer_id, item, amount, order_date

## How to run
1. Install Python and pandas (`pip install pandas`)
2. Run `python sql_practice.py`
3. Each task's result is printed under its title

The database file `practice.db` is created when the script runs. It isn't included here.

## Tools used
Python, pandas, SQLite

## Author
Vinay Simha M K
