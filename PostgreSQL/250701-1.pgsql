-- SELECT 1;
-- SELECT 1 + 1;
-- SELECT 10-20;
-- SELECT 3*6;
-- SELECT 7/3;
-- SELECT 'HELLO WORLD';



-- SELECT * FROM 고객
-- SELECT 고객ID, 이름 FROM 고객
-- SELECT 나이, 나이+10 FROM 고객

-- SELECT 나이+나이 FROM 고객

-- 이름, 연락처, 주소 연결연산자 사용
-- SELECT 이름 || ' ' || 연락처 || ' ' || 주소
-- FROM 고객;

-- SELECT 이름 || ' 고객님 ' || 주소 || '로 배송 예정입니다. 부재시 ' || 연락처 || '로 연락드리겠습니다.'
-- FROM 고객;

-- select 
--     고객id user_id,
--     이름 user_name,
--     나이 user_age,
--     성별 user_gender
-- from 고객

-- SELECT
--     C.고객ID,
--     C.이름
-- FROM 고객 C;

-- SELECT
--     D.고객ID,
--     D.이름
-- FROM 고객 D;

-- SELECT *
-- FROM 고객
-- ORDER BY 나이 DESC
-- LIMIT 5;

-- SELECT DISTINCT 가입연도 AS YEAR
-- FROM 고객;

-- SELECT DISTINCT 가입연도, 가입월
-- FROM 고객
-- ORDER BY 가입월;

-- SELECT 이름, 연락처, (2025-나이) AS 출생연도
-- FROM 고객;

-- SELECT DISTINCT 
--     가입연도 AS join_year, 
--     회원등급 AS grade
-- FROM 고객
-- LIMIT 3;

-- SELECT *
-- FROM 고객
-- WHERE 가입연도 = '2023'
-- ORDER BY 고객id;

-- SELECT 고객ID, 이메일
-- FROM 고객
-- WHERE 나이>25

-- SELECT *
-- FROM 고객
-- WHERE 나이%2 = 1;

-- SELECT *
-- FROM 고객
-- WHERE 이름 = '송현우'

-- SELECT *
-- FROM 고객
-- WHERE 가입월 != '1';

-- SELECT TRUE AND TRUE;
-- SELECT TRUE AND FALSE;

-- SELECT TRUE OR TRUE;
-- SELECT TRUE OR FALSE;

-- SELECT NOT TRUE;
-- SELECT NOT FALSE;

-- SELECT *
-- FROM 고객
-- WHERE 나이 >= 20
-- AND 가입월 = '2'

-- SELECT *
-- FROM 고객
-- WHERE 나이 <= 25
-- OR 나이 >=35

-- SELECT *
-- FROM 고객
-- WHERE NOT (가입연도='2023' AND 가입월='1')

-- SELECT *
-- FROM 고객
-- WHERE 회원등급='VIP' AND (나이 < 25 OR 나이 > 30);

-- SELECT *
-- FROM 고객
-- WHERE 나이 BETWEEN 25 AND 30;

-- SELECT *
-- FROM 고객
-- WHERE 나이 >25 AND 나이 > 30;

-- SELECT *
-- FROM 고객
-- WHERE 가입일자 BETWEEN '2024-01-01'
-- AND '2024-01-31';

-- SELECT *
-- FROM 고객
-- WHERE 고객ID IN ('101', '201', '301')

-- SELECT *
-- FROM 고객
-- WHERE 이름 IN ('김민준', '박예린', '이민서')

-- SELECT *
-- FROM 고객
-- WHERE 이메일 LIKE '%com'

-- SELECT *
-- FROM 고객
-- WHERE 이름 LIKE '김__'

-- SELECT *
-- FROM 고객
-- WHERE 이메일 LIKE '%naver%'

-- SELECT *
-- FROM 고객
-- WHERE 주소 LIKE '제주시%'
-- AND 나이 >= 30;

