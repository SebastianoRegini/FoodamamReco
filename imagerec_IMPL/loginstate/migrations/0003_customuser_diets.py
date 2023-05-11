# Generated by Django 3.2.15 on 2022-08-16 14:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loginstate', '0002_alter_customuser_allergies'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='diets',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Alcohol-free', 'No alcool'), ('Balanced', 'Bilanciata'), ('High-Fiber', 'Molte fibre'), ('High-Protein', 'Molte proteine'), ('Keto', 'Chetogenica'), ('Kidney friendly', 'Per i reni'), ('Kosher', 'Kosher'), ('Low-Carb', 'Pochi carboidrati'), ('Low-Fat', 'Pochi grassi'), ('Low potassium', 'Poco potassio'), ('Low-Sodium', 'Povera di sodio'), ('No oil added', 'Senza olio aggiunto'), ('No-sugar', 'Senza zuccheri'), ('Paleo', 'Paleolitica'), ('Pescatarian', 'Pescetariana'), ('Pork-free', 'Senza carne di maiale'), ('Red meat-free', 'Senza carne rossa'), ('Sugar-conscious', 'Pochi zuccheri'), ('Vegan', 'Vegana'), ('Vegetarian', 'Vegetariana')], max_length=212),
        ),
    ]