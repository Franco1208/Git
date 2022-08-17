import random

a = random.randint(1,4)

def retweeted():
    print("Los top 10 tweets más retweeted")
def emitieron():
    print("Los top 10 usuarios en función de la cantidad de tweets que emitieron")

def mastweets():
    print("Los top 10 días donde hay más tweets.")


def hastags():
    print("Los top 10 hashtags más usados.")

def main(a):
    if a == 1:
        retweeted()
    elif a == 2:
        emitieron()
    elif a ==3:
        mastweets()
    elif a == 4:
        hastags()


