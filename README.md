# Revwho
A simple python tool to reverse search whois by name and email from free services

[![Run on Repl.it](https://repl.it/badge/github/0xc0d/revwho)](https://repl.it/@Aggr3ssor/revwho)

## Install
    git clone https://github.com/aggr3ssor/revwho.git && cd revwho
    chmod +x setup.py
    sudo ./setup.py install

## Usage
    usage: revwho [-h] --terms [TERM [TERM ...]] [--output OUTPUTFILE] [--quiet]

    do reverse whois for term(s) specified and returns a list of domains for that
    term(s).

    optional arguments:
      -h, --help            show this help message and exit
      --terms [TERM [TERM ...]], -t [TERM [TERM ...]]
                            single term or space separated terms
      --output OUTPUTFILE, -o OUTPUTFILE
                            Output to save scan results.
      --quiet, -q           Enable quiet/silent mode (only show warnings and
                            errors).
                            
## Example
Search for `John Doe` and `johndoe@yahoo.com` quietly and save output to `output.txt`
    
    revwho -t "John Doe" "johndoe@yahoo.com" -o output.txt -q
    
### Contact Info
* [Telegram](https://t.me/aggr3ssor)
* [Twitter](https://twitter.com/0xc0d)
* [Email](mailto:aggr3ssor@protonmail.com)
