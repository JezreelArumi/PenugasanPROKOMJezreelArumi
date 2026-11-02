# 6.12 Extensions
# Extends alien.py / aliens.py: a fleet of aliens with names and new keys,
# where the first three change color, speed, and points.
aliens = []

for alien_number in range(5):
    new_alien = {
        'name': f"Alien {alien_number + 1}",
        'color': 'green',
        'points': 5,
        'speed': 'slow',
        'x_position': alien_number * 10,
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

total_points = 0
for alien in aliens:
    print(f"{alien['name']}: {alien['color']}, {alien['speed']} speed, "
          f"worth {alien['points']} points, at x = {alien['x_position']}.")
    total_points = total_points + alien['points']

print(f"\nShooting every alien earns {total_points} points!")