-- SELECT *
-- FROM 고객
-- WHERE 나이 >= 30
-- AND 가입월 LIKE '%1%'
-- OR 가입월 LIKE '%2%';

-- SELECT *
-- FROM 고객
-- WHERE 나이 >= 30
-- AND NOT (가입월 LIKE '%1%'
-- OR 가입월 LIKE '%2%');

-- SELECT *
-- FROM 고객
-- WHERE 이메일 LIKE '%woo%'
-- AND 이메일 LIKE '%naver%';

-- SELECT DISTINCT 가입월
-- FROM 고객
-- WHERE 나이 >= 30

-- SELECT *, 2025-나이 AS 출생연도
-- FROM 고객
-- WHERE 회원등급 != 'VIP'
-- AND 이름 LIKE '%우%'
-- AND (2025-나이) >= 1990;

-- SELECT 지역, SUM(방문자수) AS 총방문자수
-- FROM 방문기록
-- GROUP BY 지역

-- SELECT COUNT(고객ID)
-- FROM 고객

-- SELECT COUNT(DISTINCT 가입연도)
-- FROM 고객

-- SELECT COUNT(총주문금액)
-- FROM 고객;

-- SELECT COUNT(*)
-- FROM 고객;

-- SELECT SUM(나이)
-- FROM 고객;

-- SELECT AVG(나이)
-- FROM 고객;

-- SELECT MAX(나이), MIN(나이)
-- FROM 고객

-- SELECT VARIANCE(나이), STDDEV(나이)
-- FROM 고객

-- SELECT 회원등급, COUNT(고객ID) AS 등급별_고객수
-- FROM 고객
-- GROUP BY 회원등급;

-- SELECT 
--     회원등급, 
--     SUM(나이) AS 나이합계,
--     AVG(나이) AS 평균나이
-- FROM 고객
-- GROUP BY 회원등급;

-- SELECT 
--     회원등급, 
--     MAX(나이) AS 최고나이,
--     MIN(나이) AS 최소나이
-- FROM 고객
-- GROUP BY 회원등급;

-- 고객 테이블에서 가입연도가 2024년도이고 
-- 가입월이 1월인 고객의 
-- 가입연도별 성별 고객 수를 조회하세요

-- SELECT 가입연도, 성별, COUNT(고객ID)
-- FROM 고객
-- WHERE 가입연도='2024' AND 가입월='01'
-- GROUP BY 가입연도, 성별;


-- SELECT* FROM 고객

-- SELECT 가입연도, 성별, COUNT(고객ID)
-- FROM 고객
-- WHERE 가입연도='2024' AND 가입월='1'
-- GROUP BY 가입연도, 성별;


-- 고객 테이블에서 나이가 20대인 고객중에서 등급이 
-- 'gold'인 고객을 기준으로 
-- 성별 고객의 평균 나이를 조회하세요.

-- SELECT 성별, AVG(나이)
-- FROM 고객
-- WHERE 회원등급='GOLD' 
-- AND 나이 BETWEEN 20 AND 29
-- GROUP BY 성별;

-- SELECT 가입월, COUNT(고객ID) AS 고객수
-- FROM 고객
-- GROUP BY 가입월
-- HAVING COUNT(고객ID) >= 3;

-- SELECT 성별, AVG(나이) AS 고객수
-- FROM 고객
-- GROUP BY 성별
-- HAVING AVG(나이) >= 30;

-- SELECT * FROM 고객 ORDER BY 가입일자 DESC;

-- SELECT * FROM 고객 
-- ORDER BY 가입일자 DESC, 
-- 고객ID LIMIT 3;

-- SELECT 가입월, COUNT(고객ID) AS 고객수
-- FROM 고객
-- GROUP BY 가입월
-- HAVING COUNT(고객ID) =1 AND 가입월 ='11';

-- SELECT 가입월, COUNT(고객ID) AS 고객수
-- FROM 고객
-- WHERE 가입월='11'
-- GROUP BY 가입월
-- HAVING COUNT(고객ID) =1;













