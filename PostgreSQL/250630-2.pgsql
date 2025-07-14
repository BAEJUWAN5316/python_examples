-- CREATE TABLE test(
--     id serial PRIMARY KEY,
--     title VARCHAR(255) not null
-- )



-- id : 기본키, SERIAL (자동으로 숫자 증가, 4바이트 정수값)
-- title : 255자까지 입력 가능한 문자열, null 값이 들어갈 수 없도록

-- select * from test;
-- INSERT INTO test VALUES (1, 'Ali');
-- SELECT * FROM test;

-- INSERT INTO test(title) VALUES ('Ali'); > id 는 어차피 자동으로 올라가기때문에 생략가능하다

ALTER DATABASE test
RENAME TO test2;






