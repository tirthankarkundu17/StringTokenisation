from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


class FileReaderWriter:
    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        print("Reading File "+self.filename)
        data = open(self.filename, "r" , encoding="utf8")
        return data.read()

    def writeFile(self, string):
        print("Writing into File "+self.filename)
        data = open(self.filename, "w+")
        data.writelines(string)


class Tokenizer:
    def __init__(self, stringToTokenize):
        self.stringToTokenize = stringToTokenize

    def tokenizeString(self):
        print("Started Tokenizing-----")
        self.tokens = word_tokenize(self.stringToTokenize)

    def showTokens(self):
        print(self.tokens)

    def countWords(self):
        writeFilename = "news_stat.txt"  # Mention name of txt file you want to write into
        fileWriter = FileReaderWriter(writeFilename)
        frequencies = Counter(self.tokens)
        english_sw = stopwords.words('english')
        stringData = ''
        for token, count in frequencies.most_common():
            if(token in english_sw):
                continue
            elif(len(token) > 2 and token.isalnum()):
                stringData = stringData + token.upper() + ":"+str(count) + "\n"
        fileWriter.writeFile(stringData)
        print(stringData)


readFilename = "news.txt"  # Mention the filename of the txt file you want to read
fileReader = FileReaderWriter(readFilename)
string = fileReader.readFile()
tokenizer = Tokenizer(string)
tokenizer.tokenizeString()
tokenizer.countWords()
