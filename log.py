# NGUYEN HuuTuan 3A33

from discord.ext import commands
import logging


# Classe pour gérer les logs du Bot Discord
class Logger(commands.Cog):

	# Fonction d'initialisation de la classe
	def __init__(self, bot, config) -> None:
		super().__init__()
		self.bot = bot
		self.setupLog(config)


	# Fonction de configuration des logs
	def setupLog(self, config):
		log_format = str(config['log_format'])
		log_date = str(config['log_date'])
		log_file = str(config['log_file'])

		logging.basicConfig(filename=log_file, encoding='utf-8', format=log_format, datefmt=log_date, level=logging.INFO)


	# Fonction d'impression de debugs dans les logs
	def debugLog(msg):
		logging.debug(msg)


	# Fonction d'impression d'informations dans les logs
	def infoLog(msg):
		logging.info(msg)


	# Fonction d'impression de warnings dans les logs
	def warningLog(msg):
		logging.warning(msg)


	# Fonction d'impression d'erreurs dans les logs
	def errorLog(msg):
		logging.error(msg)


	# Fonction d'impression de debug dans les logs
	def criticalLog(msg):
		logging.critical(msg)