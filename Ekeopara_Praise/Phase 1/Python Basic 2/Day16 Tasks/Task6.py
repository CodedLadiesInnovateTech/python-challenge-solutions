words = '''It is often said that we are learning all the time and that we may not be conscious of it happening. Learning is both a process and an outcome. As a process it is part of living in the world, part of the way our bodies work. As an outcome it is a new understanding or appreciation of something.
In recent years, developments in neuroscience have shown us how learning takes place both in the body and as a social activity. We are social animals. As a result educators need to focus on creating environments and relationships for learning rather than trying to drill knowledge into people.
Teachers are losing the education war because our adolescents are distracted by the social world. Naturally, the students don’t see it that way. It wasn’t their choice to get endless instruction on topics that don’t seem relevant to them. They desperately want to learn, but what they want to learn about is their social world—how it works and how they can secure a place in it that will maximize their social rewards and minimize the social pain they feel. Their brains are built to feel these strong social motivations and to use the mentalizing system to help them along. Evolutionarily, the social interest of adolescents is no distraction. Rather, it is the most important thing they can learn well. (Lieberman 2013: 282)
The cultivation of learning is a cognitive and emotional and social activity (Illeris 2002).
Intention
Education is deliberate. We act with a purpose – to develop understanding and judgement, and enable action. We may do this for ourselves, for example, learning what different road signs mean so that we can get a license to drive; or watching wildlife programmes on television because we are interested in animal behaviour. This process is sometimes called self-education or teaching yourself. Often, though, we seek to encourage learning in others. Examples here include parents and carers showing their children how to use a knife and fork or ride a bike; schoolteachers introducing students to a foreign language; and animators and pedagogues helping a group to work together.'''



word_list = words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))