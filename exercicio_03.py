import requests
from bs4 import BeautifulSoup
import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
# cur.execute("""
# CREATE TABLE medicoes(
#     id SERIAL PRIMARY KEY,
#     temperatura text,
#     horario text
# )
# """)
# conn.commit()

url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi'
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
temperatura = html_soup.select('#momento-temperatura')[0].text[:2]
horario = html_soup.select('#momento-atualizacao')[0].string.split(' às ')[1].split(':')[0]

insert_query = "INSERT INTO public.medicoes(temperatura, horario) VALUES (%s, %s);" % (temperatura, horario)
cur.execute(insert_query)
conn.commit()

print(temperatura)