import sys
def hulk():
    print('Hulk: hulk smash!!!')

def default():
    print('Nick: welcome to avengers initiative')
    
if  __name__ == '__main__':
    try:
        avenger = sys.argv[1]
        if avenger == 'hulk':
            hulk()
        else:
            default() 
    except:
        default()
    
