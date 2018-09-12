
import asyncio
import datetime
import sys
import os

class change_sentence:

    @staticmethod   
    def change_sentence_def(sub_target_sentence):   
        second_third_aspect = ["난","넌"," 난 "," 넌 ","내"," 내 ","색깔","네 "," 네 ","<",">"]
        for i in second_third_aspect:
            #print(i)
            
            if i == "난" and sub_target_sentence[:len("난")] == "난":
                sub_target_sentence = sub_target_sentence.replace(i,'나는')
            
            if i == "넌" and sub_target_sentence[:len("넌")] == "넌":
                sub_target_sentence = sub_target_sentence.replace(i,'너는')
            
            if i == "내" and sub_target_sentence[:len("내")] == "내":
                sub_target_sentence = sub_target_sentence.replace(i,'나의')
            
            if i == "네" and sub_target_sentence[:len("네")] == "네":
                sub_target_sentence = sub_target_sentence.replace(i,'너의')

            if i == " 난 ":
                sub_target_sentence = sub_target_sentence.replace(i,' 나는 ')
            
            if i == " 넌 ":
                sub_target_sentence = sub_target_sentence.replace(i,' 너는 ')
            
            if i == " 내 ":
                sub_target_sentence = sub_target_sentence.replace(i,' 나의 ')
            
            if i == " 네 ":
                sub_target_sentence = sub_target_sentence.replace(i,' 너의 ')

            if sub_target_sentence.find(i) and i == "색깔":
                sub_target_sentence = sub_target_sentence.replace(i,'색')

            if sub_target_sentence.find(i) and i == "<":
                sub_target_sentence = sub_target_sentence.replace(i,'left_arrow')

            if sub_target_sentence.find(i) and i == ">":
                sub_target_sentence = sub_target_sentence.replace(i,'right_arrow')

            #print(sub_target_sentence)


        josa = ["은 ","는 ","이 ","가 ","을 ","를 ","야 ","의 ","이야?","이야"]
        for i in josa:
            #print(i)

            sub_target_sentence = sub_target_sentence.replace(i," * ")
            #print(sub_target_sentence)

        finish_word = ["야","야?","?","니?","니","지","지?"]
        for i in finish_word:
            if i == "야?" and sub_target_sentence[len(sub_target_sentence)-len("야?"):] == "야?":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)

            if i == "야" and sub_target_sentence[len(sub_target_sentence)-len("야"):] == "야":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)

            if i == "?" and sub_target_sentence[len(sub_target_sentence)-len("?"):] == "?":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,'')
                #print(sub_target_sentence)

            if i == "니?" and sub_target_sentence[len(sub_target_sentence)-len("니?"):] == "니?":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)

            if i == "니" and sub_target_sentence[len(sub_target_sentence)-len("니"):] == "니":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)
            
            if i == "지?" and sub_target_sentence[len(sub_target_sentence)-len("지?"):] == "지?":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)

            if i == "지" and sub_target_sentence[len(sub_target_sentence)-len("지"):] == "지":
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' *')
                #print(sub_target_sentence)



        sub_target_sentence = sub_target_sentence.lstrip()
            
             #print(sub_target_sentence)

        sub_target_sentence = sub_target_sentence.upper() 

        adjust_word = [" 나 이 "," 몇살 "]
        for i in adjust_word:
            if i == " 나 이 " and sub_target_sentence.find(" 나 이 "):
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' 나이 ')
                #print(sub_target_sentence)

            if i == " 몇살 " and sub_target_sentence.find(" 몇살 "):
                #print(i)
                sub_target_sentence = sub_target_sentence.replace(i,' 몇 살 ')
                #print(sub_target_sentence)


        return sub_target_sentence