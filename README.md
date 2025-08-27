
# zipC
This is a simple tool that I wrote in Python 3 to brute-force ZIP file passwords. I built this project a while ago just to get some scripting experience in the language. 

You can brute-force passwords of locked ZIP archives by providing a wordlist. The program will crack the password and extract the contents of the given file in the directory specified. 

<img width="1919" height="1151" alt="image" src="https://github.com/user-attachments/assets/d2bf594f-846e-4305-ad42-1e4d29c0d1eb" />

# Installation

```
git clone https://github.com/kavin-jindal/zipC.git
pip install colorama
```

# Usage
```
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
```

# Examples:

## Example 1

```
python zipc.py -w rockyou.txt -f main.zip
```

<img width="958" height="954" alt="image" src="https://github.com/user-attachments/assets/d9bcce7a-a730-43e9-bd80-c3000b1b3a05" />

## Example 2

```
python zipc.py -w rockyou.ltxt -f main.zip -o /main/test
```


<img width="1352" height="972" alt="image" src="https://github.com/user-attachments/assets/caae42bf-757a-426a-be2f-0db75054167c" />




