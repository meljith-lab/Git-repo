
import argparse
import os
import subprocess

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

This  command  line tool  for scanning github  repos through nuclei
made by @meljith
    '''
    print(banner)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Clone all repositories of a GitHub user and run nuclei scans')
    parser.add_argument('-n', '--name', type=str, required=True, help='GitHub username')
    parser.add_argument('-t', '--template', type=str, required=True, help='Path to nuclei template')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file')
    return parser.parse_args()

def clone_repos(username):
    cmd = f"curl -s 'https://api.github.com/users/{username}/repos?page=1&per_page=100' | grep 'clone_url' | awk '{{print $2}}' | sed -e 's/\"//g' -e 's/,//g' | xargs -n1 git clone"
    subprocess.run(cmd, shell=True, check=True)

def run_nuclei(nuclei_template, output_file):
    cmd = f"nuclei -target ./ -t {nuclei_template} -o {output_file}"
    subprocess.run(cmd, shell=True, check=True)

def main():
    display_banner()
    args = parse_arguments()
    username = args.name
    nuclei_template = args.template
    output_file = args.output

    repo_dir = f"{username}_repos"
    os.makedirs(repo_dir, exist_ok=True)
    os.chdir(repo_dir)

    clone_repos(username)
    run_nuclei(nuclei_template, output_file)

if __name__ == '__main__':
    main()
