from populate import base
import datetime

from account.models import User

from survey.models import Survey, Question, Choice, Response

# TODO: this script is not finished
# content -> description

titles = [
    '本校106年度歲末聯歡餐會參加調查',  
    '107學年度第1學期第3次系務會議暨第2次系教評會議出席調查',
]

contents = [
    '因為此次尾牙為資訊學院主辦，請大家務必參加!!', 
    '系教評提案：(1)兼任教師提聘案(2)兼任教師續聘案',
    '為節省出餐時間，請老師參閱菜單內容，並於意見欄加註餐點內容。'
]


def populate():
    print('Populating Survey and Question ... ', end='')
    Survey.objects.all().delete()
    Question.objects.all().delete()
    Choice.objects.all().delete()
    Response.objects.all().delete()
    userList = User.objects.first()
    for title in titles:
        survey = Survey()
        survey.title = title
        survey.description = title
        survey.date = datetime.date.today()
        survey.startDate = survey.date
        survey.endDate = survey.startDate + datetime.timedelta(60)
        survey.user = userList
        survey.emailContent = '新的問題開始'
        survey.save()
        for content in contents:
            question = Question()
            question.survey = survey
            question.title += 'Q：' + title
            question.description += title + content + '\n'
            question.save()
            Choice.objects.create(question= question, name='是')
            Choice.objects.create(question= question, name='否，另有要事')
    print('done')
    

if __name__ == '__main__':
    populate()
