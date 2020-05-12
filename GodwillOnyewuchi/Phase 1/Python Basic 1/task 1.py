pattern = [0, 1, 2,2, 0, 1]
text = ['Twinkle, Twinkle little star', 'How i wonder how you are!', 'Up above the world so high', 'Like a diamond in the sky',
        'Twinkle, Twinkle little star', 'How i wonder how you are!']
for i in pattern:
    spacing = " " * 5;
    show = (pattern[i] * spacing) + text[i]
    print(show)


