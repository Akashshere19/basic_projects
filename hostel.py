import random
import time
print("\nWelcome to Hangman") 
name=input('Enter your Name:')
print('Hello ' + name + " Best of Luck")
time.sleep(2)
print('The game is start')
time.sleep(3)
def main():
    global count
    global display
    global word 
    global already_guessed
    global length
    global play_game 
    word_to_guess = ['January','border','image','film']
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_' * length 
    already_guessed =[]
    play_game="" 
def play_loop():
    global play_game
    play_game = input("Do you want to play agin? y =yes,n=no \n") 
    while play_game not in ["y","n","Y","N"]:
              play_game = input('Do you want to play again? y=yes,n=no \n')   
    if play_game =='y':
        main()
    elif play_game =='n':
        print('thanks for playing game')  
        exit()
def hangman():
    global count
    global display
    global word 
    global already_guessed
    global length
    global play_game 
    limit =5 
    guess = input('this is the hangman word:'+ display +'enter your guess : \n')
    guess =guess.strip()
    if len(guess.strip())==0 or len(guess.strip()) >=2 or guess <='9':
        print('invalid input, try a letter\n')
        hangman()
    elif guess in word:
        already_guessed.extend([guess]) 
        index = word.find(guess)
        word = word[:index]+"_"+ word[index + 1:]
        display = display[:index]+ guess +display[index + 1:]
        print(display + '\n')
    elif guess in already_guessed:
            print('try another letter \n')
    else:
         count +=1
         if count ==1:
             time.sleep(1)
             print("______ \n"
                    "   |        \n"
                    "   |         \n"
                    "   |          \n"
                    "   |          |n"
                    "__|__\n")
             print("wrong guess. "+str(limit - count)+ "guessing remaining\n")
         elif count ==2:
             time.sleep(1)
             print(" _______\n"
                   " |       | \n"
                    "   |          \n"
                    "   |          |n"
                    "__|__\n")
             print("wrong guess. "+str(limit - count)+ "guessing remaining\n")   
         elif count ==3:
             time.sleep(1)
             print(" _______\n"
                   " |       | \n"
                    "   |          \n"
                    "   |          |n"
                    "__|__\n")
             print("wrong guess. "+str(limit - count)+ "guessing remaining\n")   
         elif count ==4:
             time.sleep(1)
             print(" _______\n"
                   " |       | \n"
                    "   |          \n"
                    "   |          |n"
                    "__|__\n")
             print("wrong guess. "+str(limit - count)+ "guessing remaining\n") 
         elif count ==5:
             time.sleep(1)
             print("  _______\n"
                   "  |       | \n"
                   "  |       |\n"
                   "  |       |  \n"
                   "  |       0  \n"
                   "  |      /|\ \n"
                   "  |      /|\ \n"  
                   "__|__\n")
             print("wrong guess. "+str(limit - count)+ "guessing remaining\n") 
             print("the word was :",already_guessed,word)
             play_loop()

    if word =='_'* length:
        print("congrats ! you have guessed the word correctly !") 
        play_loop()
    elif count !=limit:
        hangman()
main()
hangman()                                         
