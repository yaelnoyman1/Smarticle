# Generated by Django 4.1.3 on 2022-11-23 11:48

from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('projboard', '0004_test_user_data'),
        ('projboard', '0006_test_subject_data'),
    ]

    def generate_article_data(apps, schema_editor):
        from projboard.models.article import Article, User, Subject

        user1 = User.get_user_by_nickname("User1")
        user2 = User.get_user_by_nickname("User2")
        subject1 = Subject.get_subject_by_name('Sport')
        subject2 = Subject.get_subject_by_name('Math')

        test_data = [
            [user1, 'World cup', subject1, 'Messi is better then CR7'],
            [user2, '1+1 = 3', subject2, 'By Pythagoras'],
        ]
        with transaction.atomic():
            for a in test_data:
                Article(user_id=a[0], title=a[1], subject_id=a[2], content=a[3]).save()

    operations = [
        migrations.RunPython(generate_article_data),
    ]