# Generated by Django 5.0.1 on 2024-01-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_remove_comment_email_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=2, max_length=59),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='fdaf08', max_length=6),
        ),
    ]
