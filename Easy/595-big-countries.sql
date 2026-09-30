/**
 * LeetCode #595: Big Countries
 * Difficulty: Easy
 * Language: Mysql
 * Date: 2026-09-30T19:33:51.707Z
 */

SELECT name,population,area
FROM  World 
WHERE area >= 3000000 OR population >= 25000000;