from django.forms import ModelForm
from app.models import Filmes,Serie

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'duracao', 'ano','produtor','diretor','elenco','direcao']

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields =['nomeSerie','numEp','numTemp','produtoraSerie']
