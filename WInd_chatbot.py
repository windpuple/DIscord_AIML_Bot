#!/usr/bin/python3
import aiml
import discord , asyncio , datetime , sys , os
from discord.ext import commands
import codecs

client = discord.Client()

def main():
    client = discord.Client()


BRAIN_FILE="./AIML_BOT/brain.dump"

k = aiml.Kernel()

Learn_flag = 0
Sentence_Num = 0


# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.

#if os.path.exists(BRAIN_FILE):
#    print("Loading from brain file: " + BRAIN_FILE)
#    k.loadBrain(BRAIN_FILE)
#else:
#    print("Parsing aiml files")
#    k.bootstrap(learnFiles="./AIML_BOT/std-startup.xml", commands="load aiml b")
#    print("Saving brain file: " + BRAIN_FILE)
#    k.saveBrain(BRAIN_FILE)

#imsi dont use brain file
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
    channel = member.server.get_channel("481774355085524994")
    await client.send_message(channel, fmt.format(member, member.server))
    await client.send_message(member, "방갑습니다. 커뮤니티에 오신것을 한영합니다.")
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("481774355085524994")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))


@client.event
async def on_message(message):

    global Learn_flag
    global Sentence_Num
    global target_Num
    

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



        josa = ["은 ","는 ","이 ","가 ","을 ","를 ","야 ","의 ","이야?"]
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

 

        k.setPredicate("user_name","<@"+id+">", id) # 말하는 사람의 ID를 읽어서 봇에게 저장 
        k.setPredicate("bot_name","Wind",id)
        k.setPredicate("bot_sex","남자",id)
        k.setPredicate("bot_father","커뮤니티 리더 Wind",id)
        k.setPredicate("bot_mother","똥냥이",id)
        k.setPredicate("bot_hobby","살사댄스",id)
        k.setPredicate("bot_language","한국어",id)
        k.setPredicate("bot_age","21",id)
        

        print(Client_sentence[0])

        if Client_sentence[0] == "&":
             Client_sentence = Client_sentence.replace("&","")
             Client_sentence = Client_sentence.lstrip()
            
             print(Client_sentence)

      

        if(Learn_flag == 0):
            if k.respond(Client_sentence, id):
                await client.send_message(channel, k.respond(Client_sentence, id)) #봇은 해당 채널에 '커맨드' 라고 말합니다.
            else:
                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'a','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                file.write(str(Sentence_Num)+" "+k.getPredicate("user_name",id)+" "+Client_sentence+"\n")      # 파일에 문자열 저장
                file.close()                     # 파일 객체 닫기
                await client.send_message(channel, "아직은 이해 할수 없는 말입니다. 하지만 데이터베이스에 기록하여 지능의 성장에 쓰도록 하겠습니다.")
                await client.send_message(channel, "그러면 제가 대답을 어떻게 해야 하는지 알려주세요.")

                target_Num = Sentence_Num
                Sentence_Num = Sentence_Num+1
                Learn_flag = 1

        elif(Learn_flag == 1):
                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'r','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                loop = 0
                for MisUnderstand_Sentence_line in file:

                    #MisUnderstand_Sentence_line = row.readline()
                
                    print(MisUnderstand_Sentence_line)

                    
                    readline_split = MisUnderstand_Sentence_line.split()

                        
                    print("loop ",loop)
                    print("Sentence_Num ",str(target_Num))
                    print("readline_split0 ",readline_split[0])
                        
                    if readline_split[0] == str(target_Num):
                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'r','utf-8')
                            Answer_Sentence_line = file.read()
                            print("aiml erase1 ",Answer_Sentence_line)
                            Answer_Sentence_line = Answer_Sentence_line.replace('</aiml>', '')
                            print("aiml erase2 ",Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'w', 'utf-8')
                            file.write(Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'a', 'utf-8')
                            file.write("\n<category>\n")      # 파일에 문자열 저장
                            file.write("      <pattern>\n")
                            file.write("            "+MisUnderstand_Sentence_line[24:])
                            file.write("      </pattern>\n")
                            file.write("            <template>\n")
                            file.write("            "+Client_sentence+"\n")
                            file.write("            </template>\n")
                            file.write("</category>\n\n")
                            file.write("</aiml>\n")
                            file.close()

                    loop = loop + 1
                
                file.close()                     # 파일 객체 닫기
                await client.send_message(channel, "기억했어요. 대답을 알려주셔서 감사합니다.")
                Learn_flag = 0
                
            




        
    elif message.content.startswith('!종료'):
            await client.send_message(message.channel, '종료합니다.')
            client.close()

async def my_background_task():
        time = 0
        await client.wait_until_ready()
        channel = discord.Object(id='481774355085524994')
        
        while not client.is_closed:
            timemeassage = "Wind BOT이 활동한지 {}시간이 지났습니다.".format(time)
            await client.send_message(channel, timemeassage)
            await asyncio.sleep(60*60) 
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
