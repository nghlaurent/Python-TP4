# NGUYEN HuuTuan 3A33

from discord.ext.commands import Bot
from discord.ext.commands.context import Context
from message import CustomCommands
from log import Logger

import argparse
import json


# Classe pour créer le Bot Discord
class MyBot(Bot):

	# Fonction d'initialisation de la classe
	def __init__(self, config):
		super().__init__(str(config['prefix']))
		self.remove_command("help")
		
		self.add_cog(CustomCommands(self))
		self.add_cog(Logger(self, config))


	# Fonction de détection, lorsque le Bot Discord est prêt
	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')


# Fonction de récupération d'informations, données en paramètres d'arguments via la console
def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
	return parser.parse_args()


# Fonction principale, qui va permettre d'initialiser le Bot Discord
def main():
	args = get_args()
	config = json.load(open(args.config))
	
	bot = MyBot(config)
	bot.run(str(config['token']))


# Fonction de démarrage de script du fichier.py
if __name__ == "__main__":
	main()