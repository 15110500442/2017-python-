class People(object):
    country = 'China'
    def __init__(self):
        self.name = '中国'


    @ststicmethod
    def getCOuntry():
        return People.country


    @classmethod
    def getCountry(cls):
        return cls.country
