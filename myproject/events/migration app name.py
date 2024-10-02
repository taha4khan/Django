from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('events', '0003_auto_20200928_1625'),  # Adjust this line based on actual app and previous migration
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE events_event ADD COLUMN created_at TIMESTAMP DEFAULT (NOW() - INTERVAL '2 days');
            """,
            reverse_sql="""
                ALTER TABLE events_event DROP COLUMN created_at;
            """
        ),
    ]
