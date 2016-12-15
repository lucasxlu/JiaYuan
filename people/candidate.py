class Candidate():
    def __init__(self, uid=0, nickname='', age=0, height=0, image='', marriage='', education='', work_location='',
                 work_sublocation='',
                 shortnote='', matchCondition='', randListTag='', province='', gender=''):
        self.uid = uid
        self.nickname = nickname
        self.age = age
        self.height = height
        self.image = image
        self.marriage = marriage
        self.education = education
        self.work_location = work_location
        self.work_sublocation = work_sublocation
        self.shortnote = shortnote
        self.matchCondition = matchCondition
        self.randListTag = randListTag
        self.province = province
        self.gender = gender

    def __str__(self):
        return "{ " + str(self.uid) + " ;" + self.nickname + " ;" + str(self.age) + " ;" + str(
            self.height) + " ;" + self.image + " ;" + self.marriage + " ;" + self.education + " ;" \
               + self.work_location + " ;" + self.work_sublocation + " ;" + self.shortnote + " ;" + self.matchCondition + " ;" + self.randListTag + " ;" + self.province \
               + " ;" + str(self.gender) + " }"
