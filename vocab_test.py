import random
import os

def open_dict(path):
  opened_dict = {} 
  with open(path, "r", encoding='utf-8') as file:
    for line in file:
        key, val = line.strip().split(" : ")
        value = val.strip().split(", ")
        opened_dict[key] = value
  return(opened_dict)

def test(test_dict, mode):
  tested = {}
  total = 0
  correct = 0
  choice = 0
  while test_dict != tested:
    key = random.choice(list(test_dict.keys()))
    value = test_dict[key]
    value_test = random.choice(value)
    if mode == 1: 
      choice = 1
    elif mode == 2:
      choice = 2
    elif mode == 3:
      choice = random.choice([1,2])

    if key not in tested:
      if choice == 1:
        print(key)
      elif choice == 2:
        print(value_test)
      
      trans = input("Translation: ")
      total += 1
      check = False
      
      if choice == 1:
        for i in range(len(value)):
          if trans == value[i]:
            print("Correct")
            check = True
            correct += 1
        if not check:
          print(f"Nope, it's {', '.join(value)}")
    
      elif choice == 2:
        if trans == key:
          print("Correct")
          check = True
          correct += 1
        if not check:
          print(f"Nope, it's {key}")

    tested[key] = value
  rate = round(100*correct/total, 1)
  return(rate)
  
def main():
  dict_files = []
  files = os.listdir()
  print(files)
  print(len(files))
  for i in range(len(files)):
    if files[i][-4:]== ".txt":
      dict_files.append(files[i])
  
  print(dict_files)
  selected_dict = "dict_1.txt"
  test_dict = open_dict(selected_dict)
  
  mode = int(input("""Select one of these options:
1 for German -> Czech
2 for Czech -> German
3 for both German -> Czech and Czech -> German
Pick the option: """))
  
  rate = test(test_dict, mode)
  print(f"Test finished, your success rate is {rate}%")
  
if __name__ == "__main__":
  main()
