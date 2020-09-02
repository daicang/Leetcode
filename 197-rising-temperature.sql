SELECT w1.Id
FROM   Weather as w1
       JOIN Weather AS w
         ON w.RecordDate = SUBDATE(w1.RecordDate, 1)
WHERE  w1.Temperature > w.Temperature