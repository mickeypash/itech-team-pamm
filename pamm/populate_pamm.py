import os
from datetime import datetime

# # Definig population script
def populate_users():
    # Adding a User
    user_mickey = add_user(username='mickey',
                           first_name='Mickey',
                           email='pashov.m@gmail.com',
                           password='1234',
                           is_active=True)

    # Here I initialised the variable user_mickey
    # and I gave it the value returned by add_user
    # as you can see the method is taking in
    # what is known as 'keyword arguments'
    # this means that I am telling Python which
    # arguments I am passing (e.g. password = '1234')
    # add('mickey', 'Mickey', 'pashov.m@gmail.com')
    # is also acceptable but it's less clear what
    # these arguments are

    user_ana = add_user(username='ana',
                        first_name='Ana',
                        email='anavanegas@gmail.com',
                        password='1234',
                        is_active=True)

    user_pietro = add_user(username='pietro',
                           first_name='Pietro',
                           email='pietro@gmail.com',
                           password='1234',
                           is_active=True)

    user_merunas = add_user(username='merunas',
                            first_name='Merunas',
                            email='merunas@gmail.com',
                            password='1234',
                            is_active=True)

    user_james = add_user(username='james',
                          first_name='James',
                          email='james@gmail.com',
                          password='1234',
                          is_active=False)

