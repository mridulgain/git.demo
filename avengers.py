import sys
def thor():
    print('Thor: Odinson..God of thunder')

def default():
    print('Nick: welcome to avengers initiative')
    
if  __name__ == '__main__':
    try:
        avenger = sys.argv[1]
        if avenger == 'thor':
            thor()
        else:
            default() 
    except:
        default()
    
