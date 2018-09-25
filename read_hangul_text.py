import re
import asyncio
import datetime
import sys
import os
import codecs
import modify_sentence


class sub2aiml_sequence:


    @staticmethod
    def sub2aiml(sub_file,target_file,saved_file):

        count = 0

        file = codecs.open(
            sub_file, 'r', 'utf-8')
        empty_line_count = 0

        for text_line in file:

            if count < 97:
                pass
            else:
                    parse = re.sub('[-=.#/?:$}<>A-Za-z&;\'"]',
                                   '',
                                   text_line)

                    parse = re.sub(r"[0-9]\d{5,7}",
                                   '',
                                   parse)

                    #parse = parse.rstrip("\n")
                    parse = parse.replace("\n", "")

                    if parse == "":
                        pass
                    elif parse[0] == " " and parse[1] == " " and len(parse) == 3 and empty_line_count == 0:
                        
                        empty_line_count = empty_line_count+1
                    
                    elif parse[0] == " " and parse[1] == " " and len(parse) == 3 and empty_line_count == 1:

                        file = codecs.open(
                            target_file, 'a', 'utf-8')
                        file.write("enter\n")
                        file.close()
                        
                        empty_line_count = 0
                        
                        #print("enter")
                    
                    else:
                        
                        #print(parse)
                        
                        file = codecs.open(
                            target_file, 'a', 'utf-8')
                        
                        file.write(str(parse))

                        file.close()

            count = count + 1


        file.close()


        file = codecs.open(target_file,
                           'r', 'utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환

        question = ""
        answer = ""
        sub_question = ""
        sub_answer = ""
        sub_loop = 0
        line_option = 0
        write_enable = 1

        for sub_script_line in file:

                #print("sub_script_line ",sub_script_line)

                if sub_script_line == "enter\n":
                    line_option = not line_option
                    write_enable = 0

                #print("line_option ",line_option)
                #print("write_enable ",write_enable)

                if line_option == 0 and write_enable == 1:
                    
                    sub_question = sub_script_line.rstrip("\n")
                    sub_question = sub_script_line.rstrip("\r")

                    modify = modify_sentence.change_sentence()

                    question = question + str(modify.change_sentence_def(sub_question)) + " "

                    #question = " ".join([question,str(modify.change_sentence_def(sub_question))])

                    #print("sub_question ",sub_question)

                    #print("modify.change_sentence_def(sub_question) ",modify.change_sentence_def(sub_question))

                    print("question ",question)
                elif line_option == 1 and write_enable == 1:
                
                    sub_answer = sub_script_line.rstrip("\n")
                    sub_answer = sub_script_line.rstrip("\r")
                
                    answer = answer + str(sub_answer) + " "

                    #print("sub_answer ",sub_answer)

                    print("answer ",answer)
                else:
                    pass

                
               

                if write_enable == 0:

                    if question and answer:

                        #print("is this running? question ",question)
                        #print("is this running? answer ",answer)

                        if saved_file == 1:
                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer_drama.aiml', 'r', 'utf-8')

                            sub_Answer_Sentence_line = file.read()

                            sub_Answer_Sentence_line = sub_Answer_Sentence_line.replace(
                                '</aiml>', '')

                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer_drama.aiml', 'w', 'utf-8')
                            file.write(sub_Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer_drama.aiml', 'a', 'utf-8')
                            file.write("\n<category>\n")      # 파일에 문자열 저장
                            file.write("      <pattern>\n")
                            file.write("            "+question+"\n")
                            file.write("      </pattern>\n")
                            file.write("            <template>\n")
                            file.write("            "+answer+"\n")
                            file.write("            </template>\n")
                            file.write("</category>\n\n")
                            file.write("</aiml>\n")
                            file.close()

                            question = ""
                            answer = ""
                        else:
                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer.aiml', 'r', 'utf-8')
                        
                            sub_Answer_Sentence_line = file.read()

                            sub_Answer_Sentence_line = sub_Answer_Sentence_line.replace(
                                '</aiml>', '')

                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer.aiml', 'w', 'utf-8')
                            file.write(sub_Answer_Sentence_line)
                            file.close()

                            file = codecs.open(
                                './AIML_BOT/standard/sub_script_answer.aiml', 'a', 'utf-8')
                            file.write("\n<category>\n")      # 파일에 문자열 저장
                            file.write("      <pattern>\n")
                            file.write("            "+question+"\n")
                            file.write("      </pattern>\n")
                            file.write("            <template>\n")
                            file.write("            "+answer+"\n")
                            file.write("            </template>\n")
                            file.write("</category>\n\n")
                            file.write("</aiml>\n")
                            file.close()

                            question = ""
                            answer = ""

                    
                
                write_enable = 1

        file.close()                     # 파일 객체 닫기