def populate_notes():
    note_1 = add_note(title='Mystery plumes in Martian atmosphere baffle scientists',
                      author=user_list[0],
                      timestamp='2015-01-12',
                      content='A curious plume-like feature was observed on Mars on 17th May 1997 by the Hubble Space Telescope. It is similar to the features detected by amateur astronomers in 2012, although it appeared in a different location. Plumes seen reaching high above the surface of Mars are causing a stir among scientists studying the atmosphere on the Red Planet. On two separate occasions in March and April 2012, amateur astronomers reported definite plume-like features developing on the planet. The plumes were seen rising to altitudes of over 250 kilometres above the same region of Mars on both occasions. By comparison, similar features seen in the past have not exceeded 100 kilometres. At about 250 kilometres, the division between the atmosphere and outer space is very thin, so the reported plumes are extremely unexpected, says Agustin Sanchez-Lavega of the Universidad del Pais Vasco in Spain, lead author of the paper reporting the results just published in the journal Nature. he features developed in less than 10 hours, covering an area of up to 1000 x 500 km, and remained visible for around 10 days, changing their structure from day to day. None of the spacecraft orbiting Mars saw the features because of their viewing geometries and illumination conditions at the time. However, checking archived Hubble Space Telescope images taken between 1995 and 1999 and of databases of amateur images spanning 2001 to 2014 revealed occasional clouds at the limb of Mars, albeit usually only up to 100 km in altitude. But one set of Hubble images from 17th May 1997 revealed an abnormally high plume, similar to that spotted by the amateur astronomers in 2012. Scientists are now working on determining the nature and cause of the plumes by using the Hubble data in combination with the images taken by amateurs. One idea we have discussed is that the features are caused by a reflective cloud of water-ice, carbon dioxide-ice or dust particles, but this would require exceptional deviations from standard atmospheric circulation models to explain cloud formations at such high altitudes, says Agustin. Another idea is that they are related to an auroral emission, and indeed auroras have been previously observed at these locations, linked to a known region on the surface where there is a large anomaly in the crustal magnetic field, adds Antonio Garcia Munoz, a research fellow at ESA ESTEC and co-author of the study. The jury is still out on the nature and genesis of these curious high-altitude Martian plumes. Further insights should be possible following the arrival of ESA ExoMars Trace Gas Orbiter at the Red Planet, scheduled for launch in 2016.',
                      is_shared=True,
                      tag=[tag_mars, tag_hubble])

    note_2 = add_user(title='10 Hangover Remedies: What Works?',
                      author=user_pietro,
                      timestamp='2015-02-01',
                      content='The only way to avoid a pounding head and queasiness the morning after is to drink in moderation, or to stay away from alcohol entirely. But its often easy to overindulge. Alternating your drinks with water or another nonalcoholic beverage can help you slow down and stay hydrated. If you still wind up with a hangover, you may be inclined to try one of the many supposedly tried-and-true remedies. However, traditional hangover remedies are often ineffective, and some of them may actually make you feel worse',
                      is_shared=False,
                      tag=[tag_hangover, tag_alcohol])

    note_3 = add_user(title='Take Your Triathlon Performance To The Next Level',
                      author=user_ana,
                      timestamp='2015-02-19',
                      content='What are a few things I can do to take my performance to the next level? I could come up with countless ways to improve stagnant race performances, but the simplest things are often the most difficult to put into practice. Below are a few practical suggestions. Tweak your training. Consider changing up your training stimulus in order to push through plateaus. A balanced program is always best, but there are a number of ways to reach the same end results. For example, if you have always prescribed to an aerobic, high-volume training program, try adding some intensity into your schedule. Address your weaknesses. Take an objective look at yourself to consider areas where you could improve. Often a coach will have an easier time making an honest, unbiased assessment of an athletes weaknesses. Pace better in races. Are you maximizing your pacing to get to the finish line in the best time possible? Could you bike 10 minutes slower to run 20 minutes faster? Does your racing reflect your training? Try race simulation training days where you practice pacing and nutrition. Try new technologies. Consider investing in modern-day training tools. A power meter is very useful for quantifying your efforts. Optimize your equipment. Start paying attention to forces that inhibit forward motion.',
                      is_shared=False,
                      tag=[tag_training, tag_triathlon, tag_aerobic])

    note_4 = add_user(title='REACH YOUR POTENTIAL',
                      author=user_ana,
                      timestamp='2013-12-26',
                      content='Elite athletes ask a lot of their bodies, every day.  Working hard and pushing through hard workouts means that your body has to be resilient and able to adapt to that stress.  There are a few blood markers that are accurate indicators of low levels of nutrients in the body that affect performance.  Low Iron stores -Serum Ferritin- and Vitamin D -25-hydroxyD3- results in a blood test can both cause fatigue and can inhibit recovery.  A doctor or dietitian can use these results to make dietary modifications or recommendations to improve performance.  Know your numbers. Timing is everything.  Elite athletes should be fueled for every training session, no excuses.  This is especially important for the first-thing-in-the-morning practice. After sleeping 6-8 hours, it is crucial to eat something to prevent muscle breakdown, which can easily happen when training hard in the fasted state.  I am not expecting athletes to wake up and make an large egg breakfast first thing, but eating SOMETHING to elevate energy levels and jump start the metabolism after sleep -nap or overnight- can get the body moving and if it is a high intensity training session, a small dose of protein in that snack can prevent muscle breakdown and encourage strength gains.  That alone makes a pre-workout snack worth it.  Think toast with peanut butter, a granola bar, or a yogurt smoothie drink. If you are doing doubles of any kind of workout, eating something ASAP afterwards encourages faster, more efficient recovery, compared to consuming nothing when time is limited. Yes, your body will eventually bounce back and be ready to take on another day of training, but if only a few hours -or minutes with back to back swim and lifting sessions- separate one training session from another, recovery nutrition will make the difference. Quick absorbing carbohydrates and whey proteins are the best for this time think fruit plus cottage cheese, or pretzels plus yogurt.  You are already investing the time and putting in the effort. Make it count.',
                      is_shared=True,
                      tag=[tag_training, tag_metabolism.tag_athlete])

    note_5 = add_user(title='STRENGTH IN NUMBERS',
                      author=user_ana,
                      timestamp='2014-09-02',
                      content='Designing an effective dryland program for an entire swim team can be quite challenging. Factoring in such potential obstacles as equipment and spatial limitations, or groups of swimmers of different ages and genders training at the same time, it is easy to see why many conditioning programs often feature the same types of exercises. After all, it i	s much more convenient to assign groups of athletes lots of push-ups, burpees, pull-ups and plyometric jumps, than it is to plan workouts based on their specific physical needs. In a sport like swimming, though, where kids are repeatedly taxing those same muscles in the water, one has to question the efficacy of such an approach. While its true that exercises like these might elicit an initial performance boost, their long-term impact should not be overlooked. Which begs the question. How do you provide swimmers of different ages, genders and levels of physical ability with a dryland program that prioritizes injury prevention, yet is still focused on delivering results?. Here are some guidelines that I use when designing workouts for my club team. Read through them and see if you are able to incorporate a few of these strategies into your existing dryland approach. Consider breaking training up according to gender: Since girls go through their peak growth spurt a little earlier, reach physical maturity more quickly and have different conditioning needs than boys, it is best to separate the two groups if possible. This way you could do more posterior chain strengthening -glutes, hamstrings and spinal erectors working as a unit- with your female swimmers, to help improve knee stability, as well as slightly modify upper body exercises -i.e. doing push-ups with hands on a low bench, or step- to make them more manageable. It would also allow you to include more of a flexibility emphasis with your male athletes- an area where they typically struggle. Plus, you will avoid a scenario where competitive kids strive to outdo each other in areas where they may not be as strong.',
                      is_shared=True,
                      tag=[tag_training, tag_swimming, tag_athlete])

    note_6 = add_user(title='Cycling for all',
                      author=user_mickey,
                      timestamp='2014-12-12',
                      content='Cycling is unique amongst sports. it is accessible to all as a leisure activity and means of transport. Over two billion people use bikes throughout the world, from all sorts of backgrounds, ages and physical ability. The benefits of cycling to individuals and to society are vast. Cycling every day to work reduces the risk of death from all causes by 28%, while employers and health care providers benefit due to fewer days off sick. More trips cycled means fewer car trips, leading to less congested streets, lower pollution levels, and fewer risks of injury to all road users. As the worldwide governing body for cycling, the Union Cycliste Internationale -UCI- knows that its mission is wider than looking after the sport. It must also join in partnership with those who advocate better conditions and safer roads to encourage more people to cycle for whatever reason. The UCI will work with cities hosting sports events to ensure a legacy of both sporting and everyday cycling. The UCI Advocacy Commission was created in 2014 to steer UCIs work in this area. Its members bring experience from various fields and across the globe.',
                      is_shared=True,
                      tag=[tag_cycling, tag_stress, tag_pollution])

    note_7 = add_user(title='WELCOME TO DOPING CONTROL',
                      author=user_mickey,
                      timestamp='2014-12-31',
                      content='Doping Control rules are in place for all athletes. Individuals attending major competitions are subject to drug testing regardless of whether or not they are a National Team member, an Olympian or a first place finisher. Doping Control rules can be confusing for athletes, coaches and parents, and it is critical that any questions-concerns be clarified. Costly mistakes can be made that not only count against the athlete, but count against all of USA Swimming. Doping Control takes place during competitions and with no-advance-notice -Out-of-Competition testing-. Athletes must check the status of all medications prior to using them, and ensure that they have filed the necessary paperwork to be in the strictest compliance with doping control rules. Swimmers are subject to testing by FINA -the international federation for aquatic sports world-wide-, the World Anti-Doping Agency -WADA-, and the United States Anti-Doping Agency -USAD-). USA Swimming is responsible for the compliance of U.S. Swimmers with the rules and regulations surrounding doping control and does not determine who is selected for testing.',
                      is_shared=False,
                      tag=[tag_athlete, tag_swimming])

    note_8 = add_user(title='Medellin',
                      author=user_ana,
                      timestamp='2014-05-31',
                      content='Medellin. Officially the Municipality of Medellin. Spanish: Municipio de Medellin, is the second largest city in Colombia and the capital of the department of Antioquia. It is located in the Aburra Valley, a central region of the Andes Mountains in South America. According to the National Administrative Department of Statistics, the city has an estimated population of 2.44 million as of 2014. With its surrounding area that includes nine other cities, the metropolitan area of Medellin is the second largest urban agglomeration in Colombia in terms of population and economy, with more than 3.5 million people.',
                      is_shared=False,
                      tag=[tag_colombia, tag_capital, tag_population, tag_area])

    note_9 = add_user(title='Prague',
                      author=user_ana,
                      timestamp='2014-10-13',
                      content='Prague is the capital and largest city of the Czech Republic. It is the fourteenth-largest city in the European Union.[5] It is also the historical capital of Bohemia. Situated in the north-west of the country on the Vltava River, the city is home to about 1.24 million people, while its larger urban zone is estimated to have a population of nearly 2 million.[6] The city has a temperate climate, with warm summers and chilly winters.',
                      is_shared=False,
                      tag=[tag_czech, tag_capital, tag_population])

    note_10 = add_user(title='Lisbon',
                       author=user_ana,
                       timestamp='2014-08-02',
                       content='Lisbon is the capital and the largest city of Portugal, with a population of 552,700 within its administrative limits in an area of 100.05 km2 Its urban area extends beyond the administrative city limits with a population of around 1.7 million people, being the 11th-most populous urban area in the European Union.[1] About 2.8 million people live in the Lisbon Metropolitan Area (which represents approximately 27% of the population of the country).[2] It is the westernmost large city located in continental Europe, as well as its westernmost capital city and the only one along the Atlantic coast. Lisbon lies in the western Iberian Peninsula on the Atlantic Ocean and the River Tagus.',
                       is_shared=True,
                       tag=[tag_portugal, tag_capital, tag_population, tag_area])

    note_11 = add_user(title='The Great Energy Travel',
                       author=user_mickey,
                       timestamp='2014-11-24',
                       content='Energy is an issue that touches every person on the planet. Thats why National Geographic, in partnership with Shell, has launched the Great Energy Challenge. The Great Energy Challenge convenes and engages influential citizens and key energy stakeholders in solutions based thinking and dialogue about our shared energy future. Its a call to action to become actively involved, to learn more and do more to change how we think about and consume energy so that we can all help tackle the big energy questions. It is one of the main causes of global warming.',
                       is_shared=True,
                       tag=[tag_stakeholders, tag_warming])

    note_12 = add_user(title='What Causes Global Warming?',
                       author=user_mickey,
                       timestamp='2014-12-23',
                       content='Scientists have spent decades figuring out what is causing global warming. They have looked at the natural cycles and events that are known to influence climate. But the amount and pattern of warming that has been measured can not be explained by these factors alone. The only way to explain the pattern is to include the effect of greenhouse gases (GHGs) emitted by humans.',
                       is_shared=True,
                       tag=[tag_warming, tag_climate, tag_greenhouse])

    note_13 = add_user(title='Effects of Global Warming',
                       author=user_mickey,
                       timestamp='2014-09-13',
                       content='The planet is warming, from North Pole to South Pole, and everywhere in between. Globally, the mercury is already up more than 1 degree Fahrenheit (0.8 degree Celsius), and even more in sensitive polar regions. And the effects of rising temperatures are not waiting for some far-flung future. They are happening right now. Signs are appearing all over, and some of them are surprising. The heat is not only melting glaciers and sea ice, it is also shifting precipitation patterns and setting animals on the move due to the climate changes.',
                       is_shared=False,
                       tag=[tag_warming, tag_climate])


