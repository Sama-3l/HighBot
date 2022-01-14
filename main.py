import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
import asyncio

cl = discord.Client()

sad_words = ["sad", "sadness", "depression", "depressed", "unhappy", "miserable", "depressing", "nostalgia", "racism", "death", "dead", "dard", "life", "meaning", "joke", "bura", "dil", "not ok", "fine?", "mad"]
exercise_words = ["exercise", "fat", "obese", "huge"]
music_words = [
  "musician", "guitarist", "vocalist", "pianist", "guitar", "piano", "drummer", "drums"
  ]
racism_words = ["black", "white", "racist", "sexist", "discrimination"]
relation_words = ["relationship", "relation", "wife", "date", "waifu", "gf", "bandi", "ladki", "female"]
skills_words = ["Program", "programming", "python", "java", "c++", "machine learning"]
rick_roll = ["never gonna", "you up", "to love", "no strangers", "Gotta make", "so long", "say goodbye"]
jo_baat = ["jo baat", "je baat", "jee baat", "joo baat", "jooo baat", "je baaat", "je baaaat", "jee baaat", "jee baaaat"]
mauj_kardi = ["bhosdike bete", "bsdk bete", "mauj kardi", "oo bete"]
abey_saale = ["abey saale", "abhe saale", "abe saale", "abe saaale", "abee saale"]
maaf_karna = ["gusse me", "maaf karna"]
not_interested = ["not interested", "suna hi nahi hai", "nahi sun na", "nahi sunna"]
look_here = ["aa ja", "aa jao"]
how_to_talk = ["baap se aise"]
no_strategy = ["strategy?", "no idea"]
saram = ["sharam", "izzat"]
dont_know = ["you are"]
politics = ["sarkaar chutiya", "gormint", "gorment", "politics"]
go_corona = ["corona", "covid"]
kya_baat = ["kya baat hai"]
speak = ["kya?", "kya??", "kya???", "kya bol rha", "fir se bol", "what?", "what??"]
money_waste = ["paise barbaad"]
lawdu = ["lawde", "laudu", "lodu"]
ok = ["ye bhi theek hai", "theek hai"]
adios = ["bye", "adios", "good night", "gn"]
bonjour = ["yo ", "haalo", "good morning", "i am here", "aagaya", "bonjour", "helllo", "henlo", "hemlo"]

starter_encourage = [
  "I'm not depressed, you are.",
  "Sadness is the crutch of the weak",
  "What if emotions can be pleasant, when you learn to open your mind? Think about that",
  "There is a proven link between madness and abuse",
  "How can you know for sure a special person is not a venture capitalist? A venture capitalist never steals",
  "An apocalypse can be an alley. It is also a java update",
  "Nostalgia is truly one of the greatest human weaknesses, second only to the neck",
  "Small pp.",
  "In our asses begin everything",
  "You hunk",
  "Don't get angry over others' silence. Just eat",
  "You are about to turn into a party shit. Be more upfront about yourself. NOW!",
  "Modern civilization: The most overrated fairytale of them all.",
  "No confusion.... No, confusion.",
  "Lawful is he that sinneth against his swine, and know that no individual yet honoured his own next of kin, but not squandered and regretted it",
  "Aspire to romance. Don't just do what's expected of you.",
  "Those who do not swallow mind control, do not defeat death",
  "Sadism is the love child of morality and melanchony",
  "Contextualize. Aim below. Feel angry about. Get confused about.",
  "Acts of cruelty will make you anticipate what any sane person would see as unanticipatable.",
  "Don't be sad. Become dead.",
  "Painify youthism. Moraeleialize snailification.",
  "Call your congressman if colleague isn't arousing",
  "A home wreaker always laughs",
  "The law defines character strength as lying to oneself and making it look cool",
  "A dollar bill lying on the street can be a soul from your heart",
  "It takes a lot of self abuse to become great within the art of praying",
  "You are a wonderful loverboy",
  "With bad questioning comes bad thinking",
  "Between sunshine and opium there's a robot",
  "Banks end where public restrooms begin",
  "Spread disinformation about toxins",
  "Feed the suspicions",
  "Imitate the devil",
  "Believe in yourself and be the first person to lose something that nobody else can lose",
  "Be a pretend person",
  "Don't look for meaning. Clap your ass.",
  "First they squeeze you. Then they remove you, and then they say you.",
  "Learn from negativity. Recieve computers",
  "PSYCHATRISTS. Are they real?",
  "Life is politically correct.",
  "Being alive is all about being shockingly brain-washed",
  "Be the first person in the world to discover what others find undiscoverable",
  "Misinterpreting everything inspires popularity",
  "Ban incompetence.",
  "After a joke, comes the rain.",
  "If you are your true self in the boat, it is just your own boat",
  "You don't have to become president to get crucified.",
  "Act like a moron and get fucked",
  "A fool is a cave. It is also a light."
]

