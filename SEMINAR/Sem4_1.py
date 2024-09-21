def print_world(text: str) -> None:
    world_list = sorted(text.split())
    max_len = len(max(world_list, key=len))

    for nn, world in enumerate(world_list, 1):
        print(f'{nn} {world:>{max_len}}')

print_world('каждый охотник желает знать где сидят фазаны')