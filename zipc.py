import zipfile
from colorama import *
import argparse, time
init()
head = '''
     _         ___ 
 ___(_)_ __   / __\\
|_  / | '_ \\ / /   
 / /| | |_) / /___ 
/___|_| .__/\\____/ 
      |_|          
'''

parser = argparse.ArgumentParser(
    prog="zipC",
    add_help=False,
    
    
)
parser.add_argument('-h', '--help', help="View help menu", action='store_true')
parser.add_argument('-f', '--file',  help="ZIP File to be cracked")
parser.add_argument('-w', '--wordlist',  help="Wordlist to perform brute force")
parser.add_argument('-o', '--output',  help="Directory to extract the zip file in")
p=parser.parse_args()





y = 50
start = time.time()






def zipc(f, w):
    print("Total items: ", len(fo))
    name = f.strip('.zip')

    for index,i in enumerate(w):
        i = i.encode('utf-8')
        text = "[i] Progress: " + f"[{index} / {len(fo)}]"
        print(Fore.YELLOW + '\r' +  text, end='')
        
        try:
            if p.output:
                z.extractall(pwd=i, path=p.output)
            if not p.output:
                z.extractall(pwd=i, path=name)

            
            i = i.decode('utf-8')
            print(Fore.GREEN + f"\n\n[!] [{index}] Password found! ")
            print(Fore.GREEN + f"[!] Your password is => '{i}'")
            if p.output:
                print(Fore.GREEN + f'\n\nExtracted {f} to {p.output} successfully!')
            if not p.output:
                print(Fore.GREEN + f'\n\nExtracted "{f}" to "{name}\\" successfully!')

            end = time.time()
            print(Fore.RED + f"[i] Duration: {round(end-start, 2)} seconds")            
            break

            
        except Exception as e:
            None
            
            
def main():
    try:
        print(Fore.LIGHTBLUE_EX + head)
        print("-"*y)
        print(Fore.LIGHTGREEN_EX + "Built by:     "+"Kavin Jindal (@klevr)")
        print("Version:      "+"0.1")
        print("Last Updated: "+"27/08/2025")
        print(Fore.LIGHTBLUE_EX + "-"*y)
        print(Fore.LIGHTCYAN_EX + f"File:"+(9)*' '+f"{p.file}")
        print(f"Wordlist:"+(5)*' '+f"{p.wordlist}")
        if p.output:
            print("Output in:"+(4)*' '+f"{p.output}")

        if not p.output:
            print("Output in:"+(4)*' '+f"{(p.file).strip('.zip')}\\")

        print(Fore.LIGHTBLUE_EX + "-"*y)
        global z, f, fo
        f = open(p.wordlist, mode='r', errors='ignore').read()
        fo = f.splitlines()
        z = zipfile.ZipFile(p.file)
        zipc(p.file, fo)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] The process was terminated.")
    
        

try:
    filep = False
    wordp = False
    if p.help:
        helpp =  '''
==========================================================
    zipC v0.1
    By Kavin Jindal (@klevr)
    A fast password bruteforcing tool for ZIP archives.
==========================================================

Usage: 
    python zipc.py -f <zipfile> -w <wordlist> -p <output_path>

Required arguments:
    -f, --file [path]       Path to the target zip file
    -w, --wordlist [path]   Path to the wordlist to be used
Optional arguments:
    -o, --output [path]     Directory to extract the file in
    -h, --help              Shows the help menu

Examples: 
    python zipc.py -f main.zip -w rockyou.txt 
    python zipc.py -f main.zip -w rockyou.txt -o /home/Desktop/main
    python zipc.py --file /home/john/Desktop/archive.zip -w rockyou.txt -o /home/Documents/archive


'''
        print(Fore.YELLOW + helpp)

    elif not p.help:

        
        if p.file is None:
            print(Fore.RED + "Please provide a zip file via -f/--file")
            filep=False
        if p.wordlist is None:
            print(Fore.RED + "Please provide a wordlist via -w/--wordlist")
            wordp=False

    
    
    else:
        None
    if p.file and p.wordlist:
        main()


   

except zipfile.BadZipFile:
    print("File is not in the ZIP format, try again")
    exit
except Exception as e:
    print(e)
    exit
except argparse.ArgumentError:
    pass


    




