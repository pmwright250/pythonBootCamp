# Modifying Global Scope
enemies = 1

def increase_enemies(enemy):
    # Able to get the global variable; otherwise could not increment
    # global enemies
    # enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")