exercise = [
  "All you need to exercise regularly is a gun and a best friend",
  "Eating pigs is like eating diseases",
  "It takes a lot of self abuse to become great within the art of praying",
  "Spread disinformation about toxins",
  "Could it be that conspiracies against mankind are how they are because everything is eternal?",
  "Ban incompetence",
  "Has gluttony set in motion the apocalypse?",
  "If you wait for others to follow, wake up",
  "Breakfast isn't about annhilating yourself. It's about hypnotizing yourself."
]
racism = [
  "Maybe what you call genders are not innocent",
  "Lawful is he that sinneth against his swine, and know that no individual yet honoured his own next of kin, but not squandered and regretted it",
  "Sadism is the love child of morality and melanchony",
  "The law defines character strength as lying to oneself and making it look cool",
  "Imitate the devil",
  "Could it be that conspiracies against mankind are how they are because everything is eternal?",
  "Ban incompetence(Chinese)"
]
music = [
  "Knowing that you are a musician doesn't actually make you a lawyer",
  "Before the music, comes the perversion",
  "Is modern art sexy?",
  "Art regulations. NEUTRALIZE PRODUCTIVENESS!!",
  "Sadism is the love child of morality and melanchony",
  "Being creative can be disadvantage"
  "Ban incompetence"
]
relation = [
  "Without a marriage there can be no neighbourhood",
  "Seek not pleasure. Not needful things",
  "You are a wonderful loverboy",
  "Build a bridge out of her",
  "Could it be that conspiracies against mankind are how they are because everything is eternal?",
  "Talents can become a lot of fun",
  "Bros before hoes. Why? Coz your bros are always there for ya. They have got ur back, after your hoe rips your heart out for no good reason. And you were nothing but great to your hoe and that she was better than all the other hoes in the world and then..... Then suddenly she's not your hoe no mo. Think about that.",
  "Should masturbation be profitable",
  "Inaptitude can be described as pretending to be handicapped to get in touch with girls",
  "Being creative can be a disadvantage",
  "Ban incompetence in bed",
  "Don't go into oblivion, just keep inbreeding",
  "Act like a moron and get fucked"
]
skills = [
  "Programming is not about getting one's head above water, but trying to walk on the water",
  "Talents can become a lot of fun",
  "Learn from negativity. Recive computers.",
  "Being creative can be a disadvantage",
  "Ban incompetence",
  "You don't have to become president, to get crucified."
]

quote_authors = [
  "Mr. KnowItAll",
  "Some sadist bitch",
  "Some famous person no-one knew",
  "Every other high dude",
  "Your friendly neighbourhood ball-sack",
  "Bibbity-Boppity. 10 iq",
  "One sarcastic mf",
  "Ishan",
  "Raka",
  "Bhalla",
  "VSauce",
  "Donald Trump",
  "Pornographic Historian",
  "Anime Tiddies Expert",
  "Professional Street Nigga",
  "Chicken Nugget Scientist",
  "Space Lawyer",
  "Bread Scientist",
  "Gingerbread Man",
  "Discovery Channel at 1 am",
  "A celebrated Prostitute",
  "Some E-girl",
  "A familiar SIMP",
  "Drunk Astronaut",
  "Sam, a stupid little bitch"
]

