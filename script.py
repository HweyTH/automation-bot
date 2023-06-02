import argparse
import os
import WindowsBot

if __name__ == "main":
    parser = argparse.ArgumentParser(description="Clean up directory and sort files by types")

    parser.add_argument("--path", type=str, default=".", help="**Directory to start clean-up")

    bot = WindowsBot(parser)

    bot.dirList()

    print(f"Current directory is : {bot.dir}")

    print(type(bot))
     