question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Qustion:
    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer

new_Question = Qustion("dfnujdfhuv","false")

question_bank = []
for question in question_data:
    question_text = question["text"]
    qusetion_answer = question["answer"]
    new_question = Qustion(question_text,qusetion_answer)
    question_bank.append(new_question)

class Quizbrain:
    def __init__(self,q_list):
        self.qusetion_number = 0
        self.score = 0
        self.qusetion_list = q_list
    def still_has_question(self):
        if self.qusetion_number < len(self.qusetion_list):
           return True
        else:
            return False   
    def next_qusetion(self):
        current_qusetion = self.qusetion_list[self.qusetion_number]
        self.qusetion_number += 1
        user_answer = input(f"Q.{self.qusetion_number}:{current_qusetion.text} (true/false): ")
        self.check_answer(user_answer,current_qusetion.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score += 1
            print("you right")

        else:
            print("that's wrong")
        print(f"te correct answer was:{correct_answer}.")  
        print(f"your current score is : {self.score}/{self.qusetion_number}")  
        print("\n")
quiz = Quizbrain(question_bank) 
while quiz.still_has_question:
    quiz.next_qusetion()        

print("you complete the quiz")
print(f"your final score is was :1{quiz.score}/{quiz.qusetion_number}")