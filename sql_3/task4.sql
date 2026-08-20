select first_name, last_name
from customers as a
left join shippings as b
on a.customer_id = b.customer
where status is not NULL