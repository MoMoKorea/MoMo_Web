# Generated by Django 2.2.3 on 2019-12-22 08:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildAgeORM',
            fields=[
                ('child_age_id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.CharField(max_length=20)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'child_age',
            },
        ),
        migrations.CreateModel(
            name='JobAgeMappingORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'job_age_mapping',
            },
        ),
        migrations.CreateModel(
            name='JobAgeORM',
            fields=[
                ('job_age_id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(help_text='지원 연령대')),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_age',
            },
        ),
        migrations.CreateModel(
            name='JobCarPreferenceORM',
            fields=[
                ('car_preference_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(default='', help_text='차량소지선호 여부', max_length=20)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_car_preference',
            },
        ),
        migrations.CreateModel(
            name='JobDayOfWeekMappingORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'job_day_of_week_mapping',
            },
        ),
        migrations.CreateModel(
            name='JobDayOfWeekORM',
            fields=[
                ('job_day_of_week_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=5)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_day_of_week',
            },
        ),
        migrations.CreateModel(
            name='JobLocationORM',
            fields=[
                ('job_location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('parent_location_id', models.IntegerField(null=True)),
                ('depth', models.SmallIntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_location',
            },
        ),
        migrations.CreateModel(
            name='JobORM',
            fields=[
                ('job_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(default=0, help_text='회원 번호')),
                ('status', models.SmallIntegerField(default=1)),
                ('title', models.CharField(default='', help_text='글 제목', max_length=50)),
                ('pay', models.IntegerField(default=0)),
                ('is_negotiation', models.BooleanField(default=False)),
                ('third_location_id', models.SmallIntegerField(default=1)),
                ('description', models.TextField(default='')),
                ('start_available_calling_time', models.TimeField()),
                ('end_available_calling_time', models.TimeField()),
                ('start_working_time', models.TimeField(null=True)),
                ('end_working_time', models.TimeField(null=True)),
                ('start_working_date', models.DateField(default=django.utils.timezone.now)),
                ('end_working_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('car_preference', models.ForeignKey(db_column='car_preference_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobCarPreferenceORM')),
                ('child_age', models.ForeignKey(db_column='child_age_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_age', to='job.ChildAgeORM')),
                ('day_of_weeks', models.ManyToManyField(null=True, related_name='day_of_weeks', through='job.JobDayOfWeekMappingORM', to='job.JobDayOfWeekORM')),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='JobRequireDocumentORM',
            fields=[
                ('job_require_document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_require_document',
            },
        ),
        migrations.CreateModel(
            name='JobSexORM',
            fields=[
                ('job_sex_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sex', models.CharField(default='', help_text='성별', max_length=10)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_sex',
            },
        ),
        migrations.CreateModel(
            name='JobRequireDocumentMappingORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, to='job.JobORM')),
                ('require_document_id', models.ForeignKey(db_column='job_require_document_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobRequireDocumentORM')),
            ],
            options={
                'db_table': 'job_require_document_mapping',
            },
        ),
        migrations.AddField(
            model_name='joborm',
            name='documents',
            field=models.ManyToManyField(null=True, related_name='documents', through='job.JobRequireDocumentMappingORM', to='job.JobRequireDocumentORM'),
        ),
        migrations.AddField(
            model_name='joborm',
            name='root_location',
            field=models.ForeignKey(db_column='root_location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='root_location', to='job.JobLocationORM'),
        ),
        migrations.AddField(
            model_name='joborm',
            name='second_location',
            field=models.ForeignKey(db_column='second_location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_location', to='job.JobLocationORM'),
        ),
        migrations.AddField(
            model_name='joborm',
            name='worker_age',
            field=models.ManyToManyField(null=True, related_name='worker_age', through='job.JobAgeMappingORM', to='job.JobAgeORM'),
        ),
        migrations.AddField(
            model_name='joborm',
            name='worker_sex',
            field=models.ForeignKey(db_column='worker_sex_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker_sex', to='job.JobSexORM'),
        ),
        migrations.AddField(
            model_name='jobdayofweekmappingorm',
            name='day_of_week_id',
            field=models.ForeignKey(db_column='day_of_week_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='job.JobDayOfWeekORM'),
        ),
        migrations.AddField(
            model_name='jobdayofweekmappingorm',
            name='job_id',
            field=models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, to='job.JobORM'),
        ),
        migrations.AddField(
            model_name='jobagemappingorm',
            name='age_id',
            field=models.ForeignKey(db_column='job_age_id', on_delete=django.db.models.deletion.CASCADE, to='job.JobAgeORM'),
        ),
        migrations.AddField(
            model_name='jobagemappingorm',
            name='job_id',
            field=models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, to='job.JobORM'),
        ),
    ]