helps = [
  "When you are sad, I help you with some encouraging AI generated words and also have other triggering words that you will find out. To test, try typing that you are sad",
  "Type ^inspire to be inspired"
]

rick_rolled = """
  We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye"""

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + random.choice(quote_authors)
  return(quote)

@cl.event
async def on_ready():
  print('We have logged in as {0.user}'.format(cl))
  print(len(cl.guilds))
  await cl.change_presence(activity=discord.Game(name=" with your mom, lol... Also ^inspire. ^help"))

async def status():
  await cl.wait_until_ready()
  statuses = ["^inspire. ^help", "with your mom"]
  while not cl.is_closed():
    await cl.change_presence(activity=discord.Game(name=random.choice(statuses)))
    await asyncio.sleep(2)

@cl.event
async def on_message(message):
  if message.author == cl.user:
    return
  
  msg = message.content
  msg = msg.lower()

  if message.content.startswith('^inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encourage))

  if any(word in msg for word in exercise_words):
    await message.channel.send(random.choice(exercise))
  
  if any(word in msg for word in racism_words):
    await message.channel.send(random.choice(racism))

  if any(word in msg for word in music_words):
    await message.channel.send(random.choice(music))

  if any(word in msg for word in skills_words):
    await message.channel.send(random.choice(skills))

  if any(word in msg for word in relation_words):
    await message.channel.send(random.choice(relation))

  if any(word in msg for word in rick_roll):
    await message.channel.send(rick_rolled + "\n\n\nhttps://youtu.be/dQw4w9WgXcQ")

  if any(word in msg for word in jo_baat):
    await message.channel.send(file=discord.File("jo_baat.jpg"))
    
  if any(word in msg for word in mauj_kardi):
    await message.channel.send(file=discord.File("mauj_kardi.gif"))

  if any(word in msg for word in abey_saale):
    await message.channel.send(file=discord.File("abey_saale.jpg"))

  if any(word in msg for word in maaf_karna):
    await message.channel.send(file=discord.File("maaf_karna.jpg"))

  if any(word in msg for word in look_here):
    await message.channel.send(file=discord.File("look_here.jpg"))

  if any(word in msg for word in how_to_talk):
    await message.channel.send(file=discord.File("maa_baap_se_baat.jpg"))

  if any(word in msg for word in no_strategy):
    await message.channel.send(file=discord.File("no_strategy.jpg"))

  if any(word in msg for word in saram):
    await message.channel.send(file=discord.File("saram.jpg"))

  if any(word in msg for word in dont_know):
    await message.channel.send(file=discord.File("Tu_hai.jpg"))
  
  if any(word in msg for word in politics):
    await message.channel.send(file=discord.File("politics.jpg"))
  
  if any(word in msg for word in go_corona):
    await message.channel.send(file=discord.File("go_corona.jpg"))

  if any(word in msg for word in not_interested):
    await message.channel.send(file=discord.File("not_interested.jpg"))

  if any(word in msg for word in kya_baat):
    await message.channel.send(file=discord.File("kya_baat.jpg"))

  if any(word in msg for word in speak):
    await message.channel.send(file=discord.File("speak_correctly.jpg"))

  if any(word in msg for word in money_waste):
    await message.channel.send(file=discord.File("waste_money.jpg"))

  if any(word in msg for word in lawdu):
    await message.channel.send(file=discord.File("Yes.jpg"))

  if any(word in msg for word in ok):
    await message.channel.send(file=discord.File("ok.jpg"))

  if any(word in msg for word in adios):
    await message.channel.send(file=discord.File("adios.jpg"))

  if any(word in msg for word in bonjour):
    await message.channel.send(file=discord.File("bonjour.jpg")) 

  if message.content.startswith('^help'):
    await message.channel.send(helps[0])
    await message.channel.send(helps[1])

cl.loop.create_task(status())
keep_alive()
cl.run(os.environ['key'])