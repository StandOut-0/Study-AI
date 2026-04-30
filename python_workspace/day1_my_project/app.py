from utils import greet 
 
def main(): 
    name = input("이름을 입력하세요: ") 
    message = greet(name) 
    print(message) 

# main()

if __name__ == "__main__": 
    main()