def populate_tags():
    tag_mars = add_tag(label='mars',
                       slug='mars')

    tag_hubble = add_tag(label='Hubble Space Telescope',
                         slug='hubble_space_telescope')

    tag_alcohol = add_tag(label='alcohol',
                          slug='alcohol')

    tag_hangover = add_tag(label='hangover',
                           slug='hangover')

    tag_triathlon = add_tag(label='triathlon',
                            slug='triathlon')

    tag_training = add_tag(label='training',
                           slug='trining')

    tag_aerobic = add_tag(label='aerobic',
                          slug='aerobic')

    tag_metabolism = add_tag(label='metabolism',
                             slug='metabolism')

    tag_athlete = add_tag(label='athlete',
                          slug='athlete')

    tag_swimming = add_tag(label='swimming',
                           slug='swimming')

    tag_cycling = add_tag(label='cycling',
                          slug='cycling')

    tag_stress = add_tag(label='stress',
                         slug='stress')

    tag_pollution = add_tag(label='pollution',
                            slug='pollution')

    tag_colombia = add_tag(label='Colombia',
                           slug='colombia')

    tag_capital = add_tag(label='capital',
                          slug='capital')

    tag_czech = add_tag(label='Czech Republic',
                        slug='czech_republic')

    tag_portugal = add_tag(label='Portugal',
                           slug='portugal')

    tag_stakeholders = add_tag(label='stakeholders',
                               slug='stakeholders')

    tag_warming = add_tag(label='global warming',
                          slug='global_warming')

    tag_climate = add_tag(label='climate',
                          slug='climate')

    tag_greenhouse = add_tag(label='greenhouse gasses',
                             slug='greenhouse_gasses')


