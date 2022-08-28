select request_at as Day,
    round(sum(if(status<>"completed",1,0)) / count(status), 2) as "Cancellation Rate"
from Trips
where request_at between "2013-10-01" and "2013-10-03"
    and client_id not in (select users_id from Users where banned = "Yes")
    and driver_id not in (select users_id from Users where banned = "yes")
group by request_at
