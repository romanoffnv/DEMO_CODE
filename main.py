import os
import sys
import time
from GUI._main import main as gui


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)


def main():
    gui()
    
    
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds ---% {(time.time() - start_time)}')
    