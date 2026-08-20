select *
from customers as c
left join Orders as o
on c.customer_id = o.customer_id