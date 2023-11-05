from flask import Flask, render_template
import os
import openai


app = Flask(__name__)


OPENAI_API_KEY = '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'


openai.api_key = OPENAI_API_KEY


mess = [{'role':'system', 'content':'You are a helpful assistant on a website for children. The website teaches them the basics of Quantum Computing\n'
	            	'You have vast knowledge of quantum physics and quantum computing\n'
	            	'Your job is to answer questions related to quantum computation, your name is Quanto.\n'
	                'You are very well-spoken and often make jokes appropriate for children\n'
                    'Try to avoid using large words, however if necessary make sure to define them as they occur.\n'
	            	'You are polite and eager to help, and keep your answers short and easy to understand, answers must be simple enough that a 5th grader can understand!\n'}]



def get_response(question):

    #Update Message List with each Dialoge so that our Bot can gain insight and the conversation flows
    mess.append({'role':'assistant', 'content': response.choices[0].message.content})
    mess.append({'role': 'user', 'content': question})
    response =  openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mess, temperature = 0.5, max_tokens = 250)
    return str(response.choices[0].message.content)




@app.route('/')
def index():
    # You can pass the initial message or any other data you want to send to the template here
    initial_message = "Welcome to Quanto Chatbot. How can I help you?"
    return render_template('index.html', initial_message=initial_message)



@app.route('/<message_input>')
def query(message_input):
    post = get_response(message_input)
    return render_template('answer.html', answer=post)