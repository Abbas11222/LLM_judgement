from pydantic import Field


class questions:
    question_id: int
    question_text: str
    question_topic: str
    
    def __init__(self, question_id: int, question_text: str, question_topic: str):
        self.question_id = question_id
        self.question_text = question_text
        self.question_topic = question_topic

    def __str__(self):
        return f"Question ID: {self.question_id}, Text: {self.question_text}, Topic: {self.question_topic}"


class answers:
   answer_id:int
   question_id:int
   answer_text:str
   answer_generator:str

   def __init__(self, answer_id:int = 0, question_id:int = 0, answer_text:str = "", answer_generator:str = ""):
      self.answer_id = answer_id
      self.question_id = question_id
      self.answer_text = answer_text
      self.answer_generator = answer_generator

   def __str__(self):
      return f"Answer ID: {self.answer_id}, Text: {self.answer_text}, Generator: {self.answer_generator} , "



class CriterionScore:
   type:str
   score:int = Field(le=5, ge=0)
   rationale:str
         
class Score:
   answer_id : int
   evaluator:str
   scores: list[CriterionScore]

   def get_score(self, criterion):
    for score in self.scores:
        if score.criterion == criterion:
            return score.score

