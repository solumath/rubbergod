from disnake.ext.commands import Bot

from .cog import Random


def setup(bot: Bot):
    bot.add_cog(Random(bot))