import re

# Define
vowels = ['i', 'ɪ', 'ɛ', 'æ', 'ə', 'ʌ', 'u', 'ʊ', 'ɔ', 'ɑ', 'e', 'a', 'o', 'ɝ', 'ɚ'] # Also include the first symbol of all the dipthongs and r-colored vowels
# e for eɪ, a for aɪ and aʊ, o for oʊ
consonants = ['p', 'b', 't', 'd', 'k', 'g', 'ɡ', 'm', 'n', 'ŋ', 'f', 'v',
              'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʧ', 'ʤ', 'h', 'r', 'l', 'j', 'w']
stops_consonants = ['p', 'b', 't', 'd', 'k', 'g', 'ɡ']
lips_consonants = ['b', 'p', 'm', 'f', 'v', 'w']
teeth_consonants = ['d', 't', 'n', 'l', 'z', 's', 'ʃ', 'ʒ', 'ʧ', 'ʤ', 'j']
throat_consonants = ['g', 'ɡ', 'k', 'h', 'r', 'ŋ']
punctuations = [",", ";", ":", "—", '"', "'", "“", "”", "(", ")", "[", "]", ".", "?", "!", "…"]
left_blank_punctuations = ["“", "(", "["] # " is special, process it in code
no_blank_punctuations = ["—", "-", "…"]
# centre_punctuations = []

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
        # 2.4: Specific consonant pairs dtsz+ j (has a higher priority than 2.3)
        elif word1[firsr_word_tail] == 't' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʧ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 'd' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʤ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 's' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʃ)' + word2[second_word_start + 1:]
        elif word1[firsr_word_tail] == 'z' and word2[second_word_start] == 'j':
            return word1[:firsr_word_tail] + '(ʒ)' + word2[second_word_start + 1:]
        # 2.3: Consecutive consonants in same place in the mouth
        elif (word1[firsr_word_tail] in lips_consonants and word2[second_word_start] in lips_consonants) or (word1[firsr_word_tail] in teeth_consonants and word2[second_word_start] in teeth_consonants) or (word1[firsr_word_tail] in throat_consonants and word2[second_word_start] in throat_consonants):
            if word1[firsr_word_tail] in stops_consonants:
                return word1[:firsr_word_tail + 1] + '|' + word2[second_word_start:]
            return word1[:firsr_word_tail + 1] + '-' + word2[second_word_start:]

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
    input_text = '''/ə/ /laɪn/ /breɪk/ /wɪl/ /bi/ /ˈædəd/ /tə/ /ði/ /ɛnd/ /əv/ /iʧ/ /ˈsɛntəns/. /ˈpɪriəd/ /əz/ /ðə/ /moʊst/ /ˈkɑmən/ /ɛnd/ /əv/ /ˈsɛntənsəz/, /bət/ /ðə/ /səˈspɛnʃən/ /pɔɪnts/ /ˈɔlsoʊ/ /juz/ /ðə/ /seɪm/ /ˈsɪmbəl/. /haʊ/ /tə/ /meɪk/ /ðəm/ /kəˈrɛkt/? /wi/ /doʊnt/! /ðə/ /ˈproʊˌɡræm/ /wɪl/ /dʊ/ /ðə/ /ʤɑb/.
/kwoʊˈteɪʃən/ /mɑrks/ /ər/ /əˈnʌðər/ "/ɡreɪ/ /zoʊn/" /bɪˈkəz/ /ðeɪ/ /ˈɔlsoʊ/ /həv/ /ə/ /ˈsɪŋɡəl/ /ˈvɜrʒən/ /wɪʧ/ /ˈjusəz/ /ðə/ /seɪm/ /ˈsɪmbəl/ /əz/ /ði/ /əˈpɑstrəfi/. /wi/ /kən/ /ˈprɑˌsɛs/ /boʊθ/ /ˈvɜrʒənz/ /ənd/ /juz/ /səm/ /trɪks/ /tə/ /ˈsɪmpləˌfaɪ/ /ðə/ /ˈproʊˌɡræmz/ /aɪ///oʊ/.
/wɜrd/ /kəˈnɛkʃən/ /ˈkænɑt/ /ˈhæpən/ /əˈkrɔs/ /ˈkɑməz/, /ˈkoʊlənz/, /ənd/ /ˈbrækəts/. /ðɪs/ /ˈproʊˌɡræm/ /kən/ /ˈprɑˌsɛs/ /ðɛm/; /jʊ/ /ʃəd/ /juz/ /ðəm/ /kəˈrɛktli/ /ɪn/ /ði/ /ˈɪnˌpʊt/. /ðər/ /ər/ /tu/ /taɪps/ /əv/ /ˈbrækəts/: /ðə/ /lɛft/ /wʌnz/ /ənd/ /ðə/ /raɪt/ /wʌnz/ (/raʊnd/ /ɔr/ /skwɛr/). /ə/ /blæŋk/ /wɪl/ /əˈpɪr/ /ɪn/ /ðə/ /raɪt/ /pleɪs/ [/lɛft/ /ɔr/ /raɪt/] /ɪn/ /ði/ /ˈaʊtˌpʊt/.
/ˈhaɪfənz/ /ər/ /ˈɔlˌweɪz/ /ɪn/-/bɪˈtwin/ /ˈlɛtərz/. /bət/ /ðə/ /ˈsɪmələr/ /ˌpʌŋkʧuˈeɪʃən/-/ˈdæʃɪz/ /ər/ /səmˈtaɪmz/ /ˈrɪtən/ /ðə/ /seɪm/ /əz/ /ˈhaɪfənz/.
/ðɪs/ /ɪz/ /ðə/ /moʊst/ /ɪˈfɛktɪv/ /ˈproʊˌɡræm/.../ðæt/ /aɪ/ /meɪd/ /fər/ /ju/."/ɡoʊ/ /fər/ /ɪt/," /ɪt/ /sɛd/, '/lɛt/ /tɛkˈnɑləʤi/ /dʊ/ /ðə/ /ˈminɪŋləs/ /ʤɑbz/'.'''

    # Replace suspension points ... by … to make it different from period
    input_text = input_text.replace("...", "…")
     
    # Insert one or two blanks besides punctuations to make them splitable
    for punctuation in punctuations:
        input_text = input_text.replace(punctuation," "+punctuation+" ")
    
    paragraphs = input_text.split('\n')  # Split input into paragraphs
    for paragraph in paragraphs:
        # Split paragraph into sentences
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        for sentence in sentences:
            connected_sentence = ""
            words_and_punctuations = sentence.split()
            unclosed_quotation_marks = False # The indicator to show there is a left "
            unclosed_single_quotation_marks = False # The indicator to show there is a left '
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
                        else:
                            # Handle the punctuations ; ,
                            current_word_or_punctuation += words_and_punctuations[j]
                            i = j
                            break
                if current_word_or_punctuation[-1] == '"':
                    if unclosed_quotation_marks == False: 
                        connected_sentence += current_word_or_punctuation[:-1] + ' "'
                        unclosed_quotation_marks = True
                    else:
                        if connected_sentence.endswith(' ') and current_word_or_punctuation == '"':
                            # No blank between two punctuations( for ")
                            connected_sentence = connected_sentence[:-1] + current_word_or_punctuation + ' '
                        else:
                            connected_sentence += current_word_or_punctuation + ' '
                        unclosed_quotation_marks = False
                elif current_word_or_punctuation[-1] == "'":
                    if unclosed_single_quotation_marks == False: 
                        connected_sentence += current_word_or_punctuation[:-1] + " '"
                        unclosed_single_quotation_marks = True
                    else:
                        if connected_sentence.endswith(' ') and current_word_or_punctuation == "'":
                            # No blank between two punctuations( for ')
                            connected_sentence = connected_sentence[:-1] + current_word_or_punctuation + ' '
                        else:
                            connected_sentence += current_word_or_punctuation + ' '
                        unclosed_single_quotation_marks = False
                elif current_word_or_punctuation[-1] in left_blank_punctuations:
                        connected_sentence += current_word_or_punctuation[:-1] + ' ' + current_word_or_punctuation[-1]
                elif current_word_or_punctuation[-1] in no_blank_punctuations:
                        connected_sentence += current_word_or_punctuation
                else:
                    if connected_sentence.endswith(' ') and not current_word_or_punctuation.startswith("/"):
                        # No blank between two punctuations
                        connected_sentence = connected_sentence[:-1] + current_word_or_punctuation + ' '
                    else:
                        connected_sentence += current_word_or_punctuation + ' '
                i += 1
            # restore suspension points
            connected_sentence.replace("…", "...")
            print(connected_sentence.strip())
            
        # print()  # Empty line between paragraphs


if __name__ == "__main__":
    main()
