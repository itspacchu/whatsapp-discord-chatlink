import sys , os , discord , subprocess , json , io , random , COVID19Py ,time ,numpy,glob


f = io.open("call.json", mode="r", encoding="utf-8")
rep_pkg = json.load(f)
spc = " "
flag = False
secondary_flag = False
cv19 = COVID19Py.COVID19()
ispaused = False
randkeygen = random.randint(00000000,99999999)
termination_check = False
main_hashkeyfunction = 1337
attempt = 0
terminated_mode = False
filesend = None
wished_users_list = []

def system_call(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return (output,err)

client = discord.Client()

@client.event
async def on_ready():
    print("Bot's Up and runnin bois")
    activity = discord.Game(name="Helping Pacchu Fail")
    await client.change_presence(status=discord.Status.online, activity=activity)


#on message calling function

#for ... in get_all_members()
@client.event
async def on_member_update(before, after):
    global flag,wished_users_list
    if(str(after.status) == "online" and str(before.status) == "offline"): 
        for _ in client.get_all_channels():
                if("bot" in _.name and not ("pacchu" in after.name)):
                    await _.send( random.choice(rep_pkg["convos"]["person_online"])  + spc + after.mention)


            
@client.event
async def on_message(message):
    global flag,secondary_flag,ispaused,randkeygen,attempt,termination_check,terminated_mode,filesend,wished_users_list
    if(ispaused):
        time.sleep(120)
        ispaused = False
    if message.author == client.user:
        flag = True
        return
    
    if(message.content.startswith("!absolute_termination")):
        termination_check = True
        await message.channel.send("Initiating Absolute Termination override\nEnter the corresponding key for {}".format(randkeygen))
    
    if(termination_check and (attempt < 5) and (not terminated_mode)):
        if(int(message.content) == int(randkeygen/main_hashkeyfunction + randkeygen*main_hashkeyfunction)):
            await message.channel.send("Hash key matched\nTerminating ...")
        else:
            randkeygen = random.randint(00000000,99999999)
            await message.channel.send("Incorrect hash key ...  try with a new hashkey : {} \n Attempt : {}/4".format(randkeygen,attempt))
            attempt+= 1
        attempt = 0
        termination_check = False

    if(not terminated_mode):
        to_reply = single_starter_replies(message)
    else:
        to_reply = None

    if(message.content == "!absolute_start" and terminated_mode):
        attempt = 0
        terminated_mode = False
        termination_check = True
        await message.channel.send(random.choice(rep_pkg["convos"]["reanimated"]))


    try:
        if(to_reply != None):
            await message.channel.send(to_reply)
            if(filesend != None):
                await message.channel.send(file=discord.File(filesend))
                filesend = None
            return
    except:
        await message.channel.send("Something somewhere somehow went wrong" +spc + random.choice(rep_pkg["emojicons"]["sed"]) +"\n" + str(to_reply)) 
    



def single_starter_replies(message):
    global flag,cv19,ispaused,filesend
    if(message.content.startswith("!cmd")):
        print("waiting for command")
        if(len(message.content.lower()) > 4):
            givencommand = str(message.content)[5:]
            print(givencommand)
            if(  (any(msg in givencommand for msg in rep_pkg["prohibited_commands"]) )):
                return "pls" +spc+ random.choice(rep_pkg["convos"]["rejection"]) + spc + random.choice(rep_pkg["emojicons"]["broken"])
            try:
                toshow = system_call(givencommand)[0].decode()
                return  x+(str(toshow)[:1800] )
            except:
                try:
                    return system_call(script)
                except:
                    return "what did u send tho...? wut?? \n >> {}".format(givencommand)
    
    elif(message.content.startswith("!upload")):
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

    elif(message.content.startswith("!remove")):
        nameOfFile = str(message.content)[8:]
        print(nameOfFile)
        files = os.listdir('.')
        print(files)
        print((nameOfFile in list(files)))
        for name in files:
            print(str(name))
            if(nameOfFile in str(name) and (name != "discord_test.py") and (name != "call.json")):
                print(name)
                system_call("rm {}".format(name))
                return "Found file ... Removing"
        return "404 whoopsie" + spc + random.choice(rep_pkg["emojicons"]["broken"])


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





client.run("NzA2MzkyOTc1NTI1MTUwNzgw.Xq5mSw.Xi8nkVTTIT4QpNCa0wv2GW4OwiU")