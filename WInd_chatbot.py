#!/usr/bin/python3
import aiml
import discord , asyncio , datetime , sys , os
from discord.ext import commands

client = discord.Client()

def main():
    client = discord.Client()


BRAIN_FILE="./AIML_BOT/brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./AIML_BOT/std-startup.xml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))

@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("453230551554457611")
    await client.send_message(channel, fmt.format(member, member.server))
    await client.send_message(member, "방갑습니다. 커뮤니티에 오신것을 한영합니다.")
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("453230551554457611")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))


@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('&'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        Client_sentence = str(message.content)
        Client_sentence_Count = len(Client_sentence)-1

        second_third_aspect = ["난","넌"," 난 "," 넌 ","내"," 내 "]
        for i in second_third_aspect:
            print(i)
            
            if i == "난" and Client_sentence[:len("&난")] == "&난":
                Client_sentence = Client_sentence.replace(i,'&나 는')
            
            if i == "넌" and Client_sentence[:len("&넌")] == "&넌":
                Client_sentence = Client_sentence.replace(i,'&너 는')
            
            if i == "내" and Client_sentence[:len("&내")] == "&내":
                Client_sentence = Client_sentence.replace(i,'&나의')

            if i == " 난 ":
                Client_sentence = Client_sentence.replace(i,' 나 는 ')
            
            if i == " 넌 ":
                Client_sentence = Client_sentence.replace(i,' 너 는 ')
            
            if i == " 내 ":
                Client_sentence = Client_sentence.replace(i,' 나의 ')

            print(Client_sentence)



        josa = ["은 ","는 ","이 ","가 ","을 ","를 ","야 "]
        for i in josa:
            print(i)
            Client_sentence = Client_sentence.replace(i,' '+i)
            print(Client_sentence)

#        finish_word = ["야"]
#        for i in finish_word:
#            if Client_sentence[Client_sentence_Count] == finish_word:
#                 print(i)
#                 Client_sentence = Client_sentence.replace(i,' '+i)
#                 print(Client_sentence)
#
#미래에 종사로 끝나느 경우가 추가되면 사용.

        finish_word = ["야","야?","?"]
        for i in finish_word:
            if i == "야?" and Client_sentence[len(Client_sentence)-len("야?"):] == "야?":
                print(i)
                Client_sentence = Client_sentence.replace(i,' 야?')
                print(Client_sentence)

            if i == "야" and Client_sentence[len(Client_sentence)-len("야"):] == "야":
                print(i)
                Client_sentence = Client_sentence.replace(i,' 야')
                print(Client_sentence)

            if i == "?" and Client_sentence[len(Client_sentence)-len("?"):] == "?":
                print(i)
                Client_sentence = Client_sentence.replace(i,'')
                print(Client_sentence)

        #k.setPredicate("user_name","<@"+id+">", id) 말하는 사람의 ID를 읽어서 봇에게 저장 
        k.setPredicate("bot_name","Wind",id)
        k.setPredicate("bot_sex","남자",id)
        k.setPredicate("bot_father","커뮤니티 리더 Wind",id)
        k.setPredicate("bot_mother","똥냥이",id)
        k.setPredicate("bot_hobby","살사댄스",id)
        k.setPredicate("bot_language","한국어",id)

        print(Client_sentence[0])

        if Client_sentence[0] == "&":
             Client_sentence = Client_sentence.replace("&","")
             Client_sentence = Client_sentence.lstrip()
            
             print(Client_sentence)

        await client.send_message(channel, k.respond(Client_sentence, id)) #봇은 해당 채널에 '커맨드' 라고 말합니다.
    elif message.content.startswith('!종료'):
            await client.send_message(message.channel, '종료합니다.')
            client.close()

async def my_background_task():
        time = 0
        await client.wait_until_ready()
        channel = discord.Object(id='453230551554457611')
        
        while not client.is_closed:
            timemeassage = "Wind BOT이 활동한지 {}시간이 지났습니다.".format(time)
            await client.send_message(channel, timemeassage)
            await asyncio.sleep(60*60*24) 
            time += 1
            
try:
    
    client.loop.create_task(my_background_task()) 

except Exception as e:
    print("오류 발생으로 BOT을 종료하고 빠져 나옵니다.") 
    client.close()

try:
    client.run('')
  

except Exception as e:
    print("오류 발생으로 BOT을 종료하고 빠져 나옵니다.") 
    client.close()


#대기 시간 초과로 봇이 종료되었을 때 자동으로 재실행을 위함
#import sys, os
#executable = sys.executable
#args = sys.argv[:]
#args.insert(0, sys.executable)
#print("Respawning")
#os.execvp(executable, args)

#if __name__ == '__main__':
#    main()
