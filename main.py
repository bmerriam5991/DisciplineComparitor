import csv
#stored in the array sections, holds name of stream and courses in stream
class section:
    def __init__(self, Name,courseList):
        self.name=Name
        self.courses=courseList

#some classes that might need to be implemented for full scale build-------
# class fullCourseList:
#     def __init__(self, courses):
#         self.courses=courses
#     def addCourse(self,coursename,courseDescription):
#         if coursename in self.courses:
#             self.courses.append(course(coursename, courseDescription))
#
# class course:
#     def__init__(self, courseName, courseDescription):
#         self.courseName=courseName
#         self.courseDescription=courseDescription

#Accepts 2 indexes of sections and returns the overlapping ones------------
def intersect(Index1, Index2,List):
    return set(List[Index1].courses).intersection(List[Index2].courses)
#reads data from 2 CSV files cause I don't know how to put into one
data=csv.reader(open('Courses.csv', 'rt'))
f=open('DisciplineList.csv','rt')
PlanData=csv.reader(f)
#initializes some stuff, probably better in classes but thats hard
column1,streamName=[],[]
sections=[]
#grabs all of the possible stream names----------------
for row in PlanData:
    for i in range(20):
        streamName.append(row[i])
    break
#-----populates sections with the stream names and all their courses-------
for i in range(20):
    f.seek(0)
    column1.clear()
    for row in PlanData:
        if  row[i]:
            column1.append(row[i])
    #deletes stream name from course listings--------------------------
    column1=column1[1:]
    sections.append(section(streamName[i],column1))
    print(sections[i].courses)
    print("\n")
    #weird stuff happens here, they are all shifted up one
print(sections[0].courses)
#----------infinite loop to request values to check---------------------------
#current bug: sections[0] is equal to sections[19] and i don't know why
while 1:
    try:
    #accept values for value1 and value2 from user (bug might be here)
        value1=int(input('Value 1: '),10)
        value2=int(input('Value 2: '))
    except ValueError:
        print ("not a number!")
    print(sections[value1].name + " and " + sections[value2].name)
    # print(sections[value1].courses)
    # print(sections[value2].courses)
    # print("\n")

    #temporary fix, only breaks if value 1 is equal to 0 then it goes to 19
    print(intersect(value1-1,value2-1,sections))
