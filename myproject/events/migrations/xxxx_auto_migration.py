from django.db import migrations, models
import datetime
from django.utils.timezone import now

def forward_func(apps, schema_editor):
    MyModel = apps.get_model("events", "Event")
    db_alias = schema_editor.connection.alias
    MyModel.objects.using(db_alias).all().update(created_at=now() - datetime.timedelta(days=2))

class Migration(migrations.Migration):
    dependencies = [
        ('events', 'previous_migration_filename'),  # replace 'previous_migration_filename' with the actual file
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=now),
        ),
        migrations.RunPython(forward_func),
    ]
