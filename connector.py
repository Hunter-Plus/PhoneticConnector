import re

# Define
vowels = ['i', 'ɪ', 'ɛ', 'æ', 'ə', 'ʌ', 'u', 'ʊ', 'ɔ', 'ɑ']
consonants = ['p', 'b', 't', 'd', 'k', 'g', 'm', 'n', 'ŋ', 'f', 'v',
              'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʧ', 'ʤ', 'h', 'r', 'l', 'j', 'w']
stops_consonants = ['p', 'b', 't', 'd', 'k', 'g']
lips_consonants = ['b', 'p', 'm', 'f', 'v', 'w']
teeth_consonants = ['d', 't', 'n', 'l', 'z', 's', 'ʃ', 'ʒ', 'ʧ', 'ʤ', 'j']
throat_consonants = ['g', 'k', 'h', 'r', 'ŋ']


def apply_rules(word1, word2):
    firsr_word_tail = -2
    second_word_start = 1
    # Find the real indexes of 2 consective words' phonetic symbols
    if word1[firsr_word_tail] not in vowels and word1[firsr_word_tail] not in consonants:
        firsr_word_tail -= 1
    if word2[second_word_start] not in vowels and word2[second_word_start] not in consonants:
        second_word_start += 1
    # Rule 1: Connect words when the first ends with a consonant and the second starts with a vowel
    if word1[firsr_word_tail] in consonants and word2[second_word_start] in vowels:
        return word1[:firsr_word_tail + 1] + '-' + word2[second_word_start:]

    # Rule 2: Connect words when both end and start with consonants
    elif word1[firsr_word_tail] in consonants and word2[second_word_start] in consonants:
        # 2.1: Identical consecutive consonants
        if word1[firsr_word_tail] == word2[second_word_start]:
            return word1[:firsr_word_tail] + '(' + word2[second_word_start] + ')' + word2[second_word_start + 1:]
        # 2.2: Consecutive consonants are ð or θ
        elif word1[firsr_word_tail] in ['ð', 'θ'] or word2[second_word_start] in ['ð', 'θ']:
            return word1[:firsr_word_tail] + '(' + word1[firsr_word_tail] + word2[second_word_start] + ')' + word2[second_word_start + 1:]
        # 2.3: Consecutive consonants in same place in the mouth
        elif (word1[firsr_word_tail] in lips_consonants and word2[second_word_start] in lips_consonants) or (word1[firsr_word_tail] in teeth_consonants and word2[second_word_start] in teeth_consonants) or (word1[firsr_word_tail] in throat_consonants and word2[second_word_start] in throat_consonants):
            if word1[firsr_word_tail] in stops_consonants:
                return word1[:firsr_word_tail + 1] + '|' + word2[second_word_start:]
            return word1[:firsr_word_tail + 1] + '-' + word2[second_word_start:]
        # 2.4: Specific consonant pairs dtsz+ j
        elif word1[firsr_word_tail] == 't' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʧ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 'd' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʤ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 's' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʃ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 'z' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʒ)' + word2[second_word_start + 1:]

    # Rule 3: Connect words when the first ends with a specific vowel and the second starts with a vowel
    elif word1[firsr_word_tail] in vowels and word2[second_word_start] in vowels:
        # 3.1: First vowel is u or ʊ
        if word1[firsr_word_tail] in ['u', 'ʊ']:
            return word1[:firsr_word_tail + 1] + '-w-' + word2[second_word_start:]
        # 3.2: First vowel is i or ɪ
        elif word1[firsr_word_tail] in ['i', 'ɪ']:
            return word1[:firsr_word_tail + 1] + '-j-' + word2[second_word_start:]
    # No rule matched
    return word1


