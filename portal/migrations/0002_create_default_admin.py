from django.db import migrations


def create_admin(apps, schema_editor):
    User = apps.get_model('portal', 'User')
    if not User.objects.filter(username='BraveGuap').exists():
        User.objects.create_user(
            username='BraveGuap',
            password='gosdum',
            full_name='Администратор Портала',
            phone='8(999)000-00-00',
            email='braveguap@gosdumamusic.local',
            is_staff=True,
            is_superuser=True,
        )


def remove_admin(apps, schema_editor):
    User = apps.get_model('portal', 'User')
    User.objects.filter(username='BraveGuap').delete()


class Migration(migrations.Migration):
    dependencies = [('portal', '0001_initial')]

    operations = [migrations.RunPython(create_admin, remove_admin)]
