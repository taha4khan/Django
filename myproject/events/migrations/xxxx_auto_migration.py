from django.db import migrations, models
import datetime
from django.utils.timezone import now

def batch_update_created_at(apps, schema_editor):
    YourModel = apps.get_model("your_app", "YourModel")
    db_alias = schema_editor.connection.alias
    batch_size = 10000  # adjust batch size based on your environment's performance
    total = YourModel.objects.using(db_alias).count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        batch = YourModel.objects.using(db_alias).all()[start:end]
        batch.update(created_at=now() - datetime.timedelta(days=2))

class Migration(migrations.Migration):
    dependencies = [
        ('your_app', 'previous_migration_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='yourmodel',
            name='created_at',
            field=models.DateTimeField(default=now),
        ),
        migrations.RunPython(batch_update_created_at),
    ]
