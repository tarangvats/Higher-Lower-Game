import random
from art import logo
from art import vs
from game_data import data
from replit import clear
size = len(data)
def play_game():
  chosen1 = random.randint(0,size)
  name1 = data[chosen1]['name']
  status1 = data[chosen1]['description']
  country1 = data[chosen1]['country']
  print(f"Compare A: {name1} a {status1} from {country1}.\n")
  print(vs)
  chosen2 = random.randint(0,size-1)
  name2 = data[chosen2]['name']
  status2 = data[chosen2]['description']
  country2 = data[chosen2]['country']
  print(f"Against B: {name2} a {status2} from {country2}.\n")
  print("Who have more followers? Type 'A' or 'B':")
  answer_given = input()

  
  f1 = data[chosen1]['follower_count']
  f2 = data[chosen2]['follower_count']
  if f1>f2:
    actual_answer = 'A'
  if f1<f2:
    actual_answer = 'B'

  if actual_answer==answer_given:
    flag = True
  else:
    flag = False  
  return flag
answer_is_correct = True
count=0
print(logo) 
while answer_is_correct is True:
  if play_game() is False:
    answer_is_correct = False
    clear()
    print(logo)
    print(f"SORRY! thats wrong. Final score is {count}.")
    break
  clear()
  print(logo)  
  count = count+1
  print(f"Your score is {count}")
