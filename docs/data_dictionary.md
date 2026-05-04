# Data Dictionary — Gold Layer

## gold_revenue_by_category.csv
| Field | Type | Description | Example |
|---|---|---|---|
| Category | string | Product category name | Technology |
| total_revenue | float | Sum of sales for the category | 836154.03 |
| total_orders | integer | Number of orders in the category | 1847 |

## gold_revenue_by_region.csv
| Field | Type | Description | Example |
|---|---|---|---|
| Region | string | Geographic sales region | West |
| total_revenue | float | Sum of sales for the region | 725457.82 |
| total_orders | integer | Number of orders in the region | 3203 |

## gold_monthly_trend.csv
| Field | Type | Description | Example |
|---|---|---|---|
| Year | integer | Order year extracted from Order Date | 2017 |
| Month | integer | Order month number (1–12) | 11 |
| Month_Name | string | Full month name | November |
| total_revenue | float | Sum of sales for that month and year | 118447.83 |

## gold_avg_transaction.csv
| Field | Type | Description | Example |
|---|---|---|---|
| avg_transaction_value | float | Average sales value per order row | 229.86 |

## gold_top_category.csv
| Field | Type | Description | Example |
|---|---|---|---|
| Category | string | Highest revenue product category | Technology |
| total_revenue | float | Total revenue for top category | 836154.03 |

## gold_revenue_by_shipmode.csv
| Field | Type | Description | Example |
|---|---|---|---|
| Ship Mode | string | Shipping method used | Standard Class |
| total_revenue | float | Sum of sales for that ship mode | 1358215.74 |
| total_orders | integer | Number of orders using that ship mode | 5968 |

## Derived Columns (Silver Layer)
| Field | Formula | Description |
|---|---|---|
| Revenue | Sales (direct) | Sales value per transaction |
| Year | Order Date.year | Extracted year from order date |
| Month | Order Date.month | Extracted month number |
| Month_Name | Order Date.strftime("%B") | Full month name |
| Day_of_Week | Order Date.strftime("%A") | Day name of the order |