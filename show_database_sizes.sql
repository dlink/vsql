select
   table_schema                                         as "Database Name",
   round(sum(data_length + index_length )/1024/1024, 2) as "Size in MB",
   round(sum(data_free )/1024/1024, 2)                  as "Free in MB"
from
   information_schema.tables
group by
   table_schema
; 
