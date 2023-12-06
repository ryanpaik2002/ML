

from fastapi import FastAPI, BaseModel
import os
import uvicorn
import json
from chain_def import get_def_multi_choice_llm, get_def_answer
from words_import import get_words



app = FastAPI()

# class LevelRequest(BaseModel):
#      level: str
#      section: int

class WordRequest(BaseModel):
    word_list: list
    csv_path:str
    level: str
    # section: int
    q_count: int
    

def single_quest_list(single_word):
    QA_list=[]
    word={"word":single_word}
    question, answers= get_def_multi_choice_llm(single_word) # returns type dict keys(a,b,c,d) values: (def 1, )
    answer = get_def_answer(single_word, answers) # returns type dict
    print(f"answer: {answer}")
    QA_list.extend([word, question, answer])
    # QA_list.append(word, multi_choice, answ
    # print(QA_list)


single_word="bombastic"
LEVEL="TOEFL"
SECTION=1

file_name = LEVEL+".csv"
CSV_PATH=os.path.join(os.path.dirname(__file__), 'data',file_name)

@app.get('/')
def hello(single_word):
    # single_word=word
    # single_word="bombastic"
    single_quest_list(single_word)

@app.get('/words')
def prepare_quiz(q_count, CSV_PATH):
    # level=level
    # q_count=q_count    
    word_list = get_words(q_count, CSV_PATH)
    print(word_list)
    
    
    return word_list
    

    
@app.get('/predict')
def get_questions(single_word):
    # single_word=word  
    single_qa = single_quest_list(single_word)
    dict_qa = {"QA": single_qa}
    return dict_qa

    
    # question = get_def_multi_choice_llm(single_word)








# get a word list from the json table, 
# dict 







if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9988, reload=True)
    
    
    single_word="bombastic"
