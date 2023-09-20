# Generated by Django 4.2.4 on 2023-09-02 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comment_delete_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='post.products'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]