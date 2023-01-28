from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length


class CreateBookForm(FlaskForm):
    title = StringField("Título", validators=[InputRequired(), Length(min=0, max=255)])
    synopsis = TextAreaField("Sinopse")
    author_name = StringField(
        "Autor(a)", validators=[InputRequired(), Length(min=0, max=255)]
    )
    publishing_company_name = StringField(
        "Editora", validators=[InputRequired(), Length(min=0, max=255)]
    )
    release_year = DateField("Ano de lançamento", validators=[InputRequired()])
    category = StringField("Categoria", validators=[Length(min=0, max=255)])


class UpdateBookForm(FlaskForm):
    title = StringField("Título", validators=[Length(min=0, max=255)])
    synopsis = TextAreaField("Sinopse")
    author_name = StringField("Autor(a)", validators=[Length(min=0, max=255)])
    publishing_company_name = StringField(
        "Editora", validators=[Length(min=0, max=255)]
    )
    release_year = DateField("Ano de lançamento")
    category = StringField("Categoria", validators=[Length(min=0, max=255)])
