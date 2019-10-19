"""
Jonathan Nguyen
Flash Card Application "Quizzet"
"""

def display_cards():
    print("---------Card List-------")
    for card in range(cdl_size):
        print ("C"+str(card),cdl_ques[card], end = "|")
        print (cdl_ans[card])

import random

#card list question | answer
cdl_ques = []
cdl_ans = []


while True:
    display_menu_choice = int(input("Please choose an option: \n1.View all cards \n2.Create card(s) \n3.Edit a card \n4.Delete a card \n5.Quiz yourself \n6.Exit\n"))
    
    #display
    if display_menu_choice == 1:
        cdl_size = len(cdl_ques)
        if cdl_size == 0:
            print("There are no cards created. ")
        else:
            display_cards()
    #create        
    elif display_menu_choice == 2:    
        cards = int(input("How many cards do you want to create? "))
        
        for card in range(cards):
            ask_ques = input("What will be your question? ")
            ask_ans = input("What will be your answer? ")
            cdl_ques.append(ask_ques)
            cdl_ans.append(ask_ans)
    #edit       
    elif display_menu_choice == 3:
        if cdl_size == 0:
            print("There are no cards created. ")
        else:   
            display_cards()
            cdl_edit = int(input("1.Which card would you like to edit?\n"))
            cdl_edit_choice = input("Would you like to edit the question or answer? (Q/A) \n")
            if cdl_edit_choice == 'q' or cdl_edit_choice == 'Q' or cdl_edit_choice == "question":
                cdl_ques_edit = input("Q|Edit: ")
                cdl_ques[cdl_edit] = cdl_ques_edit
            elif cdl_edit_choice == 'q' or cdl_edit_choice == 'Q' or cdl_edit_choice == "question":
                cdl_ans_edit = input("A|Edit: ")
                cdl_ans[cdl_edit] = cdl_ans_edit
    #delete            
    elif display_menu_choice == 4:
        if cdl_size == 0:
            print("There are no cards created. ")
        else:   
            display_cards()
            cdl_del = int(input("Which card would you like to delete? "))
            del cdl_ques[cdl_del]
            del cdl_ans[cdl_del]
    
    #quiz
    elif display_menu_choice == 5:
        if cdl_size == 0:
            print("There are no cards created. ")
        else:   
            cdl_size = len(cdl_ques) 
            temp_ques = cdl_ques.copy()
            temp_ans = cdl_ans.copy()
            score = 0
            
            for card in range(cdl_size):
                rand_ques_index = random.randint(0,len(temp_ques))
                print(cdl_ques[rand_ques_index])
                rand_answer_choice = input("A| ")
                if rand_answer_choice == cdl_ans[rand_ques_index]:
                    score += 1
                    del temp_ques[rand_ques_index]
                    del temp_ans[rand_ques_index]
            print("Score:",score)
        
        
    #exit   
    elif display_menu_choice == 6:
        break
        
        
    