import random

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
  while test_dict != tested:
    key = random.choice(list(test_dict.keys()))
    value = test_dict[key]
    if key not in tested:
      print(key)
      trans = input("Translation: ")
      total += 1
      check = False
      for i in range(len(value)):
        if trans == value[i]:
          print("Correct")
          check = True
          correct += 1
      if not check:
        print(f"Nope, it's {', '.join(value)}")
    tested[key] = value
  rate = round(100*correct/total, 1)
  return(rate)
  
def main():
  selected_dict = "dict_1.txt"
  test_dict = open_dict(selected_dict)
  
  mode = input("""Select one of these options:
1 for German -> Czech
2 for Czech -> German
3 for both German -> Czech and Czech -> German
Pick the option: """)
  
  rate = test(test_dict, mode)
  print(f"Test finished, this is your success rate is {rate}%")
  
  
  
  
  #print(test_dict)
  


if __name__ == "__main__":
  main()
