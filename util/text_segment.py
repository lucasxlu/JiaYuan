import jieba
import jieba.analyse

user_dict = 'D:/Users/29140/PycharmProjects/JiaYuan/res/user_dict.txt'
stop_words = 'D:/Users/29140/PycharmProjects/JiaYuan/res/stop_words.txt'


def segment_text(text):
    # load user dict
    jieba.load_userdict(user_dict)
    # set stop words
    jieba.analyse.set_stop_words(stop_words)
    tags = jieba.analyse.extract_tags(text, topK=20, withWeight=True, allowPOS=())
    for tag in tags:
        print(str(tag[0]) + "\t" + str(tag[1]))

def read_all_textline(text_path):
    text = ''
    with open(text_path, mode='rt') as f:
        for each_line in f.readlines():
            text += each_line

    return text


if __name__ == '__main__':
    text = read_all_textline('D:/JiaYuan_BasicInfo/requirement/male/matchcondition-hb.txt')
    segment_text(text)
