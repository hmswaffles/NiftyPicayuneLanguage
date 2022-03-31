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
