from flask import Flask, render_template, Response, request, redirect, url_for
import ctypes
import cv2
import subprocess
import numpy as np
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')





@app.route('/youtube')
def youtube():
    return render_template('youtube.html')


@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/resources')
def resources():
    return render_template('youtube.html')



  
# @app.route('/process', methods=['POST'])
# def process():
#     data = request.get_json() # retrieve the data sent from JavaScript
#     # process the data using Python code
#     result = data['value'] * 2
#     return jsonify(result=result) # return the result to JavaScript
 
@app.route('/gpt',methods=["POST"])
def gpt():

    from dotenv import load_dotenv
    from langchain import HuggingFaceHub, LLMChain
    from langchain.prompts import PromptTemplate

    load_dotenv()
    # data = request.get_json() # retrieve the data sent from JavaScript
    # result = data['value']
    
    search_term = request.form.get("search")
    
    print(search_term)
    hub_llm = HuggingFaceHub(
            repo_id="google/flan-t5-xxl",
            model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Generate random unique hard Multiple choice questions with answers on {question} topic?"
            )
    hub_chain = LLMChain(prompt=prompt , llm=hub_llm, verbose=True)
    ques = hub_chain.run(search_term)
    print("question:",ques)

    llm = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt2 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer correctly: {question} "
            )
    chain = LLMChain(prompt=prompt2 , llm=llm, verbose=True)
    ans = chain.run(ques)        
    print("ans:A:",ans)

    llm3 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt3 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer wrong {question} "
            )
    chain3 = LLMChain(prompt=prompt3 , llm=llm3, verbose=True)
    wrong1 = chain3.run(ques)        
    print("B:",wrong1)

    llm4 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt4 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer uniquely wrong {question} "
            )
    chain4 = LLMChain(prompt=prompt4 , llm=llm4, verbose=True)
    wrong2 = chain4.run(ques)        
    print("C:",wrong2)

    llm5 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt5 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer uniquely and randomly wrong {question} "
            )
    chain5 = LLMChain(prompt=prompt5 , llm=llm5, verbose=True)
    wrong3 = chain5.run(ques)        
    print("D:",wrong3)

     # Create a dictionary to store the results
    results = [{
        "question": ques,
        "answers":[
        {"text": ans, "correct": True},
        {"text": wrong1,"correct": False},
        {"text": wrong2,"correct": False},
        {"text": wrong3,"correct": False}
        ]
    }]

    # Return the results as JSON
    return jsonify(results)

@app.route('/gpt2')
def gpt2():
    return render_template('gpt.html')


@app.route('/gpt3',methods=["POST"])
def gpt3():

    from dotenv import load_dotenv
    from langchain import HuggingFaceHub, LLMChain
    from langchain.prompts import PromptTemplate

    load_dotenv()
    # data = request.get_json() # retrieve the data sent from JavaScript
    # result = data['value']
    
    search_term = request.form.get("search")
    
    print(search_term)
    hub_llm = HuggingFaceHub(
            repo_id="google/flan-t5-xxl",
            model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Generate unique Multiple choice questions with answers on {question} topic?"
            )
    hub_chain = LLMChain(prompt=prompt , llm=hub_llm, verbose=True)
    ques = hub_chain.run(search_term)
    print("question:",ques)

    llm = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt2 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer correctly: {question} "
            )
    chain = LLMChain(prompt=prompt2 , llm=llm, verbose=True)
    ans = chain.run(ques)        
    print("ans:A:",ans)

    llm3 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt3 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer wrong {question} "
            )
    chain3 = LLMChain(prompt=prompt3 , llm=llm3, verbose=True)
    wrong1 = chain3.run(ques)        
    print("B:",wrong1)

    llm4 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt4 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer uniquely wrong {question} "
            )
    chain4 = LLMChain(prompt=prompt4 , llm=llm4, verbose=True)
    wrong2 = chain4.run(ques)        
    print("C:",wrong2)

    llm5 = HuggingFaceHub(
                repo_id="google/flan-t5-xxl",
                model_kwargs={'temperature':0.5, 'max_length':1000})

        # mrm8488/t5-base-finetuned-wikiSQL       gpt2      https://huggingface.co/chat/
    prompt5 = PromptTemplate(
                input_variables = ["question"],
                template = "Q: Answer uniquely and randomly wrong {question} "
            )
    chain5 = LLMChain(prompt=prompt5 , llm=llm5, verbose=True)
    wrong3 = chain5.run(ques)        
    print("D:",wrong3)

     # Create a dictionary to store the results
    results = [{
        "question": ques,
        "answers":[
        {"text": ans, "correct": True},
        {"text": wrong1,"correct": False},
        {"text": wrong2,"correct": False},
        {"text": wrong3,"correct": False}
        ]
    }]

    # Return the results as JSON
    return jsonify(results)


# @app.route('/process_input', methods=['POST'])
# def process_input():
#   input_value = request.form['inputValue'] # Retrieve the input value from the AJAX request
#   # Do something with the input value
#   return jsonify({'result': 'Success'})





if __name__ == '__main__':
    app.run(threaded=True, debug=True)
