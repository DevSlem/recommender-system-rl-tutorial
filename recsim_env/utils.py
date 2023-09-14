import gym
import gymnasium

def gym_space_migration(gym_space: gym.Space) -> gymnasium.Space:
    if isinstance(gym_space, gym.spaces.Discrete):
        return gymnasium.spaces.Discrete(gym_space.n)

    elif isinstance(gym_space, gym.spaces.Box):
        return gymnasium.spaces.Box(
            low=gym_space.low,
            high=gym_space.high,
            shape=gym_space.shape,
            dtype=gym_space.dtype
        )

    elif isinstance(gym_space, gym.spaces.Dict):
        migrated_dict = {key: gym_space_migration(space) for key, space in gym_space.spaces.items()}
        return gymnasium.spaces.Dict(migrated_dict)

    elif isinstance(gym_space, gym.spaces.MultiDiscrete):
        return gymnasium.spaces.MultiDiscrete(gym_space.nvec)

    elif isinstance(gym_space, gym.spaces.Tuple):
        migrated_spaces = tuple(gym_space_migration(space) for space in gym_space.spaces)
        return gymnasium.spaces.Tuple(migrated_spaces)

def pretty_print_configs(config):
    return {
        "env": config.env,
        "framework": config.framework_str,
        "gamma": config.gamma
    }
