from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="Projeto",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("titulo", models.CharField(max_length=120)),
            ("resumo", models.CharField(max_length=250)),
            ("descricao", models.TextField(blank=True)),
            ("tecnologias", models.CharField(help_text="Separe com vírgulas", max_length=180)),
            ("imagem", models.ImageField(blank=True, null=True, upload_to="projetos/")),
            ("link_github", models.URLField(blank=True)),
            ("link_demo", models.URLField(blank=True)),
            ("destaque", models.BooleanField(default=False)),
            ("publicado", models.BooleanField(default=True)),
            ("criado_em", models.DateTimeField(auto_now_add=True)),
        ],
        options={"verbose_name": "Projeto", "verbose_name_plural": "Projetos", "ordering": ["-destaque", "-criado_em"]},
    )]
