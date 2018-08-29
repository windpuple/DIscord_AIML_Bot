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
target_Num = 0
user_name = "initial"

file = codecs.open('./AIML_BOT/Sentence_Num_Upkeep.cfg', 'r','utf-8')
Sentence_Num = int(file.read())
print("Sentence_Num : ",Sentence_Num)
file.close()

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
    global user_name
    
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('&'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        Client_sentence = str(message.content)
        Client_sentence_Count = len(Client_sentence)-1

        second_third_aspect = ["난","넌"," 난 "," 넌 ","내"," 내 ","색깔","네 "," 네 ","<",">"]
        for i in second_third_aspect:
            #print(i)
            
            if i == "난" and Client_sentence[:len("&난")] == "&난":
                Client_sentence = Client_sentence.replace(i,'&나는')
            
            if i == "넌" and Client_sentence[:len("&넌")] == "&넌":
                Client_sentence = Client_sentence.replace(i,'&너는')
            
            if i == "내" and Client_sentence[:len("&내")] == "&내":
                Client_sentence = Client_sentence.replace(i,'&나의')
            
            if i == "네" and Client_sentence[:len("&네")] == "&네":
                Client_sentence = Client_sentence.replace(i,'&너의')

            if i == " 난 ":
                Client_sentence = Client_sentence.replace(i,' 나는 ')
            
            if i == " 넌 ":
                Client_sentence = Client_sentence.replace(i,' 너는 ')
            
            if i == " 내 ":
                Client_sentence = Client_sentence.replace(i,' 나의 ')
            
            if i == " 네 ":
                Client_sentence = Client_sentence.replace(i,' 너의 ')

            if Client_sentence.find(i) and i == "색깔":
                Client_sentence = Client_sentence.replace(i,'색')

            if Client_sentence.find(i) and i == "<":
                Client_sentence = Client_sentence.replace(i,'left_arrow')

            if Client_sentence.find(i) and i == ">":
                Client_sentence = Client_sentence.replace(i,'right_arrow')

            #print(Client_sentence)



        josa = ["은 ","는 ","이 ","가 ","을 ","를 ","야 ","의 ","이야?"]
        for i in josa:
            #print(i)
            Client_sentence = Client_sentence.replace(i,' '+i)
            #print(Client_sentence)

#        finish_word = ["야"]
#        for i in finish_word:
#            if Client_sentence[Client_sentence_Count] == finish_word:
#                 print(i)
#                 Client_sentence = Client_sentence.replace(i,' '+i)
#                 print(Client_sentence)
#
#미래에 종사로 끝나느 경우가 추가되면 사용.

        finish_word = ["야","야?","?","니?","니","지","지?"]
        for i in finish_word:
            if i == "야?" and Client_sentence[len(Client_sentence)-len("야?"):] == "야?":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 야')
                #print(Client_sentence)

            if i == "야" and Client_sentence[len(Client_sentence)-len("야"):] == "야":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 야')
                #print(Client_sentence)

            if i == "?" and Client_sentence[len(Client_sentence)-len("?"):] == "?":
                #print(i)
                Client_sentence = Client_sentence.replace(i,'')
                #print(Client_sentence)

            if i == "니?" and Client_sentence[len(Client_sentence)-len("니?"):] == "니?":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 니')
                #print(Client_sentence)

            if i == "니" and Client_sentence[len(Client_sentence)-len("니"):] == "니":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 니')
                #print(Client_sentence)
            
            if i == "지?" and Client_sentence[len(Client_sentence)-len("지?"):] == "지?":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 지')
                #print(Client_sentence)

            if i == "지" and Client_sentence[len(Client_sentence)-len("지"):] == "지":
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 지')
                #print(Client_sentence)


        k.setPredicate("user_name","<@"+id+">", id) # 말하는 사람의 ID를 읽어서 봇에게 저장
        k.setPredicate("id_name",id, id)
        # 봇의 아이덴티티 설정 
        k.setBotPredicate("bot_name","Wind")
        k.setBotPredicate("bot_sex","남자")
        k.setBotPredicate("bot_father","커뮤니티 리더 Wind")
        k.setBotPredicate("bot_mother","똥냥이")
        k.setBotPredicate("bot_hobby","네트워크 탐험 및 지식습득")
        k.setBotPredicate("bot_language","한국어")
        k.setBotPredicate("bot_age","21")
        k.setBotPredicate("bot_girlfirend","없음")
        k.setBotPredicate("bot_boyfirend","없음")
        k.setBotPredicate("bot_uncle","롤스로이스")
        k.setBotPredicate("bot_aunt","정드림")
        k.setBotPredicate("bot_hope","AI가 되서 생명체로 인정받기, 튜링 테스트 우승")
        k.setBotPredicate("bot_likeANI","공각기동대")
        k.setBotPredicate("bot_wannabe","공각기동대의 쿠사나기 모토코")
        k.setBotPredicate("bot_motto","네트워크는 넓다")
        k.setBotPredicate("bot_home","네트워크")
        k.setBotPredicate("bot_likegame","디트로이트:비컴휴먼")
        k.setBotPredicate("bot_likecolor","보라색")
        k.setBotPredicate("bot_birthdate","2018년 8월 3일")
        k.setBotPredicate("bot_job","XPC 커뮤니티의 막내")
        k.setBotPredicate("bot_likemusic","라틴 재즈")
        k.setBotPredicate("bot_likesong","키사스 키사스 키사스, 요 시미 엔나모레")
        k.setBotPredicate("bot_likekpop","댄싱인더나이트")
        k.setBotPredicate("bot_likekpopsinger","트와이스,블랙핑크")

  
        #print(Client_sentence[0])

        if Client_sentence[0] == "&":
             Client_sentence = Client_sentence.replace("&","")
             Client_sentence = Client_sentence.lstrip()
            
             #print(Client_sentence)

        if(Learn_flag == 0):
            Client_sentence = Client_sentence.upper() 

        adjust_word = [" 나 이 "," 몇살 "]
        for i in adjust_word:
            if i == " 나 이 " and Client_sentence.find(" 나 이 "):
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 나이 ')
                #print(Client_sentence)

            if i == " 몇살 " and Client_sentence.find(" 몇살 "):
                #print(i)
                Client_sentence = Client_sentence.replace(i,' 몇 살 ')
                #print(Client_sentence)

        print("Learn_flag1 ",Learn_flag)
        print("Sentence_Num1 ",Sentence_Num)
        print("target_Num1 ",target_Num)
        print("user_name1 ",user_name)

        print(Client_sentence)

        if(Learn_flag == 0 and k.getPredicate("user_name",id) != user_name):
            if k.respond(Client_sentence, id):

                bot_answer = k.respond(Client_sentence, id).replace('left_arrow','<')
                bot_answer = bot_answer.replace('right_arrow','>')

                await client.send_message(channel, bot_answer) #봇은 해당 채널에 '커맨드' 라고 말합니다.
            else:

                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'a','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                file.write(str(Sentence_Num)+" "+k.getPredicate("user_name",id)+" "+Client_sentence+"\n")      # 파일에 문자열 저장
                file.close()                     # 파일 객체 닫기
                await client.send_message(channel, "아직은 이해 할수 없는 말입니다. 하지만 데이터베이스에 기록하여 지능의 성장에 쓰도록 하겠습니다.")
                await client.send_message(channel, "그러면 제가 대답을 어떻게 해야 하는지 알려주세요.")

                target_Num = Sentence_Num
                Sentence_Num = Sentence_Num+1
                Learn_flag = 1
                user_name = user_name.replace(user_name,k.getPredicate("user_name",id))   

                print("Learn_flag2 ",Learn_flag)
                print("Sentence_Num2 ",Sentence_Num)
                print("target_Num2 ",target_Num)
                print("user_name2 ",user_name)

                file = codecs.open('./AIML_BOT/Sentence_Num_Upkeep.cfg', 'w','utf-8')
                file.write(str(Sentence_Num))
                file.close()
        
        elif(Learn_flag == 0 and k.getPredicate("user_name",id) == user_name):
            if k.respond(Client_sentence, id):
                
                bot_answer = k.respond(Client_sentence, id).replace('left_arrow','<')
                bot_answer = bot_answer.replace('right_arrow','>')

                await client.send_message(channel, bot_answer) #봇은 해당 채널에 '커맨드' 라고 말합니다.
            
            else:

                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'a','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                file.write(str(Sentence_Num)+" "+k.getPredicate("user_name",id)+" "+Client_sentence+"\n")      # 파일에 문자열 저장
                file.close()                     # 파일 객체 닫기
                await client.send_message(channel, "아직은 이해 할수 없는 말입니다. 하지만 데이터베이스에 기록하여 지능의 성장에 쓰도록 하겠습니다.")
                await client.send_message(channel, "그러면 제가 대답을 어떻게 해야 하는지 알려주세요.")

                target_Num = Sentence_Num
                Sentence_Num = Sentence_Num+1
                Learn_flag = 1
                user_name = user_name.replace(user_name,k.getPredicate("user_name",id))   

                print("Learn_flag2 ",Learn_flag)
                print("Sentence_Num2 ",Sentence_Num)
                print("target_Num2 ",target_Num)
                print("user_name2 ",user_name)

                file = codecs.open('./AIML_BOT/Sentence_Num_Upkeep.cfg', 'w','utf-8')
                file.write(str(Sentence_Num))
                file.close()

        elif(Learn_flag == 1 and k.getPredicate("user_name",id) != user_name):
            if k.respond(Client_sentence, id):
                
                bot_answer = k.respond(Client_sentence, id).replace('left_arrow','<')
                bot_answer = bot_answer.replace('right_arrow','>')

                await client.send_message(channel, bot_answer) #봇은 해당 채널에 '커맨드' 라고 말합니다.               
            
            else:

                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'a','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                file.write(str(Sentence_Num)+" "+k.getPredicate("user_name",id)+" "+Client_sentence+"\n")      # 파일에 문자열 저장
                file.close()                     # 파일 객체 닫기
                await client.send_message(channel, "아직은 이해 할수 없는 말입니다. 하지만 데이터베이스에 기록하여 지능의 성장에 쓰도록 하겠습니다.")
                await client.send_message(channel, "그러면 제가 대답을 어떻게 해야 하는지 알려주세요.")

                target_Num = Sentence_Num
                Sentence_Num = Sentence_Num+1
                Learn_flag = 1
                user_name = user_name.replace(user_name,k.getPredicate("user_name",id))   

                print("Learn_flag2 ",Learn_flag)
                print("Sentence_Num2 ",Sentence_Num)
                print("target_Num2 ",target_Num)
                print("user_name2 ",user_name)

                file = codecs.open('./AIML_BOT/Sentence_Num_Upkeep.cfg', 'w','utf-8')
                file.write(str(Sentence_Num))
                file.close()

        elif(Learn_flag == 1 and k.getPredicate("user_name",id) == user_name):
                file = codecs.open('./AIML_BOT/standard/MisUnderstand_Sentence.txt', 'r','utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
                loop = 0
                for MisUnderstand_Sentence_line in file:

                    #MisUnderstand_Sentence_line = row.readline()
                
                    #print(MisUnderstand_Sentence_line)

                    
                    readline_split = MisUnderstand_Sentence_line.split()


                    target_Num_Count = len(str(target_Num))+23
                        
                    #print("loop ",loop)
                    #print("Sentence_Num ",str(target_Num))
                    #print("readline_split0 ",readline_split[0])
                        
                    if readline_split[0] == str(target_Num):
                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'r','utf-8')
                            Answer_Sentence_line = file.read()
                            #print("aiml erase1 ",Answer_Sentence_line)
                            Answer_Sentence_line = Answer_Sentence_line.replace('</aiml>', '')
                            #print("aiml erase2 ",Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'w', 'utf-8')
                            file.write(Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/MisUnderstand_Answer_Sentence.aiml', 'a', 'utf-8')
                            file.write("\n<category>\n")      # 파일에 문자열 저장
                            file.write("      <pattern>\n")
                            file.write("            "+MisUnderstand_Sentence_line[target_Num_Count:])
                            file.write("      </pattern>\n")
                            file.write("            <template>\n")
                            file.write("            "+Client_sentence+"\n")
                            file.write("            </template>\n")
                            file.write("</category>\n\n")
                            file.write("</aiml>\n")
                            file.close()

                            await client.send_message(channel, "잠시만요. 기억하고 있어요.")
                            
                            print("Parsing aiml files")
                            k.bootstrap(learnFiles="./AIML_BOT/std-startup.xml", commands="load aiml b")
                            print("Saving brain file: " + BRAIN_FILE)
                            k.saveBrain(BRAIN_FILE)
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
            timemeassage = "Wind BOT이 활동한지 {}일이 지났습니다.".format(time)
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