def populate_folders(user_list):

    folder_astronomy = add_folder(title='astronomy',
                                  owner=user_list[0], note43)

    # folder_health = add_folder(title='health',
    # author=user_pietro)
    #
    # folder_cities = add_folder(title='cities',
    #                            author=user_ana)
    #
    # folder_tarining = add_folder(title='training',
    #                              author=user_ana)
    #
    # folder_warming = add_folder(title='global warming',
    #                             author=user_mickey)
    #
    # folder_sports = add_folder(title='sports',
    #                            author=user_mickey)


def populate():
    user_tom = add_user('tomtom', 'tom', 'tom@tom.com', 'james', True)
    tag_portugal = add_tag(label='Portugal',
                           slug='portugal')
    note43 = add_note('Django', user_tom,timestamp='2014-11-24' , "Hello", tag_portugal)
    folder_astronomy = add_folder(title='astronomy', owner=user_tom, note=note43)
    # populate_users()
    # populate_notes()
    # populate_tags()
    populate_folders()


# Defining the add functions for our models

# # Function for adding user to our model
def add_user(username, first_name, email, password, is_active):
    u = User.objects.get_or_create(username=username, first_name=first_name, email=email, password=password,
                                   is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u


# Fill in the param with attributes related to note (title, content, timestamp)
def add_note(title, author, timestamp, content, is_shared, tag):
    # Look at add_user and how I have done it.
    n = \
    Note.objects.get_or_create(title=title, author=author, timestamp=timestamp, content=content, is_shared=is_shared,
                               tag=tag)[0]
    # You don't need to say n.save()
    return n


# Same applies for these two functions
def add_folder(title, author):
    f = Folder, object.get_or_create(title=title, author=author)[0]
    return folder


def add_tag(label, slug):
    t = Tag.objects.get_or_create(label=label, slug=slug)[0]
    return tag


# Start execution here!
## This is like public static void main(...) in Java
if __name__ == '__main__':
    ## Printing and importting necessary things
    print "Starting Pamm population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pamm.settings')
    from notes.models import User, Folder, Note, Tag
    from django.contrib.auth.models import User
    import django

    django.setup()

    # We are running the populate function we defined above
    populate()

    # If you are feeling adventurous you can make a class
    # which adds each model (i.e. a file populate_user etc.)
