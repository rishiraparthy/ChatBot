#step 1     IMPORTING LIBRARIES
import json
import re
import random_responses

# LOAD THE JSON DATA (FUNCTION DEFINITION)
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)
# GIVE THE PATH (CALLING TO LOAD DATA )
responses_data=load_json("bot.json")

# DEFINING THE GET RESPONSE
def get_response(input_string):
    split_message= re.split(r'\s+|[,;?!.-]\s*', input_string.lower())  #SPLITTING USER INPUT
    score_list=[]  # INITIALIZING SCORE TO 0

    for response in responses_data:  # LOOP IS STARTING THROUGH DATA ##INITIALIZE TO 0 
        response_score=0 #Tracks how well the user’s input matches a chatbot response.
        required_score=0 #Tracks how many required words exist in user input.                 
        required_words=response["required_words"] #Extracts mandatory words for a response to be valid.

        if required_words:    # CHECHING FOR REQUIRED WORDS
            for word in split_message:   # Checks if there are required words for the chatbot response
                if word in required_words:
                    required_score+=1
        if required_score==len(required_words):   # SCORING USER INPUTS
            for word in split_message:
                if word in response["user_input"]:
                    response_score+=1   # Counts matching words between user input and the chatbot’s expected input.
        score_list.append(response_score)     #STORING RESPOSE SCORE 

# FINDING THE BEST RESPONSE 
    best_response=max(score_list)
    response_index=score_list.index(best_response)

# HANDLING THE EMPTY OUTPUT 
    if input_string=="":
        return "please type something so that we can chat:"
# RETUNRING THE BEST RESPONSE OR RANDOM REPLY  
    if best_response!=0:
        return responses_data[response_index]["bot_response"]
    
    return random_responses.random_string()

# RUN THE CHATBOT
while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))


