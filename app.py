class Question:


    def __init__(self,question_text,options,correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_Answer(self):
        for choice in self.options:
            if choice == self.correct_answer:
                print(f"correct the answer was {self.correct_answer} ")
            else:
                print("that is incorrect")



question_list = []
question_1 = Question("What is the smallest planet in our solar system?",["pluto","Mars","Earth","Mercury"],"Mercury")
question_2 = Question("What is the chemical symbol for gold?", ["Au", "H", "G", "Go"], "Au")
question_3 = Question("What is the fastest land animal in the world?", ["Falcon", "Cheetah", "Gazelle","Pronghorn Antelope"], "Cheetah")
question_4 = Question("What programming language is primarily used for web development alongside HTML and CSS?", ["JavaScript", "Python", "C++", "java"], "JavaScript")
question_5 = Question("What is the capital of France?", ["Paris", "Milan", "Rome", "Lyon"], "Paris")

question_list.append(question_1)
question_list.append(question_2)
question_list.append(question_3)
question_list.append(question_4)
question_list.append(question_5)

# print(question_list)


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.total= 0

    def ask_question(self):


        for question in self.questions:
            print(question.question_text)
            print(" ".join(question.options))
            answer = input("type in ur answer: ")
            if answer == question.correct_answer:
                self.score += 1
                self.total+=1

                print(f"you got it correct you have {self.score} points ")
            else:
                print(f"sorry that is incorrect the answer was {question.correct_answer} you have {self.score} points")
                self.total += 1



    def start_quiz(self):
        self.score = 0

        self.ask_question()
        print(f"your final score is {self.score}/{self.total}")


quiz = Quiz(question_list)

quiz.start_quiz()