from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        managed = False

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False

class Client(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        managed = False

class Estacao(models.Model):
    id_estacao = models.AutoField(primary_key=True)
    codigo_estacao = models.IntegerField()
    placa_estacao = models.CharField(max_length=8)
    estacao = models.CharField(max_length=30)
    status_estacao = models.CharField(max_length=30)
    data_criacao_estacao = models.DateTimeField(auto_now_add=True)
    data_validade_orcamento_estacao = models.DateField()

    class Meta:
        db_table = 'estacao'
        managed = False

class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    codigo_material = models.IntegerField()
    placa_material = models.CharField(max_length=8)
    produto_material = models.CharField(max_length=30, default='DESMONTA')
    quantidade_material = models.IntegerField(default=1)
    data_criacao_material = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'material'
        managed = False

class Produto(models.Model):
    codigo_produto = models.AutoField(primary_key=True)
    linha_servico_produto = models.CharField(max_length=50)
    tipo_produto = models.CharField(max_length=50)
    preco_custo_produto = models.DecimalField(max_digits=8, decimal_places=2)
    preco_venda_produto = models.DecimalField(max_digits=8, decimal_places=2)
    data_cadastro_produto = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateField(auto_now=True)

    class Meta:
        db_table = 'produto'
        managed = False

class Veiculo(models.Model):
    codigo_veiculo = models.AutoField(primary_key=True)
    placa_veiculo = models.CharField(max_length=8)
    marca_veiculo = models.CharField(max_length=30)
    modelo_veiculo = models.CharField(max_length=30)
    ano_veiculo = models.CharField(max_length=30)
    cor_veiculo = models.CharField(max_length=30)
    proprietario_veiculo = models.CharField(max_length=100)
    cpf_proprietario_veiculo = models.CharField(max_length=11, null=True, blank=True)
    telefone_proprietario_veiculo = models.CharField(max_length=11, null=True, blank=True)
    data_veiculo = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'veiculo'
        managed = False
