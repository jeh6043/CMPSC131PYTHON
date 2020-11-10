# Author: Josiah Harrison jeh6043@psu.edu
# GitHub ID: jeh6043

def is_anagram(s1, s2):
  for x in s1:
    if x.isalnum():
      if x.lower() not in s2 and x.upper() not in s2:
        return False
      else:
        a = s1.count(x.lower()) + s1.count(x.upper())
        b = s2.count(x.lower()) + s2.count(x.upper())
        if a != b:
          return False

  return True

def run():
  x = input("Enter a string: ")
  y = input("Enter a string: ")
  if is_anagram(x,y) == True:
    print("anagram")
  else:
    print("not anagram")

if __name__ == "__main__":
  run()    

