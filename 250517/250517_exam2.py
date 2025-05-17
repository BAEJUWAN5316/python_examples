class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.score = {}
        # 학생 이름과 학번을 저장하는 속성을 만드세요
        # 성적을 저장할 빈 딕셔너리도 만드세요 (교과목 이름: 점수)

    def add_score(self, subject, score):
        new_score = {subject: score}
        self.score = self.score | (new_score)
        # 특정 과목의 성적을 추가하거나 수정하는 메서드를 만드세요

    def get_average(self):
        if len(self.score) == 0:
            return 0
        else:
            return sum(list(self.score.values())) / len(self.score)
        # 전체 과목의 평균 점수를 계산하는 메서드를 만드세요
        # 과목이 없으면 0을 반환하세요

    def get_highest_subject(self):
        a = sorted(self.score.items(), key=lambda x: x[1], reverse=True)
        return a[0][0], a[0][1]

        # 가장 점수가 높은 과목과 그 점수를 반환하는 메서드를 만드세요
        # 반환 형식: (과목명, 점수)
        # 과목이 없으면 ("없음", 0)을 반환하세요
        pass

    def show_scores(self):
        a = list(self.score.items())
        for value in a:
            print(f"{value[0]} : {value[1]}")
        # 모든 과목과 점수, 그리고 평균 점수를 출력하는 메서드를 만드세요


# 테스트 코드
student = Student("라이캣", "20250101")

student.add_score("수학", 85)
student.add_score("영어", 92)
student.add_score("과학", 78)

# 출력
print(f"학생 이름: {student.name}")  # 출력: 학생 이름: 라이캣
print(f"학번: {student.student_id}")  # 출력: 학번: 20250101
print(f"평균 점수: {student.get_average()}")  # 출력: 평균 점수: 85.0

best_subject, best_score = student.get_highest_subject()
print(
    f"최고 점수 과목: {best_subject}, 점수: {best_score}"
)  # 출력: 최고 점수 과목: 영어, 점수: 92

student.show_scores()
# (실행 시 출력 예시)
# 수학: 85점
# 영어: 92점
# 과학: 78점
