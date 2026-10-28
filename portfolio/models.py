from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=120)
    resumo = models.CharField(max_length=250)
    descricao = models.TextField(blank=True)
    tecnologias = models.CharField(max_length=180, help_text="Separe com vírgulas")
    imagem = models.ImageField(upload_to="projetos/", blank=True, null=True)
    link_github = models.URLField(blank=True)
    link_demo = models.URLField(blank=True)
    destaque = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-destaque", "-criado_em"]
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo

    @property
    def lista_tecnologias(self):
        return [x.strip() for x in self.tecnologias.split(",") if x.strip()]
