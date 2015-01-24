#Internet Technologies 2015 Team Project

The philosophy behind Django as I understand it is that you create a project such as a blog. Let's call it 'Great Crack' - this would be your project (folder). This might be comprised of a `poll` for surveying your buddies, a `comments` section so they can troll you, and of course everyone needs to `search` through your many blog posts. The things I just enumerated are potential `apps` this makes Django quite modular.

```
pamm/						- project root
├── manage.py 				- creating and running the server
├── mango 					- an app
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── pamm					- project cofig
    ├── __init__.py
    ├── __init__.pyc
    ├── settings.py
    ├── settings.pyc
    ├── urls.py
    └── wsgi.py
```

![Python](http://imgs.xkcd.com/comics/python.png)

**[PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)

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
+ You could do `git diff` to check what differs from the original file
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

##Django
**[Starting a Django 1.6 Project the Right Way](http://www.jeffknupp.com/blog/2013/12/18/starting-a-django-16-project-the-right-way/)**
I found this quite informative

