def AutomaticYossarian(text):
    """
    All the officer patients in the ward were forced to censor letters written by all the enlisted-men patients,
    who were kept in residence in wards of their own. It was a monotonous job, and Yossarian was disappointed to
    learn that the lives of enlisted men were only slightly more interesting than the lives of officers. After the
    first day he had no curiosity at all. To break the monotony he invented games. Death to all modifiers, he
    declared one day, and out of every letter that passed through his hands went every adverb and every
    adjective. The next day he made war on articles. He reached a much higher plane of creativity the following
    day when he blacked out everything in the letters but a, an and the. That erected more dynamic intralinear
    tensions, he felt, and in just about every case left a message far more universal. Soon he was proscribing
    parts of salutations and signatures and leaving the text untouched. One time he blacked out all but
    salutation"Dear Mary" from a letter, and at the bottom he wrote, "I yearn for you tragically, A.T. Tappman,
    Chaplain, U.S. Army." A.T. Tappman was the group chaplain's name.
    """
    words = text.split(" ")
    if words[0] == "Dear" and (words[1] == "Mary" or words[1] == "Mary,"):
        return (
            " ".join(words[0:2])
            + " \n \n I yearn for you tragically. \n \n A.T. Tappman \n Chaplain, U.S. Army"
        )
    else:
        out = filter(lambda x: x in ("a", "an", "the"), words)
        return " ".join(out)



def ComputationalHermanMelville():
    """
    Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.
    """
    """
    EARLY DRAFT. NOT TESTED YET.
    """
    name = input("Hello. What is your name?")
    phone = input("And what is your phone number?")

    from twilio.rest import Client


    client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

    client.messages.create(to=phone, 
                       from_="+12023351278", 
                       body="Hello Ishmael") #etc.