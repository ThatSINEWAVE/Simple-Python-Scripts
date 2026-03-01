from utils.package_installer import install_dependencies
install_dependencies()

from alien_invasion import AlienInvasion

if __name__ == "__main__":
    print("\n=== STARTING ALIEN INVASION ===\n")
    ai = AlienInvasion()
    ai.run_game()
    