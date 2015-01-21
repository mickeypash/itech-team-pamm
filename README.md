# itech-team-pamm
Internet Technologies 2015 Team Project

![Python](http://imgs.xkcd.com/comics/python.png)

**[Download PyCharm](https://www.jetbrains.com/pycharm/download/)**

**[Licence Key](http://moodle2.gla.ac.uk/course/view.php?id=2854) (scroll down to the bottom)**

##Using Git

Study this diagram it will help you a lot.
![Git workflow](http://assets.osteele.com/images/2008/git-transport.png)

**Download the project**
```bash
	#template
	git clone <remote> <project folder> 

	#could look like this
	git clone https://github.com/mickeypash/itech-team-pamm itech-project/
```

**Pre-requisits**
+ Mac OSX - it comes preinstalled
+ Windows - you can download it [here](http://git-scm.com/download/win)
+ This will install git bash and git gui
+ I recommend you try to get used to command-line interface before moving onto a GUI

**Setting-up git**
+ Configure your credentials this will be useful when you start using Github
+ Set your name and email to the ones you used for `Github`
```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

**Basic git workflow**
+ You make changes to e.g. `view.py`
+ You do `git status` to see if the changes are registered
+ You could do `git diff` to check what differes from the original file
+ You do `git add` to add your changes to your local repo
+ You do `git commit -m "info about what you changed/fixed"` to commit things (if they are ready)
+ Finally `git push` to push your changes to the shared project on github

**Example in action**
```bash
git add README.md
git commit -m "hello world"
git push
# username and password
# todo: set-up SSH authentication
```
