# LeetCode - 175. Combine Two Tables
# Adam Vaccaro
# Accepted on June 30, 2018
# Runtime: 226ms
# Beat 55.37% of mysql submissions.

# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address ON Person.PersonId=Address.PersonId
