-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE day=28 AND month=7 AND year = 2021 AND street = 'Humphrey Street';

-- time:10:15

SELECT * FROM interviews WHERE transcript LIKE '%Bakery%';
-- ruth: saw thief get into a car in parking lot within 10 min of theft
-- security footage of parking lot might be helpful

-- eugene: recognized the thief but doesnt know name, saw him at the bank on leggett street
-- might checkout bank table

--raymond: thief plans to take earliest flight out of fiftyville on 29/7, asked person on the phone to book it
-- checking out bookings might help


SELECT license_plate, minute  FROM bakery_security_logs
WHERE day = 28 AND year = 2021 AND month =7 AND minute>=15 AND minute <=25 AND activity='exit';
-- about 15 cars exited


SELECT account_number, amount, transaction_type FROM atm_transactions WHERE day = 28 AND year = 2021 AND month =7
AND atm_location = 'Leggett Street' AND transaction_type= 'withdraw';
-- 8 transactions

SELECT p.name FROM people p, bank_accounts b WHERE b.person_id = p.id
AND b.account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND year = 2021 AND month =7
AND atm_location = 'Leggett Street' AND transaction_type= 'withdraw');

SELECT caller FROM phone_calls WHERE year = 2021  AND month = 7 AND day=28;

-- verdächtige : Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, BEnista
WITH first_flight AS (SELECT f.id FROM flights f, airports a
WHERE f.id=pa.flight_id AND f.origin_airport_id=a.id
AND a.city='Fiftyville'
AND f.day=29 AND f.month=7 and f.year= 2021
LIMIT 1)

SELECT p.name FROM people p, passengers pa, flights f
WHERE p.passport_number=pa.passport_number
AND f.id IN (SELECT id FROM first_flight)
AND p.name IN (SELECT p.name FROM people p, bank_accounts b WHERE b.person_id = p.id
AND b.account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND year = 2021 AND month =7
AND atm_location = 'Leggett Street' AND transaction_type= 'withdraw'))
AND license_plate IN (SELECT license_plate FROM bakery_security_logs
WHERE day = 28 AND year = 2021 AND month =7 AND minute>=15 AND minute <=25 AND activity='exit')
AND p.phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2021  AND month = 7 AND day=28);

-- verdächtige: diana, bruce, luca

WITH first_flight AS (SELECT * FROM flights f, airports a
WHERE f.origin_airport_id=a.id
AND a.city='Fiftyville'
AND f.day=29 AND f.month=7 and f.year= 2021
LIMIT 1)

SELECT f.destination_airport_id, p.name FROM first_flight f, passengers pa, people p
WHERE p.passport_number=pa.passport_number AND pa.flight_id = f.id;