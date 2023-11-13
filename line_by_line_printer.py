import re

def main():
    original_text = '''A line break will be added to the end of each sentence. Period is the most common end of sentences, but the suspension points also use the same symbol. How to make them correct? We don't! The program will do the job.

Quotation marks are another "grey zone" because they also have a single version which uses the same symbol as the apostrophe. We can process both versions and use some tricks to simplify the program's I/O.

Word connection cannot happen across commas, colons, and brackets. This program can process them; you should use them correctly in the input. There are two types of brackets: the left ones and the right ones (round or square). A blank will appear in the right place [left or right] in the output.

Hyphens are always in-between letters. But the similar punctuation—dashes are sometimes written the same as hyphens.

This is the most effective program...that I made for you. "Go for it," it said, 'let technology do the meaningless jobs'.'''
    phonetic_text = '''/ə/ /laɪn/ /breɪk/ /wɪl/ /bi-j-ædəd|tə/ /ði-j-ɛnd-əv-iʧ-sɛntəns/.
/ˈpɪriəd-ə(zð)ə/ /moʊst/ /ˈkɑmən-ɛnd-əv/ /ˈsɛntənsəz/, /bə(tð)ə/ /səˈspɛnʃən/ /pɔɪnts-ɔlsoʊ/ /ju(zð)ə/ /seɪm/ /ˈsɪmbəl/.
/haʊ/ /tə/ /meɪ(kð)əm/ /kəˈrɛkt/?
/wi/ /doʊnt/!
/ðə/ /ˈproʊˌɡræm-wɪl-dʊ/ /ðə/ /ʤɑb/.

/kwoʊˈteɪʃən/ /mɑrks-ər-əˈnʌðər/ "/ɡreɪ/ /zoʊn/" /bɪˈkə(zð)eɪ-j-ɔlsoʊ/ /həv-ə/ /ˈsɪŋɡəl/ /ˈvɜrʒən/ /wɪʧ-jusə(zð)ə/ /seɪm/ /ˈsɪmbəl-ə(zð)i-j-əˈpɑstrəfi/.
/wi/ /kən/ /ˈprɑˌsɛs/ /boʊ(θv)ɜrʒənz-ən(ʤ)uz-səm/ /trɪks-tə/ /ˈsɪmpləˌfaɪ/ /ðə/ /ˈproʊˌɡræmz-aɪ///oʊ/.

/wɜrd/ /kəˈnɛkʃən/ /ˈkænɑt/ /ˈhæpən-əˈkrɔs/ /ˈkɑməz/, /ˈkoʊlənz/, /ənd/ /ˈbrækəts/.
/ðɪs/ /ˈproʊˌɡræm/ /kən/ /ˈprɑˌsɛ(sð)ɛm/; /jʊ/ /ʃə(ʤ)u(zð)əm/ /kəˈrɛktli-j-ɪ(nð)i-j-ɪnˌpʊt/.
/ðər-ər/ /tu/ /taɪps-əv-brækəts/: /ðə/ /lɛft/ /wʌnz-ən(dð)ə/ /raɪt/ /wʌnz/ (/raʊnd-ɔr/ /skwɛr/).
/ə/ /blæŋk/ /wɪl-əˈpɪr-ɪ(nð)ə/ /raɪt/ /pleɪs/ [/lɛft-ɔ(r)aɪt/] /ɪ(nð)i-j-aʊtˌpʊt/.

/ˈhaɪfənz-ər-ɔlˌweɪz-ɪn/-/bɪˈtwin-lɛtərz/.
/bə(tð)ə/ /ˈsɪmələr/ /ˌpʌŋkʧuˈeɪʃən/-/ˈdæʃɪz-ər/ /səmˈtaɪmz/ /ˈrɪtə(nð)ə/ /seɪm-əz/ /ˈhaɪfənz/.

/ðɪs-ɪ(zð)ə/ /moʊst-ɪˈfɛktɪv-proʊˌɡræm/…/ðæt-aɪ/ /meɪd/ /fər/ /ju/.
"/ɡoʊ/ /fər-ɪt/," /ɪt|sɛd/,  '/lɛ(t)ɛkˈnɑləʤi/ /dʊ/ /ðə/ /ˈminɪŋləs-ʤɑbz/'.
'''
    
    formated_text = ""
    # Make a formated version of original_text
    original_text_paragraphs = original_text.split('\n')
    for paragraph in original_text_paragraphs:
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        for sentence in sentences:
            formated_text += sentence + '\n'
        # formated_text += '\n'
    
    # Split by line breaks
    formated_text_lines = formated_text.split('\n')
    phonetic_text_lines = phonetic_text.split('\n')
    i = 0
    while i < len(phonetic_text_lines):
        print(formated_text_lines[i])
        print(phonetic_text_lines[i])
        if len(phonetic_text_lines[i]) > 1:
            print()
        i += 1

if __name__ == "__main__":
    main()