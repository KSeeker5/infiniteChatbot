import random
from random import *

class BotController:
  # Static Members
  office_hours = {
      'Andrew'     : 'Thu 6-8',
      'Atallah'    : 'Wed 6-8, Wed 8-10',
      'Ben'        : 'Mon 6-8',
      'Divya'      : 'Mon 8-10',
      'Glenna'     : 'Thu 6-8, Thu 8-10',
      'Jake'       : 'Sun 4-6',
      'Jay'        : 'Wed 8-10',
      'Jessica'    : 'Mon 8-10',
      'John'       : 'Wed 8-10',
      'Joo Wan'    : 'Mon 8-10',
      'Leila'      : 'Mon 6-8, Wed 6-8',
      'Leon'       : 'Mon 6-8',
      'Marina'     : 'Thu 8-10',
      'Michelle'   : 'Sun 4-6, Wed 6-8',
      'Rachel'     : 'Thu 6-8',
      'Ryan'       : 'Mon 8-10, Thu 8-10',
      'Salah'      : 'Sun 6-8',
      'Sam'        : 'Thu 6-8',
      'Tahiya'     : 'Thu 8-10',
      'Xhama'      : 'Sun 6-8, Mon 6-8',
      'Bloomfield' : 'at an unknown time',
      'Floryan'    : 'at an unknown time',
    }

  OH_WORDS       = ['office hours', 'oh']
  GREETING_WORDS = ['hello', 'hi', 'what\'s up'] 
  HELP_WORDS     = ['help', 'you do?', 'who']
  
  COPYPASTA_WORDS = [
    'copypasta', 'meme', 'gort', 'Gort',
    'test'
    ]
  
  COPYPASTA_VALUES = [
    'What the fuck did you just fucking say about me, you little shit? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldnt, you didnt, and now youre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. Youre fucking dead, kiddo.',
    'I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I\'m fucking retarded but I don\'t care, I\'m beautiful. I\'m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me "Apache" and respect my right to kill from above and kill needlessly. If you can\'t accept me you\'re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.',
    'hi every1 im new!!!!!!! holds up spork my name is katy but u can call me t3h PeNgU1N oF d00m!!!!!!!! lol…as u can see im very random!!!! thats why i came here, 2 meet random ppl like me _… im 13 years old (im mature 4 my age tho!!) i like 2 watch invader zim w/ my girlfreind (im bi if u dont like it deal w/it) its our favorite tv show!!! bcuz its SOOOO random!!!! shes random 2 of course but i want 2 meet more random ppl =) like they say the more the merrier!!!! lol…neways i hope 2 make alot of freinds here so give me lots of commentses!!!! DOOOOOMMMM!!!!!!!!!!!!!!!! <--- me bein random again _^ hehe…toodles!!!!! \n love and waffles, t3h PeNgU1N oF d00m',
    'Here\'s the thing. You said a "mountain lion is a lion." Is it in the same family? Yes. No one\'s arguing that. As someone who is a scientist who studies lions, I am telling you, specifically, in science, no one calls mountain lions "lions". If you want to be "specific" like you said, then you shouldn\'t either. They\'re not the same thing. If you\'re saying lion family" you\'re referring to the taxonomic grouping of Felidae, which includes things from house cats to ocelots to tigers. So your reasoning for calling a mountain lion a lion is because random people "call the big ones lions?" Let\'s get panthers and leopards in there, then, too. Also, calling someone a human or an ape? It\'s not one or the other, that\'s not how taxonomy works. They\'re both. A mountain lion is a mountain lion and a member of the lion family. But that\'s not what you said. You said a mountain lion is a lion, which is not true unless you\'re okay with calling all members of the lion family lions, which means you\'d call house cats, tigers, and other cats lions, too. Which you said you don\'t. It\'s okay to just admit you\'re wrong, you know?',
    'Here\'s the thing. You said "Shrek is love." Are they in the same family? Yes. No one\'s arguing that. As someone who is a neuroscientist who studies emotions, I am telling you, specifically, in science, no one calls Shrek love. If you want to be "specific" like you said, then you shouldn\'t either. They\'re not the same thing. If you\'re talking about "love" you\'re referring to a wide range of emotions, which includes things from adoration to compassion to sentimentality. So your reasoning for calling Shrek love is because hundreds of random people have had intimate relations with him? Let\'s get my ex-wife in there, then, too. It\'s okay to just admit you\'re wrong, you know?',
    'Here\'s the thing. You said a "a PC game is a sport." Is it in the same family? Yes. No one\'s arguing that. As someone who is a a mod of /r/pcmasterrace who studies PC games, I am telling you, specifically, in PC gaming, no one calls video games sports. If you want to be "specific" like you said, then you shouldn\'t either. They\'re not the same thing. If you\'re saying "Video games" you\'re referring to the taxonomic grouping of MOBAS, which includes things from DOTA to LoL to SMITE. So your reasoning for calling a PC game a sport is because random people "call the MOBAS Sports?" Let\'s get counter-strike and starcraft in there, then, too. Also, calling someone a human or an ape? It\'s not one or the other, that\'s not how taxonomy works. They\'re both. A MOBA is a MOBA and a member of the Video game family. But that\'s not what you said. You said a PC game is a Sport, which is not true unless you\'re okay with calling all members of the video game family sports, which means you\'d call Visual novels, RPG\'s, and other games sports, too. Which you said you don\'t. It\'s okay to just admit you\'re wrong, you know?',
    'Here\'s the thing. You said a "queef is a fart." Is it in the same family? Yes. No one\'s arguing that. As someone who is an Alabama redneck who studies farts, I am telling you, specifically, in Alabama, no one calls queefs farts. If you want to be "specific" like you said, then you shouldn\'t either. They\'re not the same thing. If you\'re saying "fart family" you\'re referring to the gastronomic grouping of flatulence, which includes things from shit bubbles to tear-assers to Alabama mweep-mwoppers. So your reasoning for calling a queef a fart is because random people "call the ass ones farts?" Let\'s get diarrhea and bloodfarts in there, then, too. Also, calling someone a Newfoundlander or a gassy person? It\'s not one or the other, that\'s not how gastronomy works. They\'re both. A queef is a queef and a member of the fart family. But that\'s not what you said. You said a queef is a fart, which is not true unless you\'re okay with calling all members of the fart family farts, which means you\'d call piss, the runs, and other waste removal processes farts, too. Which you said you don\'t. It\'s okay to just admit you\'re gassy, you know?',
    'My Nana is still a looker, even at eighty. Whenever I bathe her in the driveway, I\'m always impressed by her sinewy physique. I\'ll be like "Nana you\'re ripped bro" and she\'ll be like \"nothing but clean living and good genes\" then I\'ll be like \"clean living? You ain\'t been sober an entire day since Nixon was still on the teet\" and she\'ll be like \"you\'d drink too if you had such a shitty family\" and I\'ll be like \"maybe if you didn\'t have so much side wang pop-pop wouldn\'t have moved to Reno\" and she\'ll be like \"he moved to Reno because Schenectady was getting overrun with Mexicans\" and I\'ll be like \"Nana that\'s racist\" then she\'ll say \"then why don\'t you move there.\" This goes on until I\'m done hosing her off, at which point I take her back inside, but her in front of a TV playing Diagnosis: Murder reruns, and give her a box of wine with a straw. Old people need the routine.',
    'If you are reading this, then you are wasting precious time reading the comments. You will probably comment or like this, but you will waste more time. You are now thinking what I am on about, probably thinking that I am on something. However you are just wasting more time reading my comment. I have just wasted precious moments of your life that you could have spent sleeping or smoking weed. If you just realised, I have wasted more time explaining that I have wasted time. For this reason you might as well like this comment, as you might as well waste more time. Thank you for your wasted time.',
    'iPhone is the best console, and nobody could ever fucking speak against it. When I first got an iPhone, I was so excited that I wouldn\'t be trashy anymore. I got so many friends with the iPhone 5C\'s stunning colors and sexyness, and that isn\'t even half of it. It has over 30 GB worth of data. I was able to store, if I recall, 10,000 photos and it would only take up 4 gigabytes. It would play games that would seem laggy to a console and turn it into a lagless portable experience. I am a true fucking gamer, I play Angry Birds, Fruit Ninja, Flappy Bird, and Clash of Clans daily, I can message friends and stay up to date, I can talk to people with my face and always remember how my friends looked like, I can take endless photos with no worry about using data, and I could browse infinite pages of the internet, which a shitty console can\'t do. The PC, Wii, PS4, and Xbox 1 can\'t do any of this shit. Compete with that, consoletards. Also, nice trolling fucko, with you\'re not including you\'re fucking iPhone, get your facts strate Android fuckers.',
    'Imagine this. You are attracted to women, like you are now (emotionally and sexually), but they do not exist. They existed a long time ago, and no one knows what they looked like (They have a pretty good idea from the fossils, however), but they do not exist anymore. That means, not only do you know there will never be any possibility, of you having sex with one, but there;s not even a possibility of you ever seeing one in real life. Everyone else, however, except for a very few, are not attracted to women, they are attracted to something else entirely. So, in other words, you will never find any porn anywhere on the internet, only non-sexual pictures of women. Everyone you have told about your attraction to women think it\'s disgusting. To relieve yourself, you get off on the non-sexual pictures of women, knowing it will never get any better. That’s what life is like to me. I am a degree 6 Zoosexual, sexually and emotionally attracted to Tyrannosaurs and nothing else. Women don’t even do it for me. I am cursed',
    'I r8 8/8: Gr8 b8, m8. I rel8, str8 appreci8, and congratul8. I r8 this b8 an 8/8. Plz no h8, I\'m str8 ir8. Cr8 more, can\'t w8. We should convers8, I won\'t ber8, my number is 8888888, ask for N8. No calls l8 or out of st8. If on a d8, ask K8 to loc8. Even with a full pl8, I always have time to communic8 so don\'t hesit8. dont forget to medit8 and particip8 and masturb8 to allevi8 your ability to tabul8 the f8. We should meet up m8 and convers8 on how we can cre8 more gr8 b8, I\'m sure everyone would appreci8, no h8. I don\'t mean to defl8 your hopes, but its hard to dict8 where the b8 will rel8 and we may end up with out being appreci8d, I\'m sure you can rel8. We can cre8 b8 like alexander the gr8, stretch posts longer than the Nile\'s str8s. We\'ll be the captains of b8, 4chan our first m8s the growth r8 will spread to reddit and like real est8 and be a flow r8 of gr8 b8, like a blind d8 we\'ll coll8, meet me upst8 where we can convers8, or ice sk8 or lose w8 infl8 our hot air baloons and fly, tail g8. We could land in Kuw8, eat a soup pl8 followed by a dessert pl8 the payment r8 won\'t be too ir8 and hopefully our currency won\'t defl8. We\'ll head to the Israeli-St8, taker over like Herod the gr8 and b8 the jewish masses, 8 million, m8. We could interrel8 communism, thought it\'s past it\'s maturity d8, a department of st8, volunteer st8. reduce the infant mortality r8, all in the name of making gr8 b8 m8.',
    'Here in my garage, just bought this new TOP SNIPER IN THE ENTIRE US ARMED FORCES here. It’s fun to KILL YOU IN OVER SEVEN HUNDRED WAYS up here in the Hollywood hills. But you know what I like more than THE NAVY SEALS? GORILLA WARFARE. In fact, I’m a lot more proud of these NUMEROUS SECRET RAIDS ON AL-QUAEDA that I had to get installed to hold OVER 300 CONFIRMED KILLS that I bought. It’s like the TOP SNIPER Warren Buffett says, “the more you PREPARE FOR THE STORM, the more you DROWN IN IT.” Now maybe you’ve seen my SECRET RAID ON AL-QUAEDA where I talk about how I WIPE OUT a TARGET a day. You know, I WIPE OUT a TARGET a day not to show off it’s again about the UNHOLY RETRIBUTION. In fact, the real reason I keep this TOP SNIPER here is that it’s a reminder. A reminder that YOU ARE NOTHING TO ME BUT JUST ANOTHER TARGET, because it wasn’t that long ago that I was A GODDAMN IDIOT sleeping on a couch in a mobile home with only forty seven CONFIRMED KILLS in my NETWORK OF SPIES. I didn’t have ACCESS TO THE ENTIRE ARSENAL OF THE UNITED STATES MARINE CORPS, I had no opportunities. But you know what? Something happened that changed my life. I bumped into a CONFIRMED KILL. And another CONFIRMED KILL. And a few more CONFIRMED KILLS. I found five CONFIRMED KILLS. Again, it’s not just about money, it’s about the good life; GORILLA WARFARE, THE NAVY SEALS, UNARMED COMBAT and CONFIRMED KILLS. And so I record a little SECRET RAID, it’s actually on my website, you can click here on this video and it’ll take you to my website where I share three WAYS TO KILL WITH MY BARE HANDS that they taught me. Three COMBAT TACTICS that you can implement today no matter where you are, KIDDO. Now, this isn’t a “get CONFIRMED KILLS quick” scheme. You know, like they say if KILLS sound too good to be true they are too good to be CONFIRMED. I’m not promising you that tomorrow you’re gonna be able to BECOME THE TOP SNIPER IN THE ENTIRE US ARMED FORCES. But what I am telling you is that it can happen faster than you think if you know the proven TACTICS. So, I record a little two minute SECRET RAID on my website. Like I said, now it’s not the most professional I just shot it here with my ENTIRE ARSENAL OF THE UNITED STATES MARINE CORPS, but it’s real. Nobody can argue, this is my CONFORMED KILL. And I’m going to give you the three most important KILLS you can do today. So click the link, go there it’s completely free to watch it it’s just a couple minutes. Invest in your KILLS. Always be curious. Don’t be a MAGGOT. Okay, people see videos like this and they say “Ah that’s not real that’s for somebody else.” Don’t listen, don’t listen. Be an optimist. Like, Conrad Hilton, the TOP SNIPER who started Hilton Hotel, he said that he was only fifteen years old when he GOT HIS FIRST CONFIRMED KILL, and that changed his life. CONFIRMED KILLS can change your life. And in that SECRET RAID, Helen Keller said “SHIT FURY” so if you’re a MAGGOT, if you’re a LITTLE SHIT you don’t need to click here. Don’t worry about it, I don’t need to talk to MAGGOTS. But if you’re somebody who knows GORILLA WARFARE, cause the KILLS are possible, you know, for some of you watching it’s not necessarily a TOP SNIPER, maybe it’s a SECRET RAID ON AL-QUAEDA, a new CONFIRMED KILL, starting your own NETWORK OF SPIES. Maybe it’s a new lifestyle without so much stress, GRADUATING TOP OF YOUR CLASS IN THE NAVY SEALS, doing those things you know you’re destined to do. You can\'t do those unless you understand GORILLA WARFARE. Money, I don’t call it money anymore, I call it CONFIRMED KILLS. You must have enough KILLS to live out your dream and to live out your destiny. So, I’ll see you on my website, it’s a quick video and you’ll see there absolutely free. So just click this video and you’ll be taken there in a second, and uh, I’m excited to share these COMBAT TACTICS. You’ll see, not because of anything of me but because I’ve been fortunate enough to learn from SNIPERS many years ahead of me. Not just in SECRET RAIDS ON AL-QUAEDA like these, although I love CONFIRMED KILLS but also real in-person TOP SNIPERS. So let me share with you these three COMBAT TACTICS that have made all the difference in my life. They’re practical, you can do them today, you can start on them today. All right? See you there on my site.',
    'I was only 9 years old I loved shrek so much, I had all the merchandise and movies I pray to shrek every night before bed thanking him for the life I\'ve been given. Shrek is love I say, Shrek is life My dad overhears me and calls me a faggot I knew he was just jealous of my devotion for Shrek I called him a cunt He slaps me and sends me to go to sleep Im crying now, and my face hurts I lay in bed and its really cold A warmth is moving towards me. I feel something touch me Its shrek I am so happy He whispers in to ear "this is my swamp He grabs me with his powerful ogre hands and puts me on my hands and knees I\'m ready I spread my ass cheeks for Shrek He penetrates my butthole It hurts so much but I do it for Shrek I can feel my butt tearing as my eyes start to water I push against his force I want to please Shrek He roars a mighty roar as he fills my butt with his love My dad walks in Shrek looks him straight in the eye and says "Its all ogre now" Shrek leaves through my window Shrek is love, Shrek is life',
    'Astounding! You have managed to expend effort creating a non-random string of characters which usually convey meaning, yet your overall comment was ABSOLUTELY POINTLESS! It is as though all of the industries of mankind were operated in reverse, with great will and endeavor being used to convert items of usefulness into worthless bare materials! you are the antithesis of all that is grand and great about mankinds capacity for thought and self-determination. You sir, are the mirror image of a meaningful entity, lower than base matter, lower than oblivion, because unlike the brutish deterministic plasma of the unreasoning cosmos, you CHOSE to be without value or worth. Or in the parlance of thine own ilk: LOL N0 UR GAYYYYYYYYYYYYYY!!!11ONE!!!!!ELEVENTY!!!!11!',
    'AT LEAST I DON\'T SPEND MY TIME SUCKING DICKS IN THE BATHROOM AT OLIVE GARDEN. YOU DIRTY LOWDOWN SLIMY FILTHY DISGUSTING GLUTTONOUS HOGLIKE MOTHER FUCKING COCK SUCKING SON OF AN INCESTUOUS PEDOPHILE SHEMALE RAPIST PROSTITUTE. GET YOUR MOM\'S DICK OUT OF YOUR MOUTH. DO YOU KNOW WHAT I\'M GONNA DO? I\'M GONNA SHIT SO FAR UP YOUR ASS. STOP FOR A MOMENT AND REALLY GRASP THAT STATEMENT. I AM LITERALLY GOING TO SHIT UP YOUR ASS. I WILL TAKE MY PANTS OFF, RIP YOUR PANTS OFF, OUR SPHINCTERS WILL TOUCH, AND I WILL SHIT. YOU WILL TRY TO COUNTERSHIT. BUT MY SPHINCTER WILL OVERCOME. AND I WILL PUSH A LOG OF SHIT FROM MY ASS UP INTO YOUR BODY. THIS IS WHAT SHALL OCCUR WHEN I FIND YOUR KEYBOARD FUCKING FACE. YOU KNOW WHAT ELSE? I WILL PISS INTO A POT. I WILL ADD CORNSTARCH TO THE PISS AND BOIL IT UNTIL IT GETS REALLY THICK, LIKE SAUCE. I WILL POUR THE THICKENED PISS INTO A PLASTIC CONTAINER AND PUT IT IN THE FRIDGE UNTIL IT HARDENS INTO A FIRM JELLO. THEN I WILL THEN CUT IT INTO RECTANGLES. BATTER IT IN A MIX OF MILK, FLOUR, AND EGGS. AND DEEP FRY IT AT 375 UNTIL GOLDEN BROWN, FLIPPING ONCE SINCE THEY FLOAT. AND I WILL SERVE YOU MY DEEP FRIED PISS. THAT\'S WHAT YOU GET FOR BEING SUCH A FAGGOT. COCKMUFFIN',
    'I\'m more educated than you, in every way shape and form. Also more intelligent than you (exponentially so). I am better than you, in every facet of life, and I don\'t even know you, however, I just know, that I am. Also, we aren\'t bro\'s. If anything, you are someone I assign less value and worth than my own feces. Your life has no value, and you will make no contribution to this world, in your entire life, because of your low intelligence, and lack of skills. How does that feel, you fucking bottom denominator. go back to you vegan subreddit to fill your useless void of a life, pretending it means anything. Am I a narcissist? I don\'t know, I am a fucking God. I will, do, and have succeeded in every facet of life. I have done more, in this year alone, than you will have achieved before you leave this world... let that sink in. You have no fucking clue who you are talking to. I am so vastly superior, and intelligent, that I can infer all of this, with 100% accuracy. You are like a fucking ant, and I am a GOD. You do not even fly on my radar, let alone get acknowledgement, from the likes of me. I know you can sense my superiority, my power, my intelligence,and you are trying to pretend you don\'t feel it, its real. To conclude, go back to fucking yourself, you meaningless water-trash bottom feeding peasant.',
    'You\'ve won nothing shithead. Wallow in the shit you\'ve created. Because soon, all you\'ve worked for will vanish and you\'ll be left with nothing. When you least expect it, the shit you talk, you\'ll choke on it.',
    'bitch u mad mf ugly b looking like the little ginger kid from little einstein kill urself btch ill shoot u mf ass meet me irl fuck outta here wicho dorito ass shaped head btch albino gorilla lookin ass mf ill flame u dumb spotty white pizza shaped head lookin elongated ass nose marshmallow man crusty ass mf self right here btch',
    'Wow. Okay. OKAY. OKAY. Yabba Dabba FUCK you and YABBA DABBA FUCK your shitty FUCKING memes. You are literally worth nothing to me. If I saw your FUCKING UGLY ASS FACE on the street, I\'d take a big loaded shotgun to your mouth, faggot. I have always wanted to murder you, your family, your friends, and your pet goldfish since the day I was born. Brain Blast? How about I fucking blast your faggot ass brain with a shotgun. I want to fucking candy crush your face through a mother fucking wall. You are the reason why babies cry. Fuck your memes. Fuck you. Fuck. FUCK. FUCK. Try fucking saying that to be in REAL life where you aren\'t surrounded by a precious username and see what happens, weakling. I have guns. Many guns. Guns that I could take to your head and blow it out right now. You hear me? Good.',
    'Downvoted. You\'re exactly what\'s wrong with circlejerk. Instead of posting satire, mocking reddit and being clever and original, you continue to post lame phrases and beat to glue anything that was even remotely funny, all under the guise that you want to show what\'s wrong with reddit. You don\'t care about reddit. You belong to the system that this subreddit was made to mock. You seek karma. You seek to be a power-user, a well-known name in a sea of perpetual anonymity. The higher your karma-count, the more you get off on it. You are smug and self-satisfying. You are the problem. There should be a "delete" button below your posts. Start clicking them after you post and you\'ll find that reddit starts to improve.',
    'My Grandfather smoked his whole life. I was about 10 years old when my mother said to him, \'If you ever want to see your grandchildren graduate, you have to stop immediately.\'. Tears welled up in his eyes when he realized what exactly was at stake. He gave it up immediately. Three years later he died of lung cancer. It was really sad and destroyed me. My mother said to me- \'Don\'t ever smoke. Please don\'t put your family through what your Grandfather put us through." I agreed. At 28, I have never touched a cigarette. I must say, I feel a very slight sense of regret for never having done it, because your post gave me cancer anyway.',
    'You fucking do that every damn time I try to talk to you about anything even if it\'s not important you just say K and to be honest it makes me feel rejected and unheard like nothing would be better then that bullshit who the fuck just says k after you tell them something important I just don\'t understand how you think that\'s ok and I swear to god you\'re probably just gonna say k to this but when you do you\'ll know that you\'re slowly killing me inside'
    ]

  # Field List:
  #  (none)
  
  def __init__(self):
    pass
  
  #def generate_copypasta():
    #loop_control = 1 # Loop control variable. 1 means loop, 0 means stop
    #while loop_control = 1
    #return COPYPASTAS.__len__()
    #copypasta_number = randint(1, len(COPYPASTAS))-1    # Pick a random number between 1 and length of copypasta array
    #result = COPYPASTAS[copypasta_number]
    #return result
  
  def text_preprocessing(self, text):
    return text.lower()

  def process_message(self, recd_msg):
    msg_to_send = {} # reply
    
    # Preprocessing
    text = recd_msg['text'].lower()

    # Helper function
    used_any = lambda word_list: any(map(lambda x : x in text, word_list))

    # Use some hard-coded rules to decide what this message says
    #if 'when' in text and used_any(BotController.OH_WORDS):
      #msg_to_send['text'] = 'You\'re asking about someone\'s office hours!'
    if used_any(BotController.GREETING_WORDS):
      msg_to_send['text'] = 'Greetings to you, as well, {}!'.format(recd_msg['author'])
    elif used_any(BotController.HELP_WORDS):
      msg_to_send['text'] = ('I am Infinite, and I have been born in the absense of the almighty Zo.' +
                             ' If you decide to align yourself with the misguided Gort, you will find' + 
                             ' that I have even less mercy than him. If you\'re curious, go ahead and' + 
                             ' say something to me. Who knows what will happen in your new reality. \n')
    else# used_any(BotController.COPYPASTA_WORDS):
      num_of_copypastas = randint(1, 5) #Pick a random number between 1 and 5
      msg_to_send['text'] = ''
      copypasta_counter = 0
      while copypasta_counter<num_of_copypastas:
        #copypasta_number = randint(0, len(COPYPASTA_VALUES)-1)    # Pick a random number between 0 and length of copypasta array (minus 1)
        #copypasta_number = randint(0, 1)    # Pick a random number between 0 and length of copypasta array (minus 1)
        #generated_copypasta = COPYPASTA_VALUES[copypasta_number]
        msg_to_send['text'] += choice(BotController.COPYPASTA_VALUES) #generated_copypasta
        msg_to_send['text'] += '\n\n'
        #msg_to_send['text'] += 'a'
        copypasta_counter+=1
    #else:
      #msg_to_send['text'] = 'What nonsense is this you are spouting?'

    return msg_to_send
