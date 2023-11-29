# Generated by Django 4.2.6 on 2023-11-15 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0003_rename_cart_id_cartitem_cart_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Compra Concluída'), (2, 'Cancelada')], default=0, verbose_name='Situação')),
                ('payment_option', models.CharField(choices=[('Ppagseguro', 'PagSeguro'), ('paypal', 'Paypal')], max_length=20, verbose_name='Opção de Pagamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos Pedidos',
            },
        ),
    ]
