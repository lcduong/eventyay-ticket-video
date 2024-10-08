from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredApplePayDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=190)),
                ('account', models.CharField(max_length=190)),
            ],
        ),
        migrations.CreateModel(
            name='ReferencedStripeObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('reference', models.CharField(db_index=True, max_length=190, unique=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretixbase.order')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.orderpayment')),
            ],
        ),
    ]
