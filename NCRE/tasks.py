from dbfpy import dbf
from NCRE.func import delete_media
from NCRE.models import TestScore
from cntest.celery import app
from cntest.settings import MEDIA_ROOT


@app.task
def import_score(file_name, ncre):
    db = dbf.Dbf(MEDIA_ROOT + file_name)
    for rec in db:
        stu_name = rec['XM'].decode('gb18030')
        test_id = rec['ZKZH']
        stu_id = rec['SFZH']
        paper_score = rec['ZZBSCJ']
        score = rec['ZZSJCJ']
        level = rec['CJ4']
        cert_id = rec['ZSBH']
        if not TestScore.objects.filter(testId=test_id):
            test_score = TestScore(stuId=stu_id, testId=test_id, stuName=stu_name, score=score,
                                   paper_score=paper_score, ncre=ncre, level=level, certId=cert_id)
            test_score.save()
    delete_media(file_name)