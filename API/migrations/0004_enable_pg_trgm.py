from django.db import migrations
from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):
    dependencies = [
        ('API', '0003_alter_intelforscienceworks_key_words'),
    ]
    operations = [
        CreateExtension('pg_trgm'),
    ]