import argparse
import subprocess
import sys
import curses
 
def main_work(args):
    print('Hello from term-example')
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--noterminal',
        help="don't start a new terminal'",
        action='store_true')
    ns = parser.parse_args()
    try:
        sys.stdout.fileno()
    except Exception:
        # not a terminal for sure
        if ns.noterminal:
            raise RuntimeError('Need a terminal to run.')
        else:
            subprocess.call(['konsole', '--noclose', '-e', sys.executable, __file__, '--noterminal'])
    else:
        main_work(ns)
 
     
if __name__ == '__main__':
    main()
    
curses.setsyx(0, 0)