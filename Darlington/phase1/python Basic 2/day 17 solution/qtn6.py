# program to print a long text, convert the string to a list and print all the words and their frequencies.
string_words = '''There has been much speculation about the origins of the Igbo people, as it is unknown how exactly the group came to form.[12] Geographically, the Igbo homeland is divided into two unequal sections by the Niger River – an eastern (which is the larger of the two) and a western section.[13][14] The Igbo people are one of the largest ethnic groups in Africa.[15]

The Igbo language is a part of the Niger-Congo language family. It is divided into numerous regional dialects, and somewhat mutually intelligible with the larger "Igboid" cluster.[16] The Igbo homeland straddles the lower Niger River, east and south of the Edoid and Idomoid groups, and west of the Ibibioid (Cross River) cluster.

In rural Nigeria, Igbo people work mostly as craftsmen, farmers and traders. The most important crop is the yam.[17] Other staple crops include cassava and taro.[18]

Before British colonial rule in the 20th century, the Igbo were a politically fragmented group, with a number of centralized chiefdoms such as Nri, Aro Confederacy, Agbor and Onitsha.[19] Frederick Lugard introduced the Eze system of "Warrant Chiefs".[20] Unaffected by the Fulani War and the resulting spread of Islam in Nigeria in the 19th century, they became overwhelmingly Christian under colonization. In the wake of decolonisation, the Igbo developed a strong sense of ethnic identity.[18] During the Nigerian Civil War of 1967–1970 the Igbo territories seceded as the short-lived Republic of Biafra.[21] MASSOB, a sectarian organization formed in 1999, continues a non-violent struggle for an independent Igbo state.[22]

Large ethnic Igbo populations are found in Cameroon[23] Gabon and Equatorial Guinea,[24] as well as outside Africa.'''

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))