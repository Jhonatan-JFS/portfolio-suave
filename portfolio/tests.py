from django.test import TestCase
from django.urls import reverse
from .models import Projeto

class PortfolioTests(TestCase):
    def test_home_carrega(self):
        self.assertEqual(self.client.get(reverse("portfolio:inicio")).status_code, 200)

    def test_projeto_publicado_visivel(self):
        projeto = Projeto.objects.create(titulo="Teste", resumo="Resumo", tecnologias="Python, Django")
        self.assertContains(self.client.get(reverse("portfolio:inicio")), "Teste")
        self.assertEqual(projeto.lista_tecnologias, ["Python", "Django"])
        self.assertEqual(self.client.get(reverse("portfolio:detalhe", args=[projeto.pk])).status_code, 200)

    def test_projeto_oculto_nao_exposto(self):
        projeto = Projeto.objects.create(titulo="Oculto", resumo="Não público", tecnologias="Python", publicado=False)
        self.assertNotContains(self.client.get(reverse("portfolio:inicio")), "Oculto")
        self.assertEqual(self.client.get(reverse("portfolio:detalhe", args=[projeto.pk])).status_code, 404)