def main():
    # input_text = input("Enter the phonetic symbols: ")
    input_text = '''/ˈbɪznəsəz/ /həv/ /ˈɔlˌweɪz/ /sɔt/ /tə/ /meɪk/ /ə/ /ˈprɑfət/, /bət/ /ɪt/ /əz/ /bɪˈkʌmɪŋ/ /ɪnˈkrisɪŋli/ /ˈkɑmən/ /tə/ /hir/ /ˈpipəl/ /tɔk/ /əˈbaʊt/ /ðə/ /ˈsoʊʃəl/ /ˌɑbləˈɡeɪʃənz/ /ðət/ /ˈkʌmpəniz/ /hæv/. /aɪ/ /kəmˈplitli/ /əˈɡri/ /wɪð/ /ði/ /aɪˈdiə/ /ðət/ /ˈbɪznəsəz/ /ʃəd/ /dʊ/ /mɔr/ /fər/ /səˈsaɪəti/ /ðən/ /ˈsɪmpli/ /meɪk/ /ˈmʌni/.
/ɑn/ /ðə/ /wʌn/ /hænd/, /aɪ/ /ækˈsɛpt/ /ðət/ /ˈbɪznəsəz/ /məst/ /meɪk/ /ˈmʌni/ /ɪn/ /ˈɔrdər/ /tə/ /sərˈvaɪv/ /ɪn/ /ə/ /kəmˈpɛtətɪv/ /wɜrld/. /ɪt/ /simz/ /ˈlɑʤɪkəl/ /ðət/ /ðə/ /praɪˈɔrəti/ /əv/ /ˈɛni/ /ˈkʌmpəni/ /ʃəd/ /bi/ /tə/ /ˈkʌvər/ /ɪts/ /ˈrʌnɪŋ/ /kɑsts/, /sʌʧ/ /əz/ /ɛmˈplɔɪiz/ /ˈweɪʤəz/ /ənd/ /ˈpeɪmənts/ /fər/ /ˈbɪldɪŋz/ /ənd/ /juˈtɪlətiz/. /ɑn/ /tɑp/ /əv/ /ðiz/ /kɑsts/, /ˈkʌmpəniz/ /ˈɔlsoʊ/ /nid/ /tʊ/ /ɪnˈvɛst/ /ɪn/ /ɪmˈpruvmənts/ /ənd/ /ˌɪnəˈveɪʃənz/ /ɪf/ /ðeɪ/ /wɪʃ/ /tə/ /rɪˈmeɪn/ /səkˈsɛsfəl/. 
/ɪn/ /kənˈkluʒən/, /aɪ/ /bɪˈliv/ /ðət/ /ˈkʌmpəniz/ /ʃəd/ /pleɪs/ /əz/ /mʌʧ/ /ɪmˈpɔrtəns/ /ɑn/ /ðɛr/ /ˈsoʊʃəl/ /riˌspɑnsəˈbɪlətiz/ /əz/ /ðeɪ/ /dʊ/ /ɑn/ /ðɛr/ /fəˈnænʃəl/ /əbˈʤɛktɪvz/.
'''
    if "\n\n" in input_text:
        print("it has !")

    paragraphs = input_text.split('\n\n')  # Split input into paragraphs
    print(len(paragraphs))
    for paragraph in paragraphs:
        # Split paragraph into sentences
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        for sentence in sentences:
            connected_sentence = ""
            words_and_punctuations = sentence.split()
            i = 0
            while i < len(words_and_punctuations):
                current_word_or_punctuation = words_and_punctuations[i]
                if current_word_or_punctuation.endswith('/'):
                    for j in range(i+1, len(words_and_punctuations)):
                        i = j - 1
                        if words_and_punctuations[j].endswith('/'):
                            # Try to make a connection.
                            connected_word = apply_rules(
                                current_word_or_punctuation, words_and_punctuations[j])
                            if connected_word != current_word_or_punctuation:  # Two words are connected
                                current_word_or_punctuation = connected_word
                            else:
                                break
                connected_sentence += current_word_or_punctuation + ' '

                i += 1
            # connected_sentence += '.'
            print(connected_sentence.strip())
        print()  # Empty line between paragraphs


if __name__ == "__main__":
    main()
