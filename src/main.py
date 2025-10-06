import game
import traceback
import sys

def main():
    try:
        games = game.Game()
        games.run()
    except pygame.error as e:
        print("\n⚠️ PYGAME ERROR ⚠️")
        print("Most likely: Missing assets or display driver issue")
        print(f"Details: {str(e)}")
    except Exception as e:
        print("\n💥 CRITICAL ERROR 💥")
        traceback.print_exc()
    finally:
        input("\nPress Enter to exit...")  # Keeps window open
        sys.exit(1 if isinstance(e, Exception) else 0)

if __name__ == "__main__":
    main()