import sys
def captain_america():
    print('Cap: Avengers assemble')

def default():
    print('Nick: welcome to avengers initiative')
    
if  __name__ == '__main__':
    try:
        avenger = sys.argv[1]
        if avenger == 'cap':
            captain_america()
        else:
            default() 
    except:
        default()
    
