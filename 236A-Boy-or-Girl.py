def main():
    name = input()
    name = dict.fromkeys(name)  
 
    if len(name) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
 
 
if __name__ == "__main__":
    main()
