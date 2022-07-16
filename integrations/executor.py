from .funky_dice import DiceRoomGenerator
from .wpp import whats_msg

""" 

    Chamar a função integrate() dentro da rota de iniciar jornada passando pra ela um array
    com o telefone de todos os usuário naquela campanha

"""

def integrate(players_phones):
    nova_sala = DiceRoomGenerator()
    nova_sala.open()
    nova_sala.generate_room()
    nova_sala.enter_room()
    link = nova_sala.get_room_link()

    nova_sala.close()
    
    for num in players_phones:
        message = f'Olá, como vai? Sou o mestre da jornada que você entrou pelo Trinity Dice! Aqui está o link da nossa sala de lançamento de dados: {link}'
        whats_msg(num, message)

    return True

