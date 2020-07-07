'''
By SwiftPerson 2020 
'''

import requests
import urllib3
import sys
import Banner as BN

Software_Version = 1.0

#functions 
def Intro():
    BN.AutoClear()
    BN.ShowBanner(Software_Version)
    BN.Delay(1)



def parse_args():
    import argparse
    parser =  argparse.ArgumentParser()
    parser.add_argument('-d','--domain',type=str,required=True,help="Target Domain")
    parser.add_argument('-o','--output',type=str,help="output File")
    return parser.parse_args()



def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host #gives only domain without www and com etc
    except Exception as e:
        print("[!]Not working domain")
        sys.exit(1)
    return host



def writeToFile(subdomain,outputfile):
    with open(outputfile,'a') as File:
        File.write("[+]"+subdomain + "\n")
        File.close()



def main():
    Intro()
    subdomains = []
    args = parse_args()
    target = parse_url(args.domain)
    output = args.output
    Count = 0
    req = requests.get(f"https://crt.sh/?q=%.{target}&output=json")

    if req.status_code != 200:
        print(BN.Color.BLUE+"[invalid not found in database]")
        sys.exit(1)
    for (keys,values) in enumerate(req.json()):
        subdomains.append(values['name_value'])

    print(BN.Color.YELLOW+f"++++++++++++++TARGET:{target}++++++++++++++\n")

    subs = sorted(set(subdomains))
    for s in subs:
        string = BN.Color.GREEN+"[+]Subdomain Found :"+BN.Color.CyanBold + f"{s}\n"
        BN.slowprint(string,1)
        Count += 1
        if output is not None:
            writeToFile(s,output)
      
    if output is not None:
        print(BN.Color.RED + "SwiftDomainFinder Ended "+BN.Color.YELLOW+f"Total domain found : {Count}"+ BN.Color.RED +f" And Results saved to " + BN.Color.YELLOW + output + BN.Color.Default)
    else:
        print(BN.Color.RED + "SwiftDomainFinder Ended "+BN.Color.YELLOW+f"Total domain found : {Count}"+BN.Color.Default)

if __name__ == "__main__":
    main()
