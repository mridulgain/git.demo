import sys
def thor():
    print('Thor: Odinson..God of thunder')
    print('thor IW: bring me thanos!!!!)
def captain_america():
    print('Cap: Avengers assemble')
def hulk():
    print('Hulk: hulk smash!!!')
def default():
    print('Nick: welcome to avengers initiative')
    
if  __name__ == '__main__':
    try:
        avenger = sys.argv[1]
        if avenger == 'thor':
            thor()
        elif avenger == 'cap':
            captain_america()
        elif avenger == 'hulk':
            hulk()
        else:
            default() 
    except:
        default()
    
