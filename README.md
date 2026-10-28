# Portfólio suave — Jhonatan Furtado

Portfólio pessoal em **Python + Django (arquitetura MVT)**, inspirado na organização ensinada no [Gist de André Luferat](https://gist.github.com/Luferat/5bf70eb67687e7dc67ff98461e91347c), consultado em 28/10/2026. Código independente, com identidade visual própria.

## Estrutura

- `core/` — configurações, URLs e inicialização do Django.
- `portfolio/` — model, views, URLs, painel admin e migrações.
- `templates/_base.html` — template herdado pelas páginas.
- `templates/portfolio/` — página inicial e detalhe de projeto.
- `static/css/style.css` — visual responsivo.
- `.env.example` — exemplo das variáveis de ambiente.
- `.gitignore` — arquivos que não devem ir ao GitHub.
- `requirements.txt` — bibliotecas necessárias.

## Instalação no Windows (VS Code / Prompt de Comando)

1. Extraia o ZIP, abra a pasta `portfolio-suave` no VS Code.
2. Abra o Prompt de Comando no terminal (não precisa PowerShell).
3. Crie e ative o ambiente virtual:

   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Instale as dependências:

   ```bat
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Copie o arquivo `.env.example` para `.env`:

   ```bat
   copy .env.example .env
   ```

6. Abra `.env` e troque `DJANGO_SECRET_KEY`. Para gerar uma chave aleatória:

   ```bat
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

7. Crie o banco e o administrador:

   ```bat
   python manage.py migrate
   python manage.py createsuperuser
   ```

8. Execute:

   ```bat
   python manage.py runserver
   ```

9. Acesse `http://127.0.0.1:8000/`. Para cadastrar projetos, abra `http://127.0.0.1:8000/admin/`, entre com o administrador e adicione registros em **Projetos**.

## Primeiro envio ao GitHub

Crie um **repositório novo e vazio** no GitHub (ex.: `portfolio-jhonatan`), sem marcar a opção de criar README ou .gitignore, pois já existem aqui.

```bat
git init
git add .
git commit -m "Portfólio Django inicial"
git branch -M main
git remote add origin https://github.com/Jhonatan-JFS/portfolio-jhonatan.git
git push -u origin main
```

> Troque o endereço remoto se escolher outro nome. O arquivo `.env`, o banco SQLite, imagens enviadas, cache e `.venv` **não** serão enviados — conforme o `.gitignore`.

## Configuração de produção

- Defina `DJANGO_DEBUG=False`, uma chave secreta forte e `DJANGO_ALLOWED_HOSTS` com o domínio real.
- Preencha `DJANGO_CSRF_TRUSTED_ORIGINS` com a URL HTTPS do domínio.
- Rode `python manage.py check --deploy` e `python manage.py collectstatic`.
- Configure o servidor WSGI para `core.wsgi.application`, a entrega dos arquivos estáticos e a persistência dos arquivos de mídia.
- Produção exige HTTPS e configuração do host; SQLite atende o desenvolvimento. MySQL pode ser configurado futuramente conforme o Gist.

## Personalização

- Nome e textos: `templates/portfolio/inicio.html`.
- Cores: início de `static/css/style.css`.
- Projetos: painel `/admin/` (título, resumo, descrição, tecnologias, imagem e links).
- Links externos exibidos atualmente: perfil GitHub `Jhonatan-JFS`. Acrescente e-mail ou redes sociais somente quando desejar.

## Observações

O design usa fontes Google Fonts; sem internet, o navegador utiliza fontes alternativas. A página mostra cartões demonstrativos somente enquanto não há projetos cadastrados. O login padrão é o do Django Admin; não há cadastro público de usuários.
