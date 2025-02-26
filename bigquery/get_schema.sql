-- Two ways to get the schema of an existing table.

-- Ugly JSON
SELECT
 TO_JSON_STRING(
    ARRAY_AGG(STRUCT(
      IF(is_nullable = 'YES', 'NULLABLE', 'REQUIRED') AS mode,
      column_name AS name,
      data_type AS type)
    ORDER BY ordinal_position), TRUE) AS schema
FROM project_name.dataset_name.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = "table_name"
;

-- Clean DDL statement
SELECT t.ddl
FROM `project_name.dataset_name.INFORMATION_SCHEMA.TABLES` t
WHERE t.table_name = 'table_name'
;