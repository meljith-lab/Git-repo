import argparse
import os


def display_banner():
    banner = '''
     .d8888b.  8888888 88888888888      8888888b.  8888888888 8888888b.   .d88888b.  
d88P  Y88b   888       888          888   Y88b 888        888   Y88b d88P" "Y88b 
888    888   888       888          888    888 888        888    888 888     888 
888          888       888          888   d88P 8888888    888   d88P 888     888 
888  88888   888       888          8888888P"  888        8888888P"  888     888 
888    888   888       888   888888 888 T88b   888        888        888     888 
Y88b  d88P   888       888          888  T88b  888        888        Y88b. .d88P 
 "Y8888P88 8888888     888          888   T88b 8888888888 888         "Y88888P" 

The command  line tool  for scanning github repos
made by @meljith


    '''
    print(banner)


def clone_repo(username, template_path, output_file):
    os.system(f"curl -s 'https://api.github.com/users/{username}/repos?page=1&per_page=100' | grep \"clone_url\" | awk '{{print $2}}' | sed -e 's/\"//g' -e 's/,//g' | xargs -n1 git clone")
    os.system(f"nuclei -target ./ -t {template_path} -o {output_file}")

if __name__ == '__main__':
    display_banner()
    parser = argparse.ArgumentParser(description='Clone Github Repositories and run nuclei scan')
    parser.add_argument('-n', '--username', type=str, help='Github username')
    parser.add_argument('-t', '--template_path', type=str, help='Path to nuclei templates')
    parser.add_argument('-o', '--output_file', type=str, help='Output file name')
    args = parser.parse_args()
    clone_repo(args.username, args.template_path, args.output_file)
