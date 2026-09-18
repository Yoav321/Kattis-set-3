"""
counts the amount of a's in the input
Yoav Bierkatz - September 2026
"""

def main() -> None:
  a: str = input().count("a")
  a2: str = input().count("a")
  if a >= a2:
    print("go")
  else:
    print("no")

if __name__ == "__main__":
  main()
    
