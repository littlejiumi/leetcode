# 查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
SELECT a.'CID', AVG(a.'score')
FROM SC AS a
GROUP BY a.'CID'
ORDER BY AVG(a.'score') DESC, a.'CID' ASC;

# 查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩
SELECT s.'sid', s.'name', AVG(a.'score')
FROM stu as s
LEFT JOIN SC as a
ON a.'sid' = s.'sid'
GROUP BY s.'sid'
HAVING AVG(a.'score')>=85;

# 查询课程名称为"数学"，且分数低于60的学生姓名和分数
SELECT s.'name', a.'score'
FROM SC as a
LEFT JOIN stu as s ON s.'sid' = a.'sid'
LEFT JOIN course as c ON a.'cid' = c.'cid'
WHERE c.'name' = 'shuxue'
AND a.'score' < 60;

# 查询所有学生的课程及分数情况；
SELECT s.*,a.`CID`,c.`Cname`,a.`score`
FROM student AS s,SC AS a,course AS c
WHERE s.`SID`=a.`SID` AND a.`CID`=c.`CID`
GROUP BY s.`SID`,a.`CID`
ORDER BY s.`SID`,a.`CID`;
