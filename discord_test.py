
'''
more simplified chan for better use and updatability
'''

import sys , os , discord , subprocess , json , io , random , COVID19Py ,time ,numpy,glob,asyncio

botid = "eheheh no :D pls"

#file variables
f = io.open("call.json", mode="r", encoding="utf-8")
filesend = None


#reply handling variables
flag = False
secondary_flag = False

rep_pkg = json.load(f)

#uselessly useful variables
spc = " "
cv19 = COVID19Py.COVID19()
client = discord.Client()
oldfile = []



def system_call(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return (output,err)

@client.event
async def on_ready():
    global oldfile
    print("Bot's Up and runnin bois")
    activity = discord.Game(name="Helping Pacchu Fail")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_member_update(before, after):
    global flag,filesend,oldfile
    channel = client.get_channel(709419678723866635)

    try:
        msgfile = open("whatsappmessages.txt","r")
        msgs = msgfile.readlines()
        if(len(msgs) > 2):
            for k in msgs:
                await channel.send("[WA] >> "+k)
                time.sleep(4)
            msgs = []
            system_call("del whatsappmessages.txt")
        else:
            print("might be spam .. ignoring")
    except FileNotFoundError:
        print("404 no wa messages file so ignorein")

    if(str(after.status) == "online" and str(before.status) == "offline"): 
        for _ in client.get_all_channels():
                if("bot" in _.name and not ("pacchu" in after.name)):
                    await _.send( random.choice(rep_pkg["convos"]["person_online"])  + spc + after.mention)





@client.event
async def on_message(message):
    #important Transfer variables
    global flag,filesend


    to_reply = important_functions(message)


    #handle conversion after important duties

    if(to_reply == None):
        to_reply = single_starter_replies(message)


    try:
        if(to_reply != None):
            await message.channel.send(to_reply)
            if(filesend != None):
                await message.channel.send(file=discord.File(filesend))
                filesend = None
            return
    except:
        await message.channel.send("Something somewhere somehow went wrong" +spc + random.choice(rep_pkg["emojicons"]["sed"]) +"\n" + str(to_reply)) 
    


def important_functions(message):
    if(message.content.startswith("!upload")):
        nameOfFile = str(message.content)[8:]
        print(nameOfFile)
        #files = os.listdir('./music/')
        files = os.listdir('.')
        print(files)
        print((nameOfFile in list(files)))
        for name in files:
            print(str(name))
            if(nameOfFile in str(name)):
                print(name)
                filesend = name
                return "Uploading {}".format(str(name)) + spc + random.choice(rep_pkg["emojicons"]["broken"])
        return "404 whoopsie" + spc + random.choice(rep_pkg["emojicons"]["broken"])





def single_starter_replies(message):
    global flag,cv19,ispaused,filesend
    if(message.channel == client.get_channel(709419678723866635)):
        return None
    if(message.content.startswith("!cmd")):
        return "Pacchu has said not to use this complex shit anymore so.. yeah im sorry kids :D"
    #Replies handler

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["covidcases"])) and flag):
        loc_data = cv19.getLocationByCountryCode('In')[0]
        vir = dict(loc_data['latest'])
        return "Total Active Cases {} .. and deaths are {}".format(vir['confirmed'],vir['deaths']) + spc + random.choice(rep_pkg["emojicons"]["sed"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["bot_instance"])) and flag):
        ispaused = True
        return random.choice(rep_pkg["convos"]["calling"])+spc +  message.author.mention + spc + random.choice(rep_pkg["emojicons"]["adoring"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["emojitrigger"])) and flag):
        ispaused = True
        return random.choice(rep_pkg["convos"]["Cantuseemoji"]) + spc + random.choice(rep_pkg["emojicons"]["fakku"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["stopreal"])) and flag):
        return random.choice(rep_pkg["convos"]["pausing"])+spc +  message.author.mention  + spc + random.choice(rep_pkg["emojicons"]["sed"])
    
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["simp"])) and flag):
        return random.choice(rep_pkg["convos"]["simpreply"])+spc +  message.author.mention  + spc + random.choice(rep_pkg["emojicons"]["fakku"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["reallove"])) and flag):
        return random.choice(rep_pkg["convos"]["breaking4wall"]) + spc + random.choice(rep_pkg["emojicons"]["adoring"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["reallove"])) and flag):
        return random.choice(rep_pkg["convos"]["breaking4wall"]) + spc + random.choice(rep_pkg["emojicons"]["adoring"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["botstupidity"])) and flag):
        return random.choice(rep_pkg["convos"]["scolding_reply"]) + spc + random.choice(rep_pkg["emojicons"]["scolding"])

    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["praise"])) and flag):
        return random.choice(rep_pkg["convos"]["praise_reply"]) + spc + random.choice(rep_pkg["emojicons"]["adoring"])

    elif(message.content.startswith("!python")):
        pyscript = "python3 -c '" + str(message.content)[7:] + "'"
        shell_out = system_call(pyscript)
        print(shell_out)
        try:
            scriptout = str(shell_out[0].decode())
            print(scriptout)
        except:
            scriptout = "Something Failed"+spc + random.choice(rep_pkg["emojicons"]["broken"]) + "\n" + str(shell_out[1])
        return scriptout
    elif(randomizer(10)):
        return random.choice(rep_pkg["convos"]["jokes"])
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["nice_trig"])) and len(message.content) < 10 and randomizer(3)):
        return random.choice(rep_pkg["triggers"]["nice_trig"]) + spc + random.choice(rep_pkg["emojicons"]["smirk"])
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["nums"])) and len(message.content) < 7 and randomizer(4)):
        return random.choice(rep_pkg["convos"]["numreply"]) + spc + random.choice(rep_pkg["emojicons"]["smirk"])
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["oof"])) and len(message.content) < 7):
        return random.choice(rep_pkg["triggers"]["oof"]) + spc + random.choice(rep_pkg["emojicons"]["smirk"])
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["boomer"])) and randomizer(3)):
        return "https://www.youtube.com/watch?v=9-3hvEkJsm0" #fuck it
    elif((any(msg in message.content.lower() for msg in rep_pkg["triggers"]["savemsg"])) and randomizer(3)):
        return random.choice(rep_pkg["triggers"]["savemsg"])
    if(message.content.lower().startswith('um'),message.content.lower().startswith('ok'),message.content.lower().startswith('omfg')):
        flag = True
    else:
        flag = False

def randomizer(prob):
    if(random.randint(1,prob) == 1):
        return True
    else:
        return False

client.run(botid)