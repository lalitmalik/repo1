import cli.app
#from git import Repo
import os
import re

@cli.app.CommandLineApp
def flink_auto(github_link):
    adict = {
      pyenv_env : "something",
      PYTHON_MAJOR_VERSION : "3.8",
      Perl : "Python",
      PYENV_ROOT : "something"
    } 

    
    print('inside flink app')
    Repo.clone_from("https://github.com/lalitmalik/repo1.git", "/user/lmalik/app1")
    directory =  "/user/lmalik/app1"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        
    # checking if it is a file
        if os.path.isfile(f):
                pattern = re.compile(r"\${[^{}]*}")
                r1 = re.search(pattern, f) 
                f.write(re.sub(r"\${[^{}]*}", r'\1\4\2\3',data))

                
            

    
if __name__ == "__main__":
    flink_auto.run()
