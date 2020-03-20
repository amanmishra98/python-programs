# Generated by Django 3.0.3 on 2020-03-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=30)),
                ('change', models.FloatField(max_length=30)),
                ('val', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BSE2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30)),
                ('high', models.FloatField(max_length=30)),
                ('low', models.FloatField(max_length=30)),
                ('last_price', models.FloatField(max_length=30)),
                ('change_percent', models.FloatField(max_length=30)),
                ('value', models.FloatField(max_length=30)),
                ('five_day', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fill_SEBI2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('equity_gross_pur', models.FloatField(max_length=30)),
                ('equity_gross_sal', models.FloatField(max_length=30)),
                ('equity_net_pur', models.FloatField(max_length=30)),
                ('debt_gross_pur', models.FloatField(max_length=30)),
                ('debt_gross_sal', models.FloatField(max_length=30)),
                ('debt_net_pur', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FillAndDill_Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('net_fill', models.FloatField(max_length=30)),
                ('net_dill', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FillAndDill_Cash2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fill_gross_pur', models.FloatField(max_length=30)),
                ('fill_gross_sal', models.FloatField(max_length=30)),
                ('fill_net_pur', models.FloatField(max_length=30)),
                ('dill_gross_pur', models.FloatField(max_length=30)),
                ('dill_gross_sal', models.FloatField(max_length=30)),
                ('dill_net_pur', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FillAndDill_SEBI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('equity', models.FloatField(max_length=30)),
                ('debt', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalIndices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=30)),
                ('change', models.FloatField(max_length=30)),
                ('change_percent', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalIndices2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('current_value', models.FloatField(max_length=30, null=True)),
                ('change', models.FloatField(max_length=30, null=True)),
                ('change_percent', models.FloatField(max_length=30, null=True)),
                ('open', models.FloatField(max_length=30, null=True)),
                ('high', models.FloatField(max_length=30, null=True)),
                ('low', models.FloatField(max_length=30, null=True)),
                ('prev_close', models.FloatField(max_length=30, null=True)),
                ('five_day', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndianIndices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=30)),
                ('change', models.FloatField(max_length=30)),
                ('change_percent', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IndianIndices2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('current_value', models.FloatField(max_length=30)),
                ('change', models.FloatField(max_length=30)),
                ('change_percent', models.FloatField(max_length=30)),
                ('open', models.FloatField(max_length=30)),
                ('high', models.FloatField(max_length=30)),
                ('low', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nifty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(max_length=30)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=30)),
                ('change', models.FloatField(max_length=30)),
                ('val', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NSE2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('high', models.FloatField(max_length=30)),
                ('low', models.FloatField(max_length=30)),
                ('last_price', models.FloatField(max_length=30)),
                ('change_percent', models.FloatField(max_length=30)),
                ('value', models.FloatField(max_length=30)),
                ('five_day', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sensex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(max_length=30)),
                ('time', models.TimeField()),
            ],
        ),
    ]
