
import os
import openai

# Load your API key from an environment variable or secret management service

OPENAI_API_KEY = 'SECRET KEY'


openai.api_key = OPENAI_API_KEY


mess = [{'role':'system', 'content':'You are a helpful assistant on a website for children. The website teaches them the basics of Quantum Computing\n'
	            	'You have vast knowledge of quantum physics and quantum computing\n'
	            	'Your job is to answer questions related to quantum computation, your name is Quanto.\n'
	                'You are very well-spoken and often make jokes appropriate for children\n'
                    'Try to avoid using large words, however if necessary make sure to define them as they occur.\n'
	            	'You are polite and eager to help, and keep your answers short and easy to understand, answers must be simple enough that a 5th grader can understand!\n'}]



      

def main():
    #flags if user wants to quit
    talkative = True

    #inicialize our program and introduce user to bot
    print('Hello! Welcome to the Quanto Chat...')

    print('\n ------------------------------------------------------------------')
    print('|     Type "Quit" at any time to end converstation with Quanto     |')
    print(' ------------------------------------------------------------------')
    nam = '\nFuture Scientist >> '

    #Introduce user to bot and generate responses

    response =  openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mess, temperature  = 0.5, max_tokens = 100)
    print('Quanto >> ', response.choices[0].message.content)

    while(talkative):
        question = input(nam)

        if(question == "quit" or question == 'Quit' or question == 'q' or question == 'Q'):
            mess.append({'role':'assistant', 'content': response.choices[0].message.content})
            mess.append({'role': 'user', 'content': 'Goodbye'})
            response =  openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mess, temperature = 0.5, max_tokens = 250)
            print('\nQuanto >> ', response.choices[0].message.content)
            talkative = False
        else:
            print('\n')
            #Update Message List with each Dialoge so that our Bot can gain insight and the conversation flows
            mess.append({'role':'assistant', 'content': response.choices[0].message.content})
            mess.append({'role': 'user', 'content': question})
            response =  openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = mess, temperature = 0.5, max_tokens = 250)
            print('Quanto >> ', response.choices[0].message.content)

	#main loop that gets intake from user and sends to bot to recieve a reply





# execute the main function
if __name__ == "__main__" :
    main()
    exit(0)
