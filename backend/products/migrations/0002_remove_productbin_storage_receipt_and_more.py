# Generated by Django 4.0.10 on 2023-05-16 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbin',
            name='storage_receipt',
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('name', 'location')},
        ),
        migrations.CreateModel(
            name='Productbin_Storagereceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prduct_bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productbin')),
                ('storage_receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.storagereceipt')),
            ],
            options={
                'unique_together': {('prduct_bin', 'prduct_bin')},
            },
        ),
    ]
