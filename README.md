



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

![1675859785222](https://user-images.githubusercontent.com/83987293/218049559-d8c17815-c382-46fd-b40f-4cc9f7d2e1ef.jpeg)


This is a command-line tool used to scan GitHub repositories. The tool takes in three arguments: the GitHub username of the user whose repositories you want to scan, the path to the nuclei template, and the output file. The tool first clones all the repositories of the specified user, creates a directory to store them, and then runs a nuclei scan on all the cloned repositories using the specified nuclei template and writes the results to the specified output file. This tool is meant for educational purposes and is made by @meljith.


