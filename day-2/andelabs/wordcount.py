def words(n):

    word_list = n.replace('\t', ' ').split()
    jafi = {}

    for w in list(word_list):
      try:

        theWord = int(w)

      except ValueError:

        jafi[w] = word_list.count(w)

      else:

       jafi[int(w)] = word_list.count(w)
    return jafi
