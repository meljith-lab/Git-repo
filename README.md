



<img width="1192" alt="Screenshot 2023-02-10 at 2 29 31 AM" src="https://user-images.githubusercontent.com/83987293/217937790-e80c0422-4ec0-4f6f-8842-a9c70630aca1.png">

    
usage: gitrepo.py [-h] [-n USERNAME] [-t TEMPLATE_PATH] [-o OUTPUT_FILE]

<img width="1192" alt="Screenshot 2023-02-10 at 2 36 10 AM" src="https://user-images.githubusercontent.com/83987293/217939000-bb8f0f42-5837-404d-823d-47a52e3111f6.png">


HOW TO INSTALL 


```
git clone https://github.com/meljith-lab/Git-repo.git
cd Git-repo
chmod u+x gitrepo.py
python3 gitrepo.py -n shopify -t /root/nuclei-templates  -o output.txt
````


<img width="1192" alt="Screenshot 2023-02-10 at 2 52 11 AM" src="https://user-images.githubusercontent.com/83987293/217942044-17039500-5dcc-45d4-abfb-0b93a0453824.png">


The tool is written in Python and uses the argparse library to parse command-line arguments. It also uses the os library for creating a directory to store the cloned repositories, and the subprocess library for running the nuclei scans.

The tool has three command-line arguments:

--name or -n: The GitHub username for which the repositories need to be cloned and scanned.
--template or -t: The path to the nuclei template that will be used for scanning the repositories.
--output or -o: The file where the results of the nuclei scans will be stored.
