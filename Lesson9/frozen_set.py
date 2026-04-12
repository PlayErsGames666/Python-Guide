# frozenset не подвержены изменениями, как кортеджи
# тоесть на них не работают .add() или .update()

new_data = frozenset([5, 7, 3, 5, 7, 16, 32, True, '5', 5, 12, 3, 5, 'hello'])

# new_data.add(7) # не работает
# new_data.update(7, 8) # не работает
new_data.pop() # не работает

print(new_data)