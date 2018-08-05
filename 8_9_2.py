# -*- coding: utf-8 -*-

file1 = open('8_9_2.txt')
content = file1.read()
content_list = content.split()
for i in range(len(content_list)):
    if content_list[i] == "ADJECTIVE":
        adj = raw_input("Enter an adjective:")
        content_list[i] = adj
    if content_list[i] == "ADJECTIVE.":
        adj = raw_input("Enter an adjective:")
        content_list[i] = adj + '.'
    if content_list[i] == "NOUN":
        noun = raw_input("Enter a noun:")
        content_list[i] = noun
    if content_list[i] == "NOUN.":
        noun = raw_input("Enter a noun:")
        content_list[i] = noun + '.'
    if content_list[i] == "VERB":
        verb = raw_input("Enter an verb:")
        content_list[i] = verb
    if content_list[i] == "VERB.":
        verb = raw_input("Enter an verb:")
        content_list[i] = verb + '.'

new_content = ' '.join(content_list)
file2 = open('new_8_9_2.txt', 'w')
file2.write(new_content)
file1.close()
file2.close()

