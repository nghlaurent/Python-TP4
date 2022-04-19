# NGUYEN HuuTuan 3A33

from log import Logger
from discord.ext import commands
import discord


# Classe pour gérer les commandes, appelées en message
class CustomCommands(commands.Cog):

	# Fonction d'initialisation de la classe
	def __init__(self, bot) -> None:
		super().__init__()
		self.bot = bot


	# Fonction dédiée à la commande !ping
	@commands.command()
	async def ping(self, ctx):
		msg = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logger.infoLog(msg)
		
		await ctx.send("pong")


	# Fonction dédiée à la commande !help
	@commands.command()
	async def help(self, ctx):
		msg = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logger.infoLog(msg)

		help_embed = discord.Embed(
			title = "Commandes du Bot",
			description = "Voici la liste des commandes disponibles du Bot :",
			color = 0xF59E00
		)

		help_embed.add_field(name="Help", value="Elle permet d'accéder à l'aide sur les autres commandes.\n```!help```", inline=False)
		help_embed.add_field(name="Ping", value="Elle permet de mesurer le temps mis, pour recevoir une réponse.\n```!ping```", inline=False)
		help_embed.add_field(name="Esiea", value="Elle permet d'obtenir le lien direct du site officiel de l'ESIEA.\n```!esiea```", inline=False)
		help_embed.add_field(name="Hyperplanning", value="Elle permet d'obtenir le lien direct de l'Hyperplanning de l'ESIEA.\n```!hyperplanning, !hyper ou bien !planning```", inline=False)
		help_embed.add_field(name="Moodle", value="Elle permet d'obtenir le lien direct du Moodle de l'ESIEA.\n```!moodle```", inline=False)

		help_embed.set_footer(text="Information demandée par: {}".format(ctx.author.display_name))

		await ctx.send(embed=help_embed)


	# Fonction dédiée à la commande !esiea
	@commands.command()
	async def esiea(self, ctx):
		msg = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logger.infoLog(msg)

		esiea_embed = discord.Embed(
			title = "Site officiel de l'ESIEA",
			url="https://www.esiea.fr/",
			description = "Voici le lien, qui vous redirigera directement sur le site officiel de l'ESIEA.",
			color = 0x151D34
		)

		esiea_embed.set_footer(text="Information demandée par: {}".format(ctx.author.display_name))

		await ctx.send(embed=esiea_embed)


	# Fonction dédiée à la commande !hyperplanning, !hyper ou !planning
	@commands.command(aliases=['hyper', 'planning'])
	async def hyperplanning(self, ctx):
		msg = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logger.infoLog(msg)

		hyperplanning_embed = discord.Embed(
			title = "Hyperplanning ESIEA",
			url="https://edt.esiea.fr/",
			description = "Voici le lien, qui vous redirigera directement sur l'Hyperplanning de l'ESIEA.",
			color = 0xAF194F
		)
		
		hyperplanning_embed.set_footer(text="Information demandée par: {}".format(ctx.author.display_name))
		
		await ctx.send(embed=hyperplanning_embed)


	# Fonction dédiée à la commande !moodle
	@commands.command()
	async def moodle(self, ctx):
		msg = f"{ctx.message.author.name} says " + str(ctx.message.content)
		Logger.infoLog(msg)

		moodle_embed = discord.Embed(
			title = "Moodle ESIEA",
			url="https://learning.esiea.fr/",
			description = "Voici le lien, qui vous redirigera directement sur le Moddle de l'ESIEA.",
			color = 0x36A9E1
		)

		moodle_embed.set_footer(text="Information demandée par: {}".format(ctx.author.display_name))

		await ctx.send(embed=moodle_embed)
