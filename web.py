from flask import Flask
from flask import request
import os
import openai
#set up flask app
app = Flask(__name__)



# Load your API key from an environment variable or secret management service
OPENAI_API_KEY = 'SCRET_KEY'
openai.api_key = OPENAI_API_KEY
mess = [{'role':'system', 'content':'You are a helful assistant on a website for children. The website teaches them the basics of Quantum Computing\n'
	            	'You have vast knowledge of quantum physics and quantum computing\n'
	            	'Your job is to answer questions related to quantum computation, your name is Quanto.\n'
	                'You are very well-spoken and often make jokes appropriate for children\n'
                    'Try to avoid using large words, however if necessary make sure to define them as they occur.\n'
	            	'You are polite and eager to help, and keep your answers short and easy to understand, answers must be simple enough that a 5th grader can understand!\n'}]



@app.route("/")
def index():
    question = request.args.get("question", "")
    if question:
        response = query(question)
    return (
        """<form action="" method="get">
                Enter Your question here: <input type="text" name="question">
                <input type="submit" value="Ask Quanto!>
            </form>"""
        + "Quanto's Answer: "
        + response
    )



#run when a query is received
@app.route("/<int:question>")
def query(question):
    print('\n')
    #Update Message List with each Dialoge so that our Bot can gain insight and the conversation flows
    mess.append({'role':'assistant', 'content': response.choices[0].message.content})
    mess.append({'role': 'user', 'content': question})
    response =  openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mess, temperature = 0.5, max_tokens = 250)
    final = response.choices[0].message.content
    return final






