from .funky_dice import DiceRoomGenerator
from .wpp import whats_msg

""" 

    Chamar a função integrate() dentro da rota de iniciar jornada passando pra ela um array
    com o telefone de todos os usuário naquela campanha

"""


def integrate(players_phones):
    new_room = DiceRoomGenerator()
    new_room.open()
    new_room.generate_room()
    new_room.enter_room()
    link = new_room.get_room_link()

    new_room.close()

    for num in players_phones:
        message = f"Olá, como vai? Sou o mestre da jornada que você entrou pelo Trinity Dice! Aqui está o link da nossa sala de lançamento de dados: {link}"
        whats_msg(num, message)

    return True
