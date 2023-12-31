# Generated by Django 5.0 on 2023-12-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_ingred_remove_post_recipe_remove_post_ingred_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cate1',
            field=models.CharField(choices=[('한식', '한식'), ('양식', '양식'), ('일식', '일식'), ('기타', '기타')], default='한식', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='cate2',
            field=models.CharField(choices=[('모임용', '모임용'), ('원팬/스피디', '원팬/스피디'), ('술안주', '술안주'), ('일상', '일상'), ('다이어트', '다이어트'), ('디저트', '디저트')], default='모임용', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='cate3',
            field=models.CharField(choices=[('소고기', '소고기'), ('돼지고기', '돼지고기'), ('닭고기', '닭고기'), ('육류', '육류'), ('채소', '채소'), ('생선', '생선'), ('해물', '해물'), ('쌀', '쌀'), ('밀가루', '밀가루'), ('면', '면'), ('콩/견과류', '콩/견과류'), ('달걀/유제품', '달걀/유제품'), ('가공식품류', '가공식품류'), ('기타', '기타')], default='기타', max_length=10),
        ),
    ]
