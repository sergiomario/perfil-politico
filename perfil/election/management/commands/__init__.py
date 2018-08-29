from unidecode import unidecode

from perfil.election.models import Election
from perfil.mandate.models import Politician
from perfil.party.models import Party
from perfil.person.models import Person
from perfil.utils.tools import parse_date, treat_birthday


def election_keys(election):
    if isinstance(election, Election):
        return election.year, election.state, election.candidate_sequential

    if 'ano_eleicao' in election:  # assets CSV
        return (
            election['ano_eleicao'],
            election['sigla_uf'],
            election['sq_candidato']
        )

    return election['ano'], election['uf'], election['numero']


def person_keys(person):
    if isinstance(person, Person):
        return unidecode(person.civil_name), person.cpf
    return unidecode(person['nome_candidato']), person['cpf_candidato']


def person_keys_birthdate(person):
    if isinstance(person, Person):
        return unidecode(person.civil_name), person.birthdate
    birthday = treat_birthday(person['birthday'])
    return unidecode(person['name']), parse_date(birthday)


def party_keys(party):
    if isinstance(party, Party):
        return party.initials,
    return party['sigla_partido'],


def politician_keys(politician):
    if isinstance(politician, Politician):
        return politician.congressperson_id,
    return str(politician['congressperson_id']),


def politician_name_keys(politician):
    if isinstance(politician, Politician):
        return uniddecode(politician.congressperson_name),
    return unidecode(politician['congressperson_name']),
