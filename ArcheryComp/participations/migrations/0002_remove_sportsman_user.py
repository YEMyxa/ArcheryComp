
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsman',
            name='user',
        ),
    ]
