#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import time
import sys
import time

def welcome():
    # user_name = input("who are you:")
    user_name = 'sunny'
    print('\n\
            Baacc   ..aaaxx   xxacc..aaaaaaaaaaa..  aaa..           ooaaaaaaaB       ooaaaaaabb..     aaaaa     Baaaab  ooaaaaaaaaaaa..\n\
            Baacc   ..aaaxx   xxacc..aaaaaaaaaaa..  aaa..           ooaaaaaaaB       ooaaaaaabb..     aaaaa     Baaaab  ooaaaaaaaaaaa..\n\
            .aaaa   BBaaabb   bbaoo..aaabbbbbbba..  aaa..          Baaaabbbaaacc   ooaaaaaccaaaaa.    aaaaax    aaaaab  ooaaabbbaabba..\n\
             aaaa   aaaaaaa   aaa  ooabb            aaaoo          aaa..   ..aaa   aaaaB     BBaaa    aaaaac    aaaaab  ooabb\n\
             aaaao  aabccaa.  aaa  ooabb            aaa..        xxabb       .    oaaaa        aaa..  abbaaa  ooaccaab  ooabb\n\
             aaaao  aabccaa.  aaa  ooabb            aaa..        xxabb       .    oaaaa        aaa..  abbaaa  ooaccaab  ooabb\n\
             BBaaBooaaBxxaaxooaac  ooaaaaaaaaaaa    aaaoo        ccaBB            xaabb        bbaoo  abbBBa  BBaxxaab  ooaaaaaaaaaaa\n\
             ooaacBBaao  aacBBaax  ooaaaccbbbbbc    aaa..        ccaBB            xaacc        bbaxx  aaaooaxxaaa..aab  ooaaaccbbbbbc\n\
               aaaaaaa   aaabbaa   ooabb            aaa..        BBacc       B..  oaaaa        aaa..  aaa  abbaab  aab  ooabb\n\
               aaaaabb   ccaaaaa   ooabb            aaa..        ..aaa     ..aaa   aaaao     xxaaa    aaa  aaaaax..aab  ooabb\n\
               aaaaabb   ccaaaaa   ooabb            aaa..        ..aaa     ..aaa   aaaao     xxaaa    aaa  aaaaax..aab  ooabb\n\
               ccaaaBB   ooaaacc   ooaaaccccccccoo  aaacccccccc..  caaaaBBBaaacc   xxaaaccBBbaaaax    aaa  caaaa...aab  ooaaaccccccccoo\n\
               ooaaa..     aaaxx   ooaaaaaaaaaaaBB  aaaaaaaaaaaxx   ccaaaaaaac       xxaaaaaaaaoo     aaa  oaaaa ..aab  ooaaaaaaaaaaaBB\n\
\
')
    time.sleep(2)
    for i in range(100):
        sys.stdout.write("\rloading...{0}>{1}% {2}".format("." * i, i + 1, user_name))
        sys.stdout.flush()
        time.sleep(0.1)

    return user_name


# if __name__ == '__main__':
#     welcome()