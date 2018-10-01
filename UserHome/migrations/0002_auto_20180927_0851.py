from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('UserHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
