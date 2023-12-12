from django.db import models
# from django_resized import ResizedImageField
from django.conf import settings


# 재료 테이블(재료와 게시물을 M:N으로 연결, 이 테이블에 이미 재료가 있으면 가져와서 쓰고 없으면 새로 생성하기) 
class Ingred(models.Model):
    ingred_name = models.TextField()

    def __str__(self):
        return self.ingred_name
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='media/image', default='media/image/defaultimage.jpg')
    serving = models.IntegerField()
    # ingred = models.ManyToManyField(Ingred)
    # recipe = models.ManyToManyField("RecipeDetail")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='image/%Y/%m')

    CATE_CHOICES1 = (('한식', '한식'), ('양식', '양식'), ('일식', '일식'), ('기타', '기타'))
    cate1 = models.CharField(
        max_length=10,
        choices = CATE_CHOICES1,
        default='한식',
    )

    CATE_CHOICES2 = (('모임용', '모임용'), ('원팬/스피디', '원팬/스피디'), ('술안주', '술안주'), ('일상', '일상'), ('다이어트', '다이어트'), ('디저트', '디저트')) 
    cate2 = models.CharField(
        max_length=10,
        choices = CATE_CHOICES2,
        default='모임용',
    )
    CATE_CHOICES3 = (('소고기' ,'소고기'),('돼지고기' ,'돼지고기'),('닭고기' ,'닭고기'),('육류' ,'육류'),('채소' ,'채소'),('생선' ,'생선'),('해물' ,'해물'),('쌀' ,'쌀'),('밀가루' ,'밀가루'),('면' ,'면'),('콩/견과류' ,'콩/견과류'),('달걀/유제품' ,'달걀/유제품'),('가공식품류' ,'가공식품류'),('기타' ,'기타'))
    cate3 = models.CharField(
        max_length=10,
        choices = CATE_CHOICES3,
        default='기타',
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ingred = models.ManyToManyField(Ingred)
    
    # recipe_ingred = models.ForeignKey(RecipeIngred, on_delete=models.CASCADE)
    # recipe = models.ForeignKey(RecipeDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 나중에 게시물 받는 form 클래스에서 게시물제목, 인분, 이미지, 재료, 레시피 디테일 등등 을 받고 이를 밑에 클래스에 저장을 하는 형식으로 진행?
# 그때 save 할 때 
# 게시물 정보에 대해 먼저 저장을 한다.


    
class RecipeIngred(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ingred = models.ForeignKey(Ingred, on_delete=models.CASCADE)
    # ingred_name = models.TextField()
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.post.title}의 {self.ingred}용량'
    
    
class RecipeDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    step = models.IntegerField()
    contents = models.TextField()

    def __str__(self):
        return f'{self.post.title}의 {self.step}단계'


