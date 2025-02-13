select 
   table_schema                                       as `Database`, 
   table_name                                         as `Table`, 
   round(((data_length + index_length)/1024/1024), 2) as 'Size in MB'
from
   information_schema.tables 
order by
   (data_length + index_length) desc
